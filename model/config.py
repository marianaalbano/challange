from flask import Flask


app = Flask(__name__,static_folder='../static', template_folder='../templates')

# CONFIG SQL
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True


# CONFIG MONGODB
app.config['MONGODB_SETTINGS'] = {"db":"elite"}