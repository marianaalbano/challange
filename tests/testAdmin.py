import unittest
import os


from flask_login import login_user
# some_file.py
import sys
sys.path.insert(0, os.getcwd())

from app import app
from model.Users import db


from controllers.Users import User


class TestAdmin(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join(os.getcwd() + "/model/app.db")
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

        self.assertEqual(app.debug, False)


    ### TEST INSERT / UPDATE ###

    def login(self, user, password):
        try:
            user = User()
            user = user.loginUser(user,password)
            if user.admin == True:
                login_user(user, remember=False)
                return 200
            elif user.admin == False:
                login_user(user, remember=False)
                return 200
        except Exception as e:
            return 403

        #return self.app.post("/login", data=dict(username=user,password=password))

    # def test_login_admin(self):
    #     response = self.login('admin_teste', 'admin-teste')
    #     self.assertEqual(response, 200)

    # def test_login_user(self):
    #     response = self.login('admin_teste', 'admin-teste')
    #     self.assertEqual(response, 200)

    def add_user(self, info):
        user = User()
        user = user.insertUser(info)
        return user

    def test_add_admin(self):
        info = {"name": "admin teste",
                "email": "admin@teste.com.br",
                "username":"admin_teste",
                "telefone":"11111112",
                "password":"admin-teste",
                "gridRadios":"option2"}
        response = self.add_user(info)
        self.assertEqual(response, 200)

    def test_add_user(self):
        info = {"name": "admin teste",
                "email": "admin@teste.com.br",
                "username":"admin_teste",
                "telefone":"11111112",
                "password":"admin-teste",
                "gridRadios":"option1"}
        response = self.add_user(info)
        self.assertEqual(response, 200)


    def test_search_user(self):
        user = User()

        




    ### TEST LIST / GET ### 

    def test_edit_admin(self):
        response = self.app.get("/admin/1", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
 
    def test_page_login(self):
        response = self.app.get('/login', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn("login-page", response.data)



if __name__ == '__main__':
    unittest.main()