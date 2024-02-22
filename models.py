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
    
    def save(self):
        db.session.add(self)
        db.session.commit()

    def get_all():  # to return all todos
        return Todo.query.all()

    def get_todo(todo_id):
        return Todo.query.get(todo_id)

    def todo_update(todo_id,name,notes):
        todo = Todo.query.get(todo_id)
        todo.name = name
        todo.notes= notes
        db.session.commit()

    def todo_delete(todo_id):
        todo = Todo.query.get(todo_id)
        db.session.delete(todo)
        db.session.commit()
