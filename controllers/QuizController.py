from model.Users import db
from model.Users import Quiz as quizDB

class QuizController():
    
    def findAll(self):
        return quizDB.query.all()

    def findOne(self, id):
        return quizDB.query.get(id)

    def findLastOne(self):
        return db.session.query(quizDB).order_by(quizDB.id.desc()).first()

    def insertQuiz(self, info):
        quiz = quizDB()
        quiz.name = info['name']
        quiz.responsetime = info['response_time']
        quiz.category = info['category']
        quiz.dificulty = info['dificulty']
        db.session.add(quiz)
        return db.session.commit()

    
    def updateQuiz(self, id, info):
        quiz = quizDB.query.get(id)
        print(quiz.id)
        quiz.name = info['name']
        quiz.responsetime = info['response_time']
        quiz.dificulty = info['dificulty']
        return db.session.commit()


    def removeQuiz(self, id):
        quiz = quizDB.query.get(id)
        db.session.delete(quiz)
        return db.session.commit()

