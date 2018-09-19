from model.Users import db
from model.Users import Users as userDB

from model.Users import Quiz

from model.Users import quiz_users

class User():
    
    def findAll(self):
        return userDB.query.all()

    def findOne(self,id):
        return userDB.query.get(id)

    def findUserQuiz(self, id):
        return Quiz.query.filter(Quiz.users.any(id=id)).all()

    def insertUser(self, info):
        try:
            user = userDB()
            user.name = info['name']
            user.email = info['email']
            user.username = info['username']
            user.telefone = info['telefone']
            user.password = info['password']
            user.admin = info["gridRadios"]
            if user.admin == "option1":
                user.admin = False
            else:
                user.admin = True

            db.session.add(user)
            db.session.commit()
            return 200
        except Exception as e:
            return 403

    
    def updateUser(self, id, info):
        try:
            user = userDB.query.get(id)
            user.name = info['name']
            user.email = info['email']
            user.username = info['username']
            user.telefone = info['telefone']
            user.password = info['password']
            admin = info['gridRadios']
            if admin == "option1":
                user.admin = False
            else:
                user.admin = True
            db.session.commit()
            return 200
        except Exception as e:
            return 403


    def removeUser(self, id):
        try:
            user = userDB.query.get(id)
            db.session.delete(user)
            db.session.commit()
            return 200
        except Exception as e:
            return 403
            
    def loginUser(self, username, password):
        try:
            usuario = db.session.query(userDB).filter(userDB.username == username).first()
            if username == usuario.username and password == usuario.password:
                return usuario
            else:
                return None
        except Exception as e:
            return None
