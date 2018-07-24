from model.Users import db
from model.Users import Users as userDB

class User():
    
    def findAll(self):
        return userDB.query.all()

    def findOne(self,id):
        return userDB.query.get(id)

    def insertUser(self, info):
        user = userDB
        user.name = info['name']
        user.email = info['email']
        user.username = info['username']
        user.telefone = info['telefone']
        user.passowrd = info['password']
        user.is_admin = False
        db.session.add(user)
        return db.session.commit()


    def removeUser(self, id):
        user = userDB.query.get(id)
        db.session.delete(user)
        return db.session.commit()
