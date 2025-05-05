"""
Model Project – simple CRUD avec owner et tasks.
"""

from datetime import datetime
from app import db

class Project(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    name        = db.Column(db.String(128), nullable=False)
    description = db.Column(db.Text)
    start_date  = db.Column(db.Date)
    end_date    = db.Column(db.Date)
    completed   = db.Column(db.Boolean, default=False)
    created     = db.Column(db.DateTime, default=datetime.utcnow)

    # foreign
    owner_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    owner    = db.relationship("User", back_populates="projects")

    # tasks (one‑to‑many)
    tasks = db.relationship("Task", back_populates="project", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<Project {self.name}>"
