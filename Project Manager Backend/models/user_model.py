from extentions import db
from flask_bcrypt import generate_password_hash, check_password_hash

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), default='member')

    def set_password(self, password):
        """Hash and set password"""
        self.password = generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        """Check if password matches hash"""
        return check_password_hash(self.password, password)

    def to_dict(self):
        """Convert user to dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'role': self.role,
        }

    @staticmethod
    def find_by_email(email):
        """Find user by email"""
        user = User.query.filter_by(email=email).first()
        if user:
            return user
        return None

    def __repr__(self):
        return f'<User {self.email}>'