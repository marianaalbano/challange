from model import db
from model import User as userDB

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
        db.session.commit()
