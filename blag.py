from flask import *
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.mail import *

app = Flask(__name__)

@app.route('/')
def index():
	return render_template("index.html") 

@app.route('/blog')
def blog():
	return render_template("blog.html")

@app.route('/about')
def about():
	return render_template("about.html")

@app.route('/resume')
def resume():
	return render_template("resume.html")

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0',port=5222)
