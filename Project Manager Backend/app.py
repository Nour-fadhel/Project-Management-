from flask import Flask
from flask_cors import CORS
from config import Config

from extentions import db, bcrypt, jwt, mail, migrate


def create_app():
    app = Flask(__name__)

    # ===========================
    #   CONFIG
    # ===========================
    app.config.from_object(Config)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JWT_SECRET_KEY"] = Config.JWT_SECRET_KEY

    # ===========================
    #   INIT EXTENSIONS
    # ===========================
    db.init_app(app)
    bcrypt.init_app(app)
    jwt.init_app(app)
    mail.init_app(app)
    migrate.init_app(app, db)

    # ===========================
    #   CORS
    # ===========================
    CORS(
        app,
        resources={r"/*": {"origins": "http://localhost:5173"}},
        supports_credentials=True
    )



    # ===========================
    #   REGISTER ROUTES
    # ===========================
    from routes.auth_routes import auth_bp
    from routes.admin_routes import admin_bp
    from routes.invitation_routes import invitation_bp
    from routes.task_routes import task_bp
    from routes.project_routes import project_bp
    from routes.sentiment_routes import sentiment_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(admin_bp, url_prefix="/admin")
    app.register_blueprint(invitation_bp, url_prefix="/invitation")
    app.register_blueprint(task_bp, url_prefix="/tasks")
    app.register_blueprint(project_bp, url_prefix="/projects")
    app.register_blueprint(sentiment_bp, url_prefix="/sentiment")

    return app


app = create_app()


if __name__ == "__main__":
    print("=" * 50)
    print("Available routes:")
    for rule in app.url_map.iter_rules():
        if rule.endpoint != "static":
            print(f"{rule.rule} -> {list(rule.methods)}")
    print("=" * 50)

    app.run(debug=True, host="0.0.0.0", port=5000)
