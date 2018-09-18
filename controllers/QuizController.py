from model.Users import db
#from model.Users import Users as usersDB
from model.Users import Quiz as quizDB
from Users import User

class QuizController():
    
    def findAll(self):
        return quizDB.query.all()

    def findOne(self, id):
        return quizDB.query.get(id)

    def findLastOne(self):
        return quizDB.query.order_by(quizDB.id.desc()).first()

      
    def insertQuiz(self, info):
        quiz = quizDB()
        quiz.name = info['name']
        quiz.response_time = info['time']
        quiz.category = info['type']
        quiz.dificulty = info['dificulty']
        db.session.add(quiz)
        return db.session.commit()

    
    def updateQuiz(self, id, info):
        quiz = quizDB.query.get(id)
        quiz.name = info['name']
        quiz.responsetime = info['time']
        quiz.dificulty = info['dificulty']
        return db.session.commit()


    def removeQuiz(self, id):
        quiz = quizDB.query.get(id)
        db.session.delete(quiz)
        return db.session.commit()

    def addUser(self,id_user, quizzes):
        user = User()
        user = user.findOne(int(id_user))
        
        for quiz in quizzes.keys():
            id_quiz = self.findOne(quizzes[quiz])
            u = user.quiz_users.append(id_quiz)
            db.session.commit()
        return 200
    

