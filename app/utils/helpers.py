# ---------------------------------------------
# Auteur   : LM-Code
# Site     : https://lm-code.be
# GitHub   : https://github.com/LM-Code-Be
# Projet   : Project Manager (Flask + MySQL)
# ---------------------------------------------

def paginate(query, page, per_page=20):
    """Renvoie un objet pagination de SQLAlchemy."""
    return query.paginate(page=page, per_page=per_page, error_out=False)
