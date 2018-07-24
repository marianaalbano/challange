#!/usr/bin/python
# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand

from datetime import datetime
import os

# POSTGRES_USER = os.environ["POSTGRES_USER"]
# POSTGRES_PW = os.environ["POSTGRES_PW"]
# POSTGRES_URL = os.environ["POSTGRES_URL"]
# POSTGRES_DB = os.environ["POSTGRES_DB"]

# DB_URL = 'postgresql+psycopg2://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB)


app = Flask(__name__,static_folder='../static', template_folder='../templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app, session_options={"autoflush": False})


migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)


class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    username = db.Column(db.String, nullable=False)
    telefone = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    is_admin = db.Column(db.String, nullable=False)


if __name__ == '__main__':
    manager.run()
