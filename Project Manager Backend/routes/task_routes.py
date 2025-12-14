# routes/task_routes.py
from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from datetime import datetime, date
from extentions import db
from models.task_model import Task
from models.task_model import TaskComment
from models.project_model import Project
import models.user_model as user_model
import models.task_model as TaskStatus
from sqlalchemy import and_, or_
from models.project_member_model import ProjectMember
from models.project_model import Member
task_bp = Blueprint("tasks", __name__)


# ===========================
#   TASK ROUTES
# ===========================

@task_bp.route("/projects/<int:project_id>/tasks", methods=["GET"])
@jwt_required()
def get_project_tasks(project_id):
    tasks = Task.query.filter_by(project_id=project_id).all()

    return jsonify([
        {
            "id": t.id,
            "title": t.title,
            "description": t.description,
            "status": t.status,
            "priority": t.priority,
            "estimated_hours": t.estimated_hours,
            "actual_hours": t.actual_hours,
            "due_date": t.due_date.isoformat() if t.due_date else None,
            "created_at": t.created_at.isoformat() if t.created_at else None,

            # ✅ NAME instead of ID
            "assigned_to": t.assignee.name if t.assignee else "Unassigned"
        }
        for t in tasks
    ])





@task_bp.route("/projects/<int:project_id>/tasks", methods=["POST"])
@jwt_required()
def create_task(project_id):
    """Create a new task"""
    try:
        current_user = get_jwt_identity()
        data = request.json

        # Validate required fields
        title = data.get("title")
        if not title:
            return jsonify({"message": "Task title is required"}), 400

        # Check project exists
        project = Project.query.get_or_404(project_id)

        # Check if user has access to project
        if current_user["role"] == "member":
            is_member = any(user.id == current_user["id"] for user in project.user_members)
            if not is_member:
                return jsonify({"message": "Access denied"}), 403

        # Create task
        task = Task(
            title=title,
            description=data.get("description", ""),
            status=data.get("status", TaskStatus.TODO),
            priority=data.get("priority", "medium"),
            project_id=project_id,
            created_by=current_user["id"],
            assigned_to=data.get("assigned_to")
        )

        # Parse due date if provided
        if data.get("due_date"):
            try:
                task.due_date = datetime.strptime(data["due_date"], "%Y-%m-%d").date()
            except:
                return jsonify({"message": "Invalid date format. Use YYYY-MM-DD"}), 400

        if data.get("estimated_hours"):
            task.estimated_hours = float(data["estimated_hours"])

        db.session.add(task)
        db.session.commit()

        return jsonify({
            "message": "Task created successfully",
            "task": task.to_dict()
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Error creating task: {str(e)}"}), 500


@task_bp.route("/tasks/<int:task_id>", methods=["GET"])
@jwt_required()
def get_task(task_id):
    """Get a specific task"""
    try:
        current_user = get_jwt_identity()
        task = Task.query.get_or_404(task_id)

        # Check if user has access to the project
        project = Project.query.get(task.project_id)
        if current_user["role"] == "member":
            is_member = any(user.id == current_user["id"] for user in project.user_members)
            if not is_member:
                return jsonify({"message": "Access denied"}), 403

        return jsonify(task.to_dict()), 200

    except Exception as e:
        return jsonify({"message": f"Error fetching task: {str(e)}"}), 500


@task_bp.route("/tasks/<int:task_id>", methods=["PUT"])
@jwt_required()
def update_task(task_id):
    """Update a task"""
    try:
        current_user = get_jwt_identity()
        task = Task.query.get_or_404(task_id)
        data = request.json

        # Check if user can edit task
        # Members can only edit tasks assigned to them
        if current_user["role"] == "member":
            if task.assigned_to != current_user["id"]:
                return jsonify({"message": "You can only edit tasks assigned to you"}), 403

        # Update fields
        if "title" in data:
            task.title = data["title"]
        if "description" in data:
            task.description = data["description"]
        if "status" in data:
            task.status = data["status"]
        if "priority" in data:
            task.priority = data["priority"]
        if "assigned_to" in data:
            task.assigned_to = data["assigned_to"]
        if "estimated_hours" in data:
            if data["estimated_hours"] is not None and data["estimated_hours"] != "":
                task.estimated_hours = float(data["estimated_hours"])
            else:
                task.estimated_hours = None

        if "actual_hours" in data:
            if data["actual_hours"] is not None and data["actual_hours"] != "":
                task.actual_hours = float(data["actual_hours"])
            else:
                task.actual_hours = 0

        if "due_date" in data:
            if data["due_date"]:
                try:
                    task.due_date = datetime.strptime(data["due_date"], "%Y-%m-%d").date()
                except:
                    return jsonify({"message": "Invalid date format. Use YYYY-MM-DD"}), 400
            else:
                task.due_date = None

        task.updated_at = datetime.utcnow()
        db.session.commit()

        return jsonify({
            "message": "Task updated successfully",
            "task": task.to_dict()
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Error updating task: {str(e)}"}), 500


@task_bp.route("/tasks/<int:task_id>", methods=["DELETE"])
@jwt_required()
def delete_task(task_id):
    """Delete a task"""
    try:
        current_user = get_jwt_identity()
        task = Task.query.get_or_404(task_id)

        # Only admins or task creator can delete
        if current_user["role"] != "admin" and task.created_by != current_user["id"]:
            return jsonify({"message": "Access denied"}), 403

        db.session.delete(task)
        db.session.commit()

        return jsonify({"message": "Task deleted successfully"}), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Error deleting task: {str(e)}"}), 500


@task_bp.route("/tasks/<int:task_id>/status", methods=["PUT"])
@jwt_required()
def update_task_status(task_id):
    """Update only task status (for Kanban drag & drop)"""
    try:
        current_user = get_jwt_identity()
        task = Task.query.get_or_404(task_id)
        data = request.json

        new_status = data.get("status")
        if not new_status:
            return jsonify({"message": "Status is required"}), 400

        # Check if user can update status
        if current_user["role"] == "member":
            if task.assigned_to != current_user["id"]:
                return jsonify({"message": "You can only update tasks assigned to you"}), 403

        # Validate status
        valid_statuses = [TaskStatus.TODO, TaskStatus.IN_PROGRESS, TaskStatus.REVIEW, TaskStatus.DONE,
                          TaskStatus.BLOCKED]
        if new_status not in valid_statuses:
            return jsonify({"message": "Invalid status"}), 400

        # Update status
        old_status = task.status
        task.status = new_status
        task.updated_at = datetime.utcnow()

        # If moving to DONE, update actual hours if not set
        if new_status == TaskStatus.DONE and task.actual_hours == 0 and task.estimated_hours:
            task.actual_hours = task.estimated_hours

        db.session.commit()

        return jsonify({
            "message": "Task status updated",
            "task": task.to_dict(),
            "old_status": old_status,
            "new_status": new_status
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Error updating task status: {str(e)}"}), 500


@task_bp.route("/tasks/<int:task_id>/assign", methods=["PUT"])
@jwt_required()
def assign_task(task_id):
    """Assign task to a user"""
    try:
        current_user = get_jwt_identity()
        task = Task.query.get_or_404(task_id)
        data = request.json

        user_id = data.get("user_id")
        if not user_id:
            return jsonify({"message": "User ID is required"}), 400

        # Only admins or task creator can assign
        if current_user["role"] != "admin" and task.created_by != current_user["id"]:
            return jsonify({"message": "Access denied"}), 403

        # Check if user exists and is member of project
        user = user_model.query.get(user_id)
        if not user:
            return jsonify({"message": "User not found"}), 404

        project = Project.query.get(task.project_id)
        is_member = any(member.id == user_id for member in project.user_members)
        if not is_member:
            return jsonify({"message": "User is not a member of this project"}), 400

        task.assigned_to = user_id
        task.updated_at = datetime.utcnow()
        db.session.commit()

        return jsonify({
            "message": "Task assigned successfully",
            "task": task.to_dict()
        }), 200

    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Error assigning task: {str(e)}"}), 500


@task_bp.route("/tasks/<int:task_id>/comments", methods=["GET"])
@jwt_required()
def get_task_comments(task_id):
    """Get all comments for a task"""
    try:
        current_user = get_jwt_identity()
        task = Task.query.get_or_404(task_id)

        # Check access to task
        project = Project.query.get(task.project_id)
        if current_user["role"] == "member":
            is_member = any(user.id == current_user["id"] for user in project.user_members)
            if not is_member:
                return jsonify({"message": "Access denied"}), 403

        comments = TaskComment.query.filter_by(task_id=task_id).order_by(TaskComment.created_at).all()

        return jsonify([comment.to_dict() for comment in comments]), 200

    except Exception as e:
        return jsonify({"message": f"Error fetching comments: {str(e)}"}), 500


@task_bp.route("/tasks/<int:task_id>/comments", methods=["POST"])
@jwt_required()
def add_task_comment(task_id):
    """Add a comment to a task"""
    try:
        current_user = get_jwt_identity()
        task = Task.query.get_or_404(task_id)
        data = request.json

        content = data.get("content")
        if not content:
            return jsonify({"message": "Comment content is required"}), 400

        # Check access to task
        project = Project.query.get(task.project_id)
        if current_user["role"] == "member":
            is_member = any(user.id == current_user["id"] for user in project.user_members)
            if not is_member:
                return jsonify({"message": "Access denied"}), 403

        comment = TaskComment(
            task_id=task_id,
            user_id=current_user["id"],
            content=content
        )

        db.session.add(comment)
        db.session.commit()

        return jsonify({
            "message": "Comment added successfully",
            "comment": comment.to_dict()
        }), 201

    except Exception as e:
        db.session.rollback()
        return jsonify({"message": f"Error adding comment: {str(e)}"}), 500


@task_bp.route("/my-tasks", methods=["GET"])
@jwt_required()
def get_my_tasks():
    """Get tasks assigned to current user"""
    try:
        current_user = get_jwt_identity()

        # Get filters
        status_filter = request.args.get('status')
        project_filter = request.args.get('project_id')

        query = Task.query.filter_by(assigned_to=current_user["id"])

        if status_filter:
            query = query.filter_by(status=status_filter)
        if project_filter:
            query = query.filter_by(project_id=project_filter)

        tasks = query.order_by(
            Task.priority.desc(),
            Task.due_date.asc(),
            Task.created_at.desc()
        ).all()

        return jsonify([task.to_dict() for task in tasks]), 200

    except Exception as e:
        return jsonify({"message": f"Error fetching tasks: {str(e)}"}), 500


@task_bp.route("/dashboard/stats", methods=["GET"])
@jwt_required()
def get_dashboard_stats():
    """Get dashboard statistics for admin"""
    try:
        current_user = get_jwt_identity()

        # Only admins can access dashboard stats
        if current_user["role"] != "admin":
            return jsonify({"message": "Access denied"}), 403

        from sqlalchemy import func

        # Total tasks
        total_tasks = Task.query.count()

        # Tasks by status
        status_counts = db.session.query(
            Task.status,
            func.count(Task.id).label('count')
        ).group_by(Task.status).all()

        status_stats = {status: count for status, count in status_counts}

        # Tasks by priority
        priority_counts = db.session.query(
            Task.priority,
            func.count(Task.id).label('count')
        ).group_by(Task.priority).all()

        priority_stats = {priority: count for priority, count in priority_counts}

        # Overdue tasks
        today = date.today()
        overdue_tasks = Task.query.filter(
            Task.due_date.isnot(None),
            Task.due_date < today,
            Task.status != TaskStatus.DONE
        ).count()

        # Recent tasks
        recent_tasks = Task.query.order_by(Task.created_at.desc()).limit(10).all()

        return jsonify({
            "total_tasks": total_tasks,
            "by_status": status_stats,
            "by_priority": priority_stats,
            "overdue_tasks": overdue_tasks,
            "recent_tasks": [task.to_dict() for task in recent_tasks]
        }), 200

    except Exception as e:
        return jsonify({"message": f"Error fetching dashboard stats: {str(e)}"}), 500


# routes/task_routes.py - Update the create_task_for_my_project function

@task_bp.route("/my-project/tasks", methods=["POST"])
@jwt_required()
def create_task_for_my_project():
    """Create task for the project the member belongs to"""
    try:
        current_user = get_jwt_identity()
        data = request.json

        print(f"🔍 Creating task for user: {current_user}")  # Debug

        # Validate title
        if not data.get("title"):
            return jsonify({"message": "Task title is required"}), 400

        # Get user's project membership
        membership = ProjectMember.query.filter_by(
            user_id=current_user["id"]
        ).first()

        if not membership:
            print(f"❌ No membership found for user {current_user['id']}")  # Debug

            # Check all memberships for debugging
            all_memberships = ProjectMember.query.all()
            print(f"📊 Total memberships in DB: {len(all_memberships)}")
            for m in all_memberships:
                print(f"  - Project {m.project_id}, User {m.user_id}")

            return jsonify({
                "message": "You are not assigned to any project. Please contact your administrator."
            }), 403

        # Verify project exists
        project = Project.query.get(membership.project_id)
        if not project:
            return jsonify({"message": "Project not found"}), 404

        print(f"✅ Found project: {project.title} (ID: {project.id})")  # Debug

        # Parse due date
        due_date = None
        if data.get("due_date"):
            try:
                due_date = datetime.strptime(data["due_date"], "%Y-%m-%d").date()
            except:
                return jsonify({"message": "Invalid date format"}), 400

        # Create task
        task = Task(
            title=data["title"],
            description=data.get("description", ""),
            status=data.get("status", "todo"),
            priority=data.get("priority", "medium"),
            due_date=due_date,
            estimated_hours=data.get("estimated_hours"),
            project_id=membership.project_id,
            created_by=current_user["id"],
            assigned_to=current_user["id"]
        )

        db.session.add(task)
        db.session.commit()

        print(f"✅ Task created: {task.id}")  # Debug

        return jsonify({
            "message": "Task created successfully",
            "task": task.to_dict()
        }), 201

    except Exception as e:
        db.session.rollback()
        import traceback
        print(f"❌ Error creating task:")
        traceback.print_exc()
        return jsonify({"message": str(e)}), 500


@task_bp.route("/debug/my-projects", methods=["GET"])
@jwt_required()
def debug_my_projects():
    """Debug endpoint to see user's project memberships"""
    try:
        current_user = get_jwt_identity()

        memberships = ProjectMember.query.filter_by(
            user_id=current_user["id"]
        ).all()

        # Also check the old Member model
        old_memberships = db.session.query(Member).filter_by(
            email=current_user["email"]
        ).all()

        return jsonify({
            "user_id": current_user["id"],
            "email": current_user["email"],
            "project_memberships": [{
                "id": m.id,
                "project_id": m.project_id,
                "user_id": m.user_id,
                "joined_at": m.joined_at.isoformat() if m.joined_at else None
            } for m in memberships],
            "old_memberships": [{
                "id": m.id,
                "name": m.name,
                "email": m.email,
                "project_id": m.project_id
            } for m in old_memberships]
        }), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


