from flask_mongoengine import MongoEngine
from datetime import datetime

from config import app

db = MongoEngine(app)

class UserResponse(db.Document):
    name = db.StringField()
    id_user = db.StringField()
    id_quiz = db.StringField()
    questions = db.ListField()
    date = db.DateTimeField(default=datetime.now())


