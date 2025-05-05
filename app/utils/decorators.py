# ---------------------------------------------
# Auteur   : LM-Code
# Site     : https://lm-code.be
# GitHub   : https://github.com/LM-Code-Be
# Projet   : Project Manager (Flask + MySQL)
# ---------------------------------------------

from functools import wraps
from flask import abort
from flask_login import current_user

def role_required(role: str):
    """Déco qui bloque si l'utilisateur n'a pas le bon rôle."""
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated or current_user.role != role:
                # hop, 403
                return abort(403)
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper
