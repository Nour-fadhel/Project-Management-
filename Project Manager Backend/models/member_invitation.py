from extentions import db
from datetime import datetime, timedelta ,timezone


class MemberInvitation(db.Model):
    __tablename__ = 'member_invitations'

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey('projects.id'), nullable=False)
    invited_by = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    token = db.Column(db.String(255), unique=True, nullable=False)
    status = db.Column(db.String(20), default='pending')  # pending, accepted, expired
    sent_at = db.Column(db.DateTime, default=datetime.utcnow)

    expires_at = db.Column(db.DateTime)

    # Relationships
    project = db.relationship('Project', backref='invitations')
    inviter = db.relationship('User', foreign_keys=[invited_by], backref='sent_invitations')

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Set expiration to 7 days from now if not provided
        if not self.expires_at:
            self.expires_at = datetime.utcnow() + timedelta(days=7)

    def is_valid(self):
        """Check if invitation is still valid"""
        if self.status != "pending" or not self.expires_at:
            return False

        return datetime.utcnow() < self.expires_at

    def to_dict(self):
        """Convert to dictionary"""
        return {
            'id': self.id,
            'email': self.email,
            'project_id': self.project_id,
            'invited_by': self.invited_by,
            'token': self.token,
            'status': self.status,
            'sent_at': self.sent_at.isoformat() if self.sent_at else None,
            'expires_at': self.expires_at.isoformat() if self.expires_at else None
        }

    def __repr__(self):
        return f'<MemberInvitation {self.email} for project {self.project_id}>'