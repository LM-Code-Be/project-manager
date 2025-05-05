# 🗂️ Project Manager – Gestion de projets collaboratifs avec Flask & MySQL

Développé par [LM-Code](https://lm-code.be) – GitHub : [@LM-Code-Be](https://github.com/LM-Code-Be)

---

## 📌 Présentation

**Project Manager** est une application web complète de gestion de projets collaboratifs (type Trello simplifié), construite avec :

- **Python Flask** pour le backend
- **MySQL** pour la base de données relationnelle
- **Bootstrap 5** pour une interface moderne et responsive
- **Chart.js** pour des statistiques visuelles et dynamiques

L'application permet de :
- créer et gérer des projets
- ajouter des tâches avec échéances, priorités et statuts
- assigner des utilisateurs aux tâches
- suivre l’avancement grâce à un dashboard dynamique
- voir les tâches en retard, terminées ou en cours

---

## 🧰 Stack technique

- Python 3.10+
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-Migrate
- MySQL (local ou distant)
- Bootstrap 5 + Chart.js
- Jinja2

---

## 🚀 Fonctionnalités principales

- Authentification sécurisée (hash + rôles)
- Création/édition de projets et de tâches
- Assignation de plusieurs utilisateurs par tâche
- Dashboard visuel :
  - Graphique des tâches créées par mois
  - Répartition des statuts : À faire, En cours, Terminé
- Interface responsive mobile/desktop
- Gestion des utilisateurs (admin only)

---

## 🖥️ Captures d’écran

![alt text](image.png)

---

## ⚙️ Installation locale

### 1. Cloner le projet

```bash
git clone https://github.com/LM-Code-Be/project-manager.git
cd project-manager

2. Créer un environnement virtuel

python -m venv venv
venv\Scripts\activate  # sur Windows

3. Installer les dépendances

pip install -r requirements.txt

4. Configurer la base de données

Créer une base project_manager dans MySQL (phpMyAdmin ou CLI) puis adapter app/config.py si besoin :

SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:motdepasse@localhost/project_manager"

5. Appliquer les migrations

flask db init      # une seule fois
flask db migrate -m "Initial"
flask db upgrade

6. Lancer l'application

python run.py

L'application sera disponible sur : http://localhost:5000


👤 Auteur

Développé par LM-Code
GitHub : https://github.com/LM-Code-Be
📝 Licence

Ce projet est open source et disponible sous licence MIT.
💬 Suggestions / Contributions

Tu peux ouvrir une issue ou proposer une pull request si tu souhaites contribuer ou signaler un bug. N'hésite pas à me contacter si tu veux échanger autour de ce projet !

