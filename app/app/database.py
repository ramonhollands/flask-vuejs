from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relationship, relation
from sqlalchemy import create_engine, Integer, ForeignKey, String, Column
from sqlalchemy import DateTime
from sqlalchemy_utils import database_exists, create_database
from flask_user import login_required, UserManager, UserMixin
import datetime, os

db_url = 'postgresql+psycopg2://'+ os.getenv('db_user') + ':' + os.getenv('db_password') + '@mydb:5432/' + os.getenv('db_name')
print(db_url, flush=True)
app = Flask(__name__)

# Check and create db if necessary
engine = create_engine(db_url)
if not database_exists(engine.url):
    create_database(engine.url)

def get_setting(setting, settings):
    if setting in settings.keys():
        return settings[setting]
    else:
        return None


app.config['SQLALCHEMY_DATABASE_URI'] = db_url

app.config['SECRET_KEY'] = os.getenv('secret_key')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['USER_APP_NAME'] = "Box21"

if os.getenv('mail_server', False) is not False:
    app.config['MAX_CONTENT_LENGTH'] = 120 * 1024 * 1024
    app.config['MAIL_SERVER'] = os.getenv('mail_server')
    app.config['MAIL_PORT'] = 465
    app.config['MAIL_USE_SSL'] = True
    app.config['MAIL_USE_TLS'] = False
    app.config['MAIL_USERNAME'] = os.getenv('mail_username')
    app.config['MAIL_PASSWORD'] = os.getenv('mail_password')
    app.config['MAIL_DEFAULT_SENDER'] = os.getenv('mail_default_sender')
    app.config['USER_EMAIL_SENDER_EMAIL'] = os.getenv('mail_email_sender')
    app.config['USER_EMAIL_SENDER_NAME'] = os.getenv('mail_email_sender_name')
    app.config['USER_ENABLE_EMAIL'] = True
else:
    app.config['USER_ENABLE_EMAIL'] = False

app.config['USER_ENABLE_REGISTER'] = False
app.config['USER_ENABLE_USERNAME'] = False

db = SQLAlchemy(app)

# Define User data-model
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)

    # User Authentication fields
    email = db.Column(db.String(255), nullable=False, unique=True)
    email_confirmed_at = db.Column(db.DateTime())
    username = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(255), nullable=False)

    # User fields
    active = db.Column(db.Boolean()),
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)

    # Relationships
    roles = db.relationship('Role', secondary='user_roles')


# Define the Role data-model
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), unique=True)


# Define the UserRoles association table
class UserRoles(db.Model):
    __tablename__ = 'user_roles'
    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.Integer(), db.ForeignKey('users.id', ondelete='CASCADE'))
    role_id = db.Column(db.Integer(), db.ForeignKey('roles.id', ondelete='CASCADE'))

