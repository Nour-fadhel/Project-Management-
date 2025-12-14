from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_mail import Message
from extentions import db, mail
import secrets
from datetime import datetime, timedelta, timezone

invitation_bp = Blueprint("invitation", __name__)


@invitation_bp.route("/send-invitation", methods=["POST"])
@jwt_required()
def send_invitation():
    try:
        from models.user_model import User
        from models.project_model import Project
        from models.member_invitation import MemberInvitation

        # 🔑 JWT identity
        current_user_identity = get_jwt_identity()
        current_user_id = current_user_identity.get("id")

        current_user = User.query.get(current_user_id)
        if not current_user:
            return jsonify({"message": "User not found"}), 404

        if current_user.role != "admin":
            return jsonify({"message": "Only admins can send invitations"}), 403

        data = request.get_json()
        email = data.get("email")
        project_id = data.get("project_id")

        if not email or not project_id:
            return jsonify({"message": "Email and project_id are required"}), 400

        project = Project.query.get(project_id)
        if not project:
            return jsonify({"message": "Project not found"}), 404

        if User.query.filter_by(email=email).first():
            return jsonify({"message": "User already registered"}), 400

        if MemberInvitation.query.filter_by(
            email=email,
            project_id=project_id,
            status="pending"
        ).first():
            return jsonify({"message": "Invitation already sent"}), 400

        token = secrets.token_urlsafe(32)

        invitation = MemberInvitation(
            email=email,
            project_id=project_id,
            invited_by=current_user.id,
            token=token,
            status="pending",
            expires_at=datetime.now(timezone.utc) + timedelta(days=7)
        )

        db.session.add(invitation)
        db.session.commit()

        msg = Message(
            subject=f"🎯 Invitation to join {project.title}",
            recipients=[email],
            sender=current_app.config["MAIL_DEFAULT_SENDER"]
        )

        registration_link = f"http://localhost:5173/register?token={token}"

        msg.body = f"""
Hello!

You have been invited by {current_user.name} to join the project "{project.title}".

Register here:
{registration_link}

This invitation expires in 7 days.
"""

        mail.send(msg)

        return jsonify({"message": "Invitation sent successfully"}), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"message": str(e)}), 500


@invitation_bp.route("/validate-invitation/<token>", methods=["GET"])
def validate_invitation(token):
    from models.member_invitation import MemberInvitation
    from models.project_model import Project
    from datetime import datetime, timezone

    invitation = MemberInvitation.query.filter_by(token=token).first()

    if not invitation:
        return jsonify({"message": "Invalid invitation"}), 404

    if invitation.status != "pending" or datetime.now(timezone.utc) > invitation.expires_at:
        return jsonify({"message": "Invitation expired"}), 400

    project = Project.query.get(invitation.project_id)

    return jsonify({
        "email": invitation.email,
        "project_name": project.title
    }), 200


@invitation_bp.route("/register-with-invitation", methods=["POST"])
def register_with_invitation():
    """Register a new user with invitation token"""
    try:
        from models.user_model import User
        from models.member_invitation import MemberInvitation
        from models.project_member_model import ProjectMember

        data = request.get_json()
        token = data.get("token")
        name = data.get("name")
        password = data.get("password")

        if not all([token, name, password]):
            return jsonify({"message": "All fields are required"}), 400

        invitation = MemberInvitation.query.filter_by(token=token).first()
        if not invitation or not invitation.is_valid():
            return jsonify({"message": "Invalid or expired invitation"}), 400

        if User.query.filter_by(email=invitation.email).first():
            return jsonify({"message": "User already exists"}), 400

        # Create user
        new_user = User(name=name, email=invitation.email, role="member")
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.flush()

        # ✅ ADD TO PROJECT_MEMBERS
        project_member = ProjectMember(
            project_id=invitation.project_id,
            user_id=new_user.id,
            joined_at=datetime.now(timezone.utc)
        )
        db.session.add(project_member)

        # Mark invitation as accepted
        invitation.status = "accepted"

        db.session.commit()

        print(f"✅ User {new_user.email} added to project {invitation.project_id}")

        return jsonify({
            "message": "Registration successful",
            "user": new_user.to_dict()
        }), 201

    except Exception as e:
        db.session.rollback()
        print(f"❌ Registration error: {str(e)}")
        import traceback
        traceback.print_exc()
        return jsonify({"message": str(e)}), 500