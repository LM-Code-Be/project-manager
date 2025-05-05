# ---------------------------------------------
# Auteur   : LM-Code
# Site     : https://lm-code.be
# GitHub   : https://github.com/LM-Code-Be
# Projet   : Project Manager (Flask + MySQL)
# ---------------------------------------------


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_wtf.csrf import CSRFProtect
from .config import Config
from datetime import datetime

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()
csrf = CSRFProtect()

login_manager.login_view = "auth.login"
login_manager.login_message_category = "warning"

def create_app(config_class: type[Config] = Config) -> Flask:
    app = Flask(__name__)
    app.config.from_object(config_class)

    # init extensions
    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    csrf.init_app(app)

    # bleuprints
    from .routes import auth_bp, dashboard_bp, projects_bp, tasks_bp, users_bp
    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(projects_bp,  url_prefix="/projects")
    app.register_blueprint(tasks_bp,    url_prefix="/tasks")
    app.register_blueprint(users_bp,    url_prefix="/users")

    # erreurs custom
    from flask import render_template
    @app.errorhandler(404)
    def not_found(e):   # noqa
        return render_template("404.html"), 404

    @app.errorhandler(500)
    def server_err(e):  # noqa
        return render_template("500.html"), 500
    
    @app.context_processor
    def inject_current_year():
        return {"current_year": datetime.utcnow().year}

    return app




