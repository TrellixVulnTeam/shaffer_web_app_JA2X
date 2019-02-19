# before running command "flask run" we need to create "export FLASK_APP=file.py" variable
# where file.py is the main flask file with the app's body. It will make it as in production
# meaning foe every change you will need to restart the server and when theapp is closed the 
# variable disapears too. To avoid that and make the work easier, we need to create the command
# "export FLASK_DEBUG=1" and thus have a dev environment so all the changes reflect with just page refresh
# from flask import Flask, render_template, url_for, flash, redirect
# from forms import RegistrationForm, LoginForm
# from flask_sqlalchemy import SQLAlchemy



# app = Flask(__name__)
# # needed for some cross site access security (I don't remember exact wording)
# app.config['SECRET_KEY'] = 'c96b95a020e5ff5189aaff83b2199aca'

# # creating connection between our app and a sqlite db. A file will be geenrated in the main dir
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
# # instantiating a db based on SQLAlchemy
# db = SQLAlchemy(app)

# from models import User, Post


# posts = [
#     {
#         'author': 'Corey Shaffer',
#         'title': 'Blog Post 1',
#         'content': 'first post content',
#         'date_posted': 'April 20, 2018'
#     },
#     {
#         'author': 'Mi Mioso',
#         'title': 'Blog Post 2',
#         'content': 'Second post content',
#         'date_posted': 'April 21, 2018' 
#     }
# ]

# @app.route("/")
# @app.route("/home")
# def home():
#     return render_template("home.html", posts=posts)

# @app.route("/about")
# def about():
#     return render_template("about.html", title="About")

# @app.route("/contact")
# def contact():
#     return render_template("contact.html", title="Contact")

# @app.route("/register", methods=['GET', 'POST'])
# def register():
#     form = RegistrationForm()
#     if form.validate_on_submit():
#         flash(f'Account created for {form.username.data}!', 'success')
#         return redirect(url_for('home'))
#     return render_template("register.html", title="Register", form=form)

# @app.route("/login", methods=['GET', 'POST'])
# def login():
#     form = LoginForm()
#     if form.validate_on_submit():
#         if form.email.data == "admin@blog.com" and form.password.data == "password":
#             flash("You have been logged in!", "success")
#             return redirect(url_for("home"))
#         else:
#             flash("Login unsuccesful. Please check username and password", "danger")
            
#     return render_template("login.html", title="Login", form=form)
from flaskblog import app
   
if __name__ == "__main__":
    app.run(debug=True)

