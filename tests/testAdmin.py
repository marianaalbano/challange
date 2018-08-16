import unittest
import os

# some_file.py
import sys
sys.path.insert(0, os.getcwd())

from app import app
from model.Users import db

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
        return self.app.post("/login", data=dict(username=user,password=password))

    def test_login_admin(self):
        response = self.login('admin', 'admin')
        self.assertEqual(response.status_code, 200)

    def test_login_user(self):
        response = self.login('user', 'user')
        self.assertEqual(response.status_code, 200)

    def add_user(self, info):
        return self.app.post("/admin/user/new", data=dict(name=info["name"],
                                                          email=info["email"],
                                                          username=info["username"],
                                                          telefone=info["telefone"],
                                                          password=info["password"],
                                                          admin=info["admin"]), 
                                                follow_redirects=True)

    def test_add_admin(self):
        info = {"name": "admin teste",
                "email": "admin@teste.com.br",
                "username":"admin_teste",
                "telefone":"11111112",
                "password":"admin-teste",
                "admin":True}
        response = self.add_user(info)
        self.assertEqual(response.status_code, 200)

    def test_add_user(self):
        info = {"name": "admin teste",
                "email": "admin@teste.com.br",
                "username":"admin_teste",
                "telefone":"11111112",
                "password":"admin-teste",
                "admin":False}
        response = self.add_user(info)
        self.assertEqual(response.status_code, 200)


    def add_quiz(self, info):
        return self.app.post("/admin/quiz/new", data=dict(name=info["name"],
                                                          response_time=info["response_time"],
                                                          category=info["category"],
                                                          dificulty=info["dificulty"]),
                                                follow_redirects=True)

    def test_add_quiz(self):
        response = self.login('admin', 'admin')
        info = {"name": "quiz teste",
                "response_time": "00:10:00",
                "category":"Python",
                "dificulty":"Junior"}
        response = self.add_quiz(info)
        print (response.data)
        self.assertEqual(response.status_code, 200)




    ### TEST LIST / GET ### 

    def test_edit_admin(self):
        response = self.app.get("/admin/1", follow_redirects=True)
        self.assertEqual(response.status_code, 200)
 
    def test_page_login(self):
        response = self.app.get('/login', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn("login-page", response.data)

    def teste_admin_main(self):
        response = self.app.get('/admin/main', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn("login-page", response.data)

    def teste_admin_user(self):
        response = self.app.get('/admin/user', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn("login-page", response.data)

    def teste_admin_user_new(self):
        response = self.app.get('/admin/user/new', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn("login-page", response.data)

if __name__ == '__main__':
    unittest.main()