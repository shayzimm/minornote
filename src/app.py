from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://minornote_dev:Dagger01!@localhost:5432/minornote'

db = SQLAlchemy(app)

class User(db.Model):
    """
    User model for the application.

    Attributes:
        id (db.Column(db.Integer, primary_key=True)): The unique identifier for the user.
        username (db.Column(db.String(80), unique=True, nullable=False)): The username of the user.
        email (db.Column(db.String(120), unique=True, nullable=False)): The email address of the user.
        password_hash (db.Column(db.String(128), nullable=False)): The hashed password of the user.
        first_name (db.Column(db.String(50))): The first name of the user.
        last_name (db.Column(db.String(50))): The last name of the user.
        is_admin (db.Column(db.Boolean, default=False)): A boolean indicating whether the user is an admin.

    Methods:
        __init__(self, username: str, email: str, password_hash: str, first_name: str, last_name: str, is_admin: bool): Initializes a new User object.
    """
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    first_name = db.Column(db.String(50))
    last_name = db.Column(db.String(50))
    is_admin = db.Column(db.Boolean, default=False)

@app.cli.command('db_create')
def db_create():
    db.drop_all()
    db.create_all()
    print('Created tables')

    user = User(username='testuser', email='testemail@test.com', password_hash='testpassword', first_name='testuserfirst', last_name='testuserlast', is_admin=True)

    db.session.add(user)
    db.session.commit()
    
@app.route("/")
def index():
    return "Hello World!"
