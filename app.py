from flask import Flask, render_template, request, redirect, jsonify, url_for
from flask_sqlalchemy import SQLAlchemy
from models import db, Todo
import os


app = Flask(__name__)


# db path
base_dir = os.path.abspath(os.path.dirname(__file__))
db_path = os.path.join(base_dir,'todo.db')

# flask config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + db_path
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


# create tables when start as migrate
with app.app_context():
    db.create_all()

# views
@app.route('/') # url
def todo_list():
    data = Todo.get_all()
    return render_template('list.html', todos=data)

@app.route('/add', methods=['POST'])
def add_todo():
    name = request.form['task']
    notes = request.form['note']
    todo = Todo(name,notes)
    todo.save()
    return redirect(url_for('todo_list'))


@app.route('/delete/<int:todo_id>', methods=['POST'])
def delete_todo(todo_id):
    Todo.todo_delete(todo_id)
    return redirect(url_for('todo_list'))






if __name__ == "__main__": # to run server
    app.run(debug=True)