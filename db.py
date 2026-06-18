import click
from flask_sqlalchemy import SQLAlchemy  # (1.)
from sqlalchemy import orm
from app import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Pflegehilfe.db'  # (2.)

db = SQLAlchemy()  # (3.)
db.init_app(app)  # (4.)