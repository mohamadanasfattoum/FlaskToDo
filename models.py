from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# define model

class Todo(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100) , nullable=False) 
    notes = db.Column(db.String(500)) 

    def __init__(self, name, notes=''): # tp show the same name
        self.name=name
        self.notes=notes
    
    def get_all():  # to return all todos
        return Todo.query.all()