# ---------------------------------------------
# Auteur   : LM-Code
# Site     : https://lm-code.be
# GitHub   : https://github.com/LM-Code-Be
# Projet   : Project Manager (Flask + MySQL)
# ---------------------------------------------

from app import create_app

app = create_app()

if __name__ == "__main__":
    # debug True en dev, à couper en prod hein ;-)
    app.run(debug=True)
