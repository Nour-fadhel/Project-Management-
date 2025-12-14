from extentions import db
class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150), nullable=False)
    description = db.Column(db.Text, nullable=False)
    deadline = db.Column(db.String(20), nullable=False)
    members = db.relationship("Member", backref="project", cascade="all, delete-orphan", lazy='dynamic')

    def __repr__(self):
        return f'<Project {self.title}>'


class Member(db.Model):
    __tablename__ = 'members'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    project_id = db.Column(db.Integer, db.ForeignKey("projects.id"))

    def __repr__(self):
        return f'<Member {self.name}>'

