from model.Users import db
from model.Users import QuestionsMultiple as Multiple

from QuizController import QuizController

class QuestionsMultiple():

    def findAll(self):
        return Multiple.query.all()

    def findOne(self,id):
        return Multiple.query.get(id)

    def findByQuiz(self,id):
        return Multiple.query.filter_by(id_quiz=id).all()

    def insertQM(self, id, info):
        quiz = QuizController()
        quiz_id = quiz.findOne(id)
        qm = Multiple()
        qm.option_1 = info['option_1']
        qm.option_2 = info['option_2']
        qm.option_3 = info['option_3']
        qm.option_4 = info['option_4']
        qm.right_question = info['right_question']
        qm.quiz_id = quiz_id
        db.session.add(qm)
        return db.session.commit()

    
    def updateQM(self, id, info):
        qm = Multiple.query.get(id)
        qm.questions = info['questions']
        qm.right_question = info['right_question']
        return db.session.commit()


    def removeQM(self, id):
        qm = Multiple.query.get(id)
        db.session.delete(qm)
        return db.session.commit()