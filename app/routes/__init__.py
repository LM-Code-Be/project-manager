"""
Expose les Blueprints pour import facile dans create_app().
"""

from .auth      import bp as auth_bp
from .dashboard import bp as dashboard_bp
from .projects  import bp as projects_bp
from .tasks     import bp as tasks_bp
from .users     import bp as users_bp
