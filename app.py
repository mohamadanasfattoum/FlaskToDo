from flask import Flask, render_template, request, redirect

app = Flask(__name__)




# views
@app.route('/') # url
def welcome():
    return jsonify({'Message':'Welcome'})




if __name__ == "__main__":
    # with app.app_context():
    #     db.create_all()

    app.run(debug=True)