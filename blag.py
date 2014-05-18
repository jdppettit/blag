from flask import *
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.mail import *

app = Flask(__name__)

@app.route('/')
def index():
	return "Hi, i'm a blag"

if __name__ == '__main__':
	app.run(debug=True,host='0.0.0.0')
