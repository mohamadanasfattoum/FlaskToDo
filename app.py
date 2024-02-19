from flask import Flask, render_template, request, redirect, jsonify
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



if __name__ == "__main__": # to run server
    app.run(debug=True)