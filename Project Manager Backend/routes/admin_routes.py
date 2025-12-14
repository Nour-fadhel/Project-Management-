from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_bcrypt import generate_password_hash
from extentions import db
from models.user_model import User
from models.task_model import Task
from models.project_model import  Project
from models.project_member_model import ProjectMember
import secrets
from datetime import datetime, timedelta, timezone

admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/add-member", methods=["POST", "OPTIONS"])
@jwt_required()
def add_member():
    """Add a member directly to a project (admin only)"""
    if request.method == 'OPTIONS':
        return '', 200

    try:
        current_user = get_jwt_identity()

        # Check admin role
        if current_user["role"] != "admin":
            return jsonify({"message": "Only admins can add members"}), 403

        data = request.json
        name = data.get("name")
        email = data.get("email")
        password = data.get("password", "ChangeMe123!")
        project_id = data.get("project_id")

        # Validation
        if not name or not email or not project_id:
            return jsonify({"message": "Name, email, and project_id are required"}), 400

        # Check if project exists
        project = Project.query.get(project_id)
        if not project:
            return jsonify({"message": "Project not found"}), 404

        # Check if email already exists
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return jsonify({"message": "Email already registered"}), 400

        # Hash password
        hashed_password = generate_password_hash(password).decode('utf-8')

        # Create user
        new_member = User(
            name=name,
            email=email,
            password=hashed_password,
            role='member'
        )

        db.session.add(new_member)
        db.session.flush()  # Get the ID without committing

        # Add user to project
        project_member = ProjectMember(
            project_id=project_id,
            user_id=new_member.id
        )

        db.session.add(project_member)
        db.session.commit()

        return jsonify({
            "message": "Member added successfully",
            "member": {
                "id": new_member.id,
                "name": new_member.name,
                "email": new_member.email,
                "project_id": project_id,
                "default_password": password
            }
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Error: {str(e)}"}), 500


@admin_bp.route("/projects", methods=["GET", "OPTIONS"])
@jwt_required()
def get_all_projects():
    """Get all projects (admin only)"""
    if request.method == 'OPTIONS':
        return '', 200

    try:
        current_user = get_jwt_identity()

        # Check admin role
        if current_user["role"] != "admin":
            return jsonify({"message": "Only admins can view all projects"}), 403

        projects = Project.query.all()
        return jsonify([project.to_dict() for project in projects]), 200

    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500


@admin_bp.route("/users", methods=["GET", "OPTIONS"])
@jwt_required()
def get_all_users():
    """Get all users (admin only)"""
    if request.method == 'OPTIONS':
        return '', 200

    try:
        current_user = get_jwt_identity()

        # Check admin role
        if current_user["role"] != "admin":
            return jsonify({"message": "Only admins can view all users"}), 403

        users = User.query.all()
        return jsonify([user.to_dict() for user in users]), 200

    except Exception as e:
        return jsonify({"message": f"Error:  {str(e)}"}), 500


@admin_bp.route("/dashboard/stats", methods=["GET", "OPTIONS"])
@jwt_required()
def get_dashboard_stats():
    """Get admin dashboard statistics"""
    if request.method == 'OPTIONS':
        return '', 200

    try:
        from sqlalchemy import func
        from app import Task
        from datetime import date

        current_user = get_jwt_identity()

        # Check admin role
        if current_user["role"] != "admin":
            return jsonify({"message": "Only admins can access dashboard"}), 403

        # Total counts
        total_users = User.query.count()
        total_projects = Project.query.count()
        total_tasks = Task.query.count()

        # Task statistics
        status_counts = db.session.query(
            Task.status,
            func.count(Task.id).label('count')
        ).group_by(Task.status).all()

        priority_counts = db.session.query(
            Task.priority,
            func.count(Task.id).label('count')
        ).group_by(Task.priority).all()

        # Overdue tasks
        today = date.today()
        overdue_tasks = Task.query.filter(
            Task.due_date.isnot(None),
            Task.due_date < today,
            Task.status != 'done'
        ).count()

        # Recent tasks
        recent_tasks = Task.query.order_by(Task.created_at.desc()).limit(10).all()

        # Team sentiment (if available)
        from app import Message

        messages_with_sentiment = Message.query.filter(
            Message.sentiment.isnot(None)
        ).all()

        sentiment_stats = {}
        if messages_with_sentiment:
            for msg in messages_with_sentiment:
                sentiment = msg.sentiment
                sentiment_stats[sentiment] = sentiment_stats.get(sentiment, 0) + 1

        return jsonify({
            "users": {
                "total": total_users
            },
            "projects": {
                "total": total_projects
            },
            "tasks": {
                "total": total_tasks,
                "by_status": {status: count for status, count in status_counts},
                "by_priority": {priority: count for priority, count in priority_counts},
                "overdue": overdue_tasks
            },
            "sentiment": sentiment_stats,
            "recent_tasks": [task.to_dict() for task in recent_tasks]
        }), 200

    except Exception as e:
        return jsonify({"message": f"Error: {str(e)}"}), 500