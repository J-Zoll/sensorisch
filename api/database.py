import os
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def setup(app):
    if not os.path.exists("instance/database.sqlite"):
        with app.app_context():
            db.create_all()