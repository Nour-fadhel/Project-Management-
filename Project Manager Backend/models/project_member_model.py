# models/project_member_model.py
from extentions import db
from datetime import datetime

class ProjectMember(db.Model):
    __tablename__ = 'project_members'

    id = db.Column(db.Integer, primary_key=True)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    joined_at = db.Column(db.DateTime, default=datetime.utcnow)

    # relationships
    project = db.relationship('Project', backref=db.backref('project_members', lazy='dynamic'))
    user = db.relationship('User', backref=db.backref('project_associations', lazy='dynamic'))

    def __repr__(self):
        return f'<ProjectMember project_id={self.project_id} user_id={self.user_id}>'
