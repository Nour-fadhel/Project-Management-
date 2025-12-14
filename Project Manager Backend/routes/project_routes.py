from flask import Blueprint, request, jsonify, current_app
from flask_jwt_extended import jwt_required
from datetime import datetime, timezone

from extentions import db, mail
from flask_mail import Message

from models.project_model import Project, Member
from models.project_member_model import ProjectMember
from models.member_invitation import MemberInvitation
from models.task_model import Task

# ✅ CORRECT BLUEPRINT
project_bp = Blueprint("project", __name__)


# ===========================
#   PROJECT ROUTES
# ===========================
@project_bp.route("/", methods=["GET"])
def get_projects():
    projects = Project.query.all()
    return jsonify([
        {
            "id": p.id,
            "title": p.title,
            "description": p.description,
            "deadline": p.deadline,
            "members": [{"id": m.id, "name": m.name, "email": m.email} for m in p.members]
        }
        for p in projects
    ]), 200


@project_bp.route("/", methods=["POST"])
def add_project():
    data = request.json
    project = Project(
        title=data.get("title"),
        description=data.get("description"),
        deadline=data.get("deadline")
    )
    db.session.add(project)
    db.session.commit()
    return jsonify({"message": "Project created", "id": project.id}), 201


@project_bp.route("/<int:project_id>", methods=["GET"])
def get_project(project_id):
    project = Project.query.get_or_404(project_id)
    return jsonify({
        "id": project.id,
        "title": project.title,
        "description": project.description,
        "deadline": project.deadline,
        "members": [{"id": m.id, "name": m.name, "email": m.email} for m in project.members]
    }), 200


@project_bp.route("/<int:project_id>", methods=["PUT"])
def update_project(project_id):
    project = Project.query.get_or_404(project_id)
    data = request.json
    project.title = data.get("title", project.title)
    project.description = data.get("description", project.description)
    project.deadline = data.get("deadline", project.deadline)
    db.session.commit()
    return jsonify({"message": "Project updated"}), 200


@project_bp.route("/<int:project_id>", methods=["DELETE"])
def delete_project(project_id):
    ProjectMember.query.filter_by(project_id=project_id).delete()
    MemberInvitation.query.filter_by(project_id=project_id).delete()
    Task.query.filter_by(project_id=project_id).delete()

    project = Project.query.get_or_404(project_id)
    db.session.delete(project)
    db.session.commit()

    return jsonify({"message": "Project deleted"}), 200


# ===========================
#   MEMBER ROUTES
# ===========================
@project_bp.route("/<int:project_id>/members", methods=["GET"])
def get_members(project_id):
    project = Project.query.get_or_404(project_id)
    return jsonify([
        {"id": m.id, "name": m.name, "email": m.email}
        for m in project.members
    ]), 200


@project_bp.route("/<int:project_id>/members", methods=["POST"])
def add_member(project_id):
    data = request.json
    member = Member(
        name=data.get("name"),
        email=data.get("email"),
        project_id=project_id
    )
    db.session.add(member)
    db.session.commit()
    return jsonify({"message": "Member added"}), 201


@project_bp.route("/<int:project_id>/members/<int:member_id>", methods=["DELETE"])
def remove_member(project_id, member_id):
    member = Member.query.filter_by(id=member_id, project_id=project_id).first_or_404()
    db.session.delete(member)
    db.session.commit()
    return jsonify({"message": "Member removed"}), 200


# ===========================
#   HEALTH CHECK
# ===========================
@project_bp.route("/health", methods=["GET"])
def health_check():
    return jsonify({
        "status": "ok",
        "service": "project"
    }), 200
