from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

#Create the App
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/post')
def post():
    return render_template('post.html')

if __name__ == '__main__':
    app.run(debug=True)

    