"""
Table d'association user <-> task.
"""

from datetime import datetime
from app import db

class Assignment(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    task_id = db.Column(db.Integer, db.ForeignKey("task.id"))

    user = db.relationship("User", back_populates="tasks_asg")
    task = db.relationship("Task", back_populates="assignees")

    def __repr__(self):
        return f"<Assignment u{self.user_id}-t{self.task_id}>"
