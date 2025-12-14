from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from flask_bcrypt import generate_password_hash, check_password_hash
from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from extentions import db, bcrypt
from models.user_model import User



auth_bp = Blueprint("auth", __name__)


@auth_bp.route('/login', methods=['POST', 'OPTIONS'])
def login():
    """Login and get JWT token"""
    if request.method == 'OPTIONS':
        return '', 200

    try:
        # ✅ Import User from app.py
        from models.user_model import User

        data = request.json
        email = data.get("email")
        password = data.get("password")

        print(f"🔐 Login attempt for: {email}")

        if not email or not password:
            return jsonify({"message": "Email and password are required"}), 400

        # Find user
        user = User.query.filter_by(email=email).first()
        if not user:
            print(f"❌ User not found: {email}")
            return jsonify({"message": "Invalid email or password"}), 401

        # Check password
        if not check_password_hash(user.password, password):
            print(f"❌ Invalid password for: {email}")
            return jsonify({"message": "Invalid email or password"}), 401

        print(f"✅ Password verified for: {email}, role: {user.role}")

        # Create JWT with user dict as identity
        identity_data = {
            "id": user.id,
            "email": user.email,
            "name": user.name,
            "role": user.role
        }

        print(f"🎫 Creating token with identity: {identity_data}")

        access_token = create_access_token(identity=identity_data)

        # Verify token was created
        if not access_token:
            print("❌ Token creation failed!")
            return jsonify({"message": "Token creation failed"}), 500

        print(f"✅ Token created: {access_token[:50]}...")
        print(f"✅ Token length: {len(access_token)}")

        # Verify token has 3 parts
        token_parts = access_token.split('.')
        print(f"✅ Token parts: {len(token_parts)} (should be 3)")

        if len(token_parts) != 3:
            print(f"❌ WARNING: Token has {len(token_parts)} parts instead of 3!")

        response_data = {
            "message": "Login successful",
            "token": access_token,
            "user": {
                "id": user.id,
                "name": user.name,
                "email": user.email,
                "role": user.role
            }
        }

        print(f"✅ Sending response with token")
        return jsonify(response_data), 200

    except Exception as e:
        print(f"❌ Login error: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({"message": f"Error: {str(e)}"}), 500


@auth_bp.route('/signup', methods=['POST', 'OPTIONS'])
def signup():
    """Sign up a new user"""
    if request.method == 'OPTIONS':
        return '', 200

    try:
        from models.user_model import User

        data = request.json
        name = data.get("name")
        email = data.get("email")
        password = data.get("password")

        if not name or not email or not password:
            return jsonify({"message": "Name, email, and password are required"}), 400

        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({"message": "Email already registered"}), 400

        hashed_password = generate_password_hash(password).decode('utf-8')

        new_user = User(
            name=name,
            email=email,
            password=hashed_password,
            role="member"
        )

        db.session.add(new_user)
        db.session.commit()

        # Create token with user dict
        identity_data = {
            "id": new_user.id,
            "email": new_user.email,
            "name": new_user.name,
            "role": new_user.role
        }

        access_token = create_access_token(identity=identity_data)

        return jsonify({
            "message": "User created successfully",
            "token": access_token,
            "user": new_user.to_dict()
        }), 201

    except Exception as e:
        db.session.rollback()
        print(f"❌ Signup error: {str(e)}")
        return jsonify({"message": f"Error: {str(e)}"}), 500


@auth_bp.route('/verify-token', methods=['GET', 'OPTIONS'])
@jwt_required()
def verify_token():
    """Verify if JWT token is valid"""
    if request.method == 'OPTIONS':
        return '', 200

    try:
        current_user = get_jwt_identity()
        print(f"✅ Token verified, identity: {current_user}")
        return jsonify({
            "valid": True,
            "user": current_user
        }), 200
    except Exception as e:
        print(f"❌ Token verification failed: {str(e)}")
        return jsonify({"valid": False, "message": str(e)}), 401