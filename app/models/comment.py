"""
Ptits commentaires pour collaborer sur une tâche.
"""

from datetime import datetime
from app import db

class Comment(db.Model):
    id      = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow)

    task_id = db.Column(db.Integer, db.ForeignKey("task.id"))
    task    = db.relationship("Task", back_populates="comments")

    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user    = db.relationship("User")

    def __repr__(self):
        return f"<Comment {self.id}>"
