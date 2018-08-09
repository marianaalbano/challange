import unittest
import os

# some_file.py
import sys
sys.path.insert(0, '/Users/hfujie/elite/')

from app import app
from model.Users import db

class TestAdmin(unittest.TestCase):
    
    # def setUp(self):
    #     teste_app = app.test_client()
    #     self.response = teste_app.get('/login')

    
    # def test_get(self):
    #     print(self.response)
    #     self.assertEqual(200, self.response.status_code)

    # # Testamos se a nossa home retorna a string "ok"
    # #def test_html_string_response(self):
    # #    self.assertEqual("ok", self.response.data.decode('utf-8'))

    # # Testamos se o content_type da resposta da home esta correto
    # def test_content_type(self):
    #     self.assertIn('text/html', self.response.content_type)
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False
        app.config['DEBUG'] = False
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
            os.path.join("/Users/hfujie/elite/model/app.db")
        self.app = app.test_client()
        db.drop_all()
        db.create_all()

        # Disable sending emails during unit testing
        #mail.init_app(app)
        self.assertEqual(app.debug, False)

    def login(self, user, password):
        return self.app.post("/login", data=dict(username=user,password=password))

    def test_edit_admin(self):
        response = self.app.get("/admin/1")
        self.assertEqual(response.status_code, 200)

    def test_login_admin(self):
        response = self.login('admin', 'admin')
        self.assertEqual(response.status_code, 200)

    def test_login_user(self):
        response = self.login('user', 'user')
        self.assertEqual(response.status_code, 200)

    # executed after each test
    def tearDown(self):
        pass
 
 
###############
#### tests ####
###############
 
    def test_page_login(self):
        response = self.app.get('/login', follow_redirects=True)
        self.assertEqual(response.status_code, 200)
        self.assertIn("login-page", response.data)



if __name__ == '__main__':
    unittest.main()