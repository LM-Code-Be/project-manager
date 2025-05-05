# ---------------------------------------------
# Auteur   : LM-Code
# Site     : https://lm-code.be
# GitHub   : https://github.com/LM-Code-Be
# Projet   : Project Manager (Flask + MySQL)
# ---------------------------------------------


from os import getenv, path

basedir = path.abspath(path.dirname(__file__))

class Config:
    SECRET_KEY = getenv("SECRET_KEY", "changeme‑en‑prod")
    SQLALCHEMY_DATABASE_URI = getenv(
        "DATABASE_URL",
        # ex : mysql+pymysql://user:pwd@localhost/project_manager
        "mysql+pymysql://lm-code:lm-code@localhost/project-manager"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # nom pour le footer
    SITE_NAME = "Project-Manager"
