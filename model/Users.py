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



quiz_users = db.Table('quiz_users',
    db.Column('users_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('quiz_id', db.Integer, db.ForeignKey('quiz.id'), primary_key=True)
)

class Users(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False, unique=True)
    username = db.Column(db.String, nullable=False, unique=True)
    telefone = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    admin = db.Column(db.Boolean, nullable=False)
    quiz_users = db.relationship('Quiz', secondary=quiz_users, lazy='subquery', backref=db.backref('users', lazy=True))


    def is_active(self):
        return self.is_active()

    def get_id(self):
        return self.id

    def is_authenticated(self):
        return True

    def is_anonymous(self):
        return False

    def is_admin(self):
        return self.admin


class Quiz(db.Model):
    __tablename__ = 'quiz'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    response_time = db.Column(db.String, nullable=False)
    category = db.Column(db.String, nullable=False)
    dificulty = db.Column(db.String, nullable=False)
    questions_multiple = db.relationship('QuestionsMultiple', backref='quiz', lazy=True)
    questions_disserty = db.relationship('QuestionsDisserty', backref='quiz', lazy=True)


class QuestionsMultiple(db.Model):
    __tablename__ = 'questions_multiple'

    id = db.Column(db.Integer, primary_key=True)

    question = db.Column(db.String, nullable=False)
    option_1 = db.Column(db.String, nullable=False)
    option_2 = db.Column(db.String, nullable=False)
    option_3 = db.Column(db.String, nullable=False)
    option_4 = db.Column(db.String, nullable=False)

    right_question = db.Column(db.String, nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)

class QuestionsDisserty(db.Model):
    __tablename__ = 'questions'

    id = db.Column(db.Integer, primary_key=True)
    questions = db.Column(db.String, nullable=False)
    right_question = db.Column(db.String, nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)


if __name__ == '__main__':
    manager.run()