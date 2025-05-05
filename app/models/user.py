"""
Model User – gère auth + rôles.
"""

from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login_manager

class User(UserMixin, db.Model):
    id       = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, nullable=False)
    email    = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    role     = db.Column(db.String(20), default="member")  # admin / member
    created  = db.Column(db.DateTime, default=datetime.utcnow)

    # relations
    projects  = db.relationship("Project", back_populates="owner", lazy="dynamic")
    tasks_asg = db.relationship("Assignment", back_populates="user", lazy="dynamic")

    # —‑ methods —‑
    def set_password(self, pwd: str):
        self.password_hash = generate_password_hash(pwd)

    def check_password(self, pwd: str) -> bool:
        return check_password_hash(self.password_hash, pwd)

    def is_admin(self) -> bool:
        return self.role == "admin"

    def __repr__(self):
        return f"<User {self.username}>"

# loader login_manager
@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))
