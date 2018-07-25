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
        user.passowrd = info['password']
        user.admin = False
        db.session.add(user)
        return db.session.commit()


    def removeUser(self, id):
        user = userDB.query.get(id)
        db.session.delete(user)
        return db.session.commit()

    def loginUser(self, username, password):
        try:
            usuario = db.session.query(userDB).filter(userDB.username == username).first()
            print (username, usuario.username)
            if username == usuario.username and password == usuario.password:
                print ("if ok")
                print(usuario)
                return usuario
            else:
                return None
        except Exception as e:
            print e
            return None
