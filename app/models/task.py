"""
Model Task – status, priority, due date, etc.
"""

from datetime import datetime, date
from app import db

class Task(db.Model):
    id          = db.Column(db.Integer, primary_key=True)
    title       = db.Column(db.String(140), nullable=False)
    description = db.Column(db.Text)
    status      = db.Column(db.String(20), default="todo")       # todo / in_progress / done
    priority    = db.Column(db.String(10), default="medium")     # low/medium/high
    due_date    = db.Column(db.Date)
    created     = db.Column(db.DateTime, default=datetime.utcnow)

    # foreign
    project_id = db.Column(db.Integer, db.ForeignKey("project.id"))
    project    = db.relationship("Project", back_populates="tasks")

    # assignees (many‑to‑many via Assignment)
    assignees  = db.relationship("Assignment", back_populates="task", cascade="all, delete-orphan")

    comments   = db.relationship("Comment", back_populates="task", cascade="all, delete-orphan")

    # helpers
    def is_overdue(self) -> bool:
        return self.due_date and self.due_date < date.today() and self.status != "done"

    def get_status_display(self):
        return {
            "todo": "À faire",
            "in_progress": "En cours",
            "done": "Terminé"
        }.get(self.status, self.status)

    def __repr__(self):
        return f"<Task {self.title}>"
