from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)
# needed for some cross site access security (I don't remember exact wording)
app.config['SECRET_KEY'] = 'c96b95a020e5ff5189aaff83b2199aca'

# creating connection between our app and a sqlite db. A file will be geenrated in the main dir
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# instantiating a db based on SQLAlchemy
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
login_manager = LoginManager(app)


from flaskblog import routes


