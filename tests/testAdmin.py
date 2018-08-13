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

    def login(self, user, password):
        return self.app.post("/login", data=dict(username=user,password=password))

    # def test_edit_admin(self):
    #     response = self.app.get("/admin/1")
    #     self.assertEqual(response.status_code, 200)

    def test_login_admin(self):
        response = self.login('admin', 'admin')
        self.assertEqual(response.status_code, 200)

    def test_login_user(self):
        response = self.login('user', 'user')
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