from model.Users import db
from model.Users import Users as userDB

class User():
    
    def findAll(self):
        return userDB.query.all()

    def findOne(self,id):
        return userDB.query.get(id)

    def insertUser(self, info):
        user = userDB()
        user.name = info['name']
        user.email = info['email']
        user.username = info['username']
        user.telefone = info['telefone']
        user.password = info['password']
        user.admin = False
        db.session.add(user)
        return db.session.commit()

    
    def updateUser(self, id, info):
        user = userDB.query.get(id)
        print(user.id)
        user.name = info['name']
        user.email = info['email']
        user.username = info['username']
        user.telefone = info['telefone']
        user.password = info['password']
        user.admin = False
        return db.session.commit()


    def removeUser(self, id):
        user = userDB.query.get(id)
        db.session.delete(user)
        return db.session.commit()

    def loginUser(self, username, password):
        try:
            usuario = db.session.query(userDB).filter(userDB.username == username).first()
            if username == usuario.username and password == usuario.password:
                return usuario
            else:
                return None
        except Exception as e:
            return None
