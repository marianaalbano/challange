from model.Users import db
from model.Users import QuestionsDisserty as Disserty

from controllers.Quiz import Quiz

class QuestionsDisserty():

    def findAll(self):
        return Disserty.query.all()

    def findOne(self,id):
        return Disserty.query.get(id)

    def insertQD(self, info):
        quiz = Quiz()
        quiz_id = quiz.findOne(info['quiz_id'])
        qd = Disserty()
        qd.questions = info['questions']
        qd.right_question = info['right_question']
        qd.quiz_id = quiz_id
        db.session.add(qd)
        return db.session.commit()

    
    def updateQD(self, id, info):
        qd = Disserty.query.get(id)
        qd.questions = info['questions']
        qd.right_question = info['right_question']
        return db.session.commit()


    def removeQD(self, id):
        qd = Disserty.query.get(id)
        db.session.delete(qd)
        return db.session.commit()