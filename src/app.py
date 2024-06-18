from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://minornote_dev:Dagger01!@localhost:5432/minornote'

db = SQLAlchemy(app)

@app.route("/")
def index():
    return "Hello World!"
