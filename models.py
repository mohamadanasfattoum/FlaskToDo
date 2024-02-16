from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# define model

class Todo(db.model):
    id = db.Column(db.Integer, primary_key=True)