from flask import Flask, render_template, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from models import db, Todo



app = Flask(__name__)

# flask config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'
db.init_app(app)

# create tables when start as migrate
# with app.app_context():
#     db.create_all()

# views
@app.route('/') # url
def todo_list():
    data = Todo.get_all()
    return render_template('list.html', todos=data)



if __name__ == "__main__": # to run server
    with app.app_context():
        db.create_all()

    app.run(debug=True)