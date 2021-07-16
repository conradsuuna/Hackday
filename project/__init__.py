from flask import Flask, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
# from project.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'
mail = Mail()
# migrate = Migrate(db)


def create_app():
    app = Flask(__name__, instance_relative_config=False, static_url_path='/static')
    app.config.from_object('config.Config')


    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)
    Migrate(app, db)

    # Imports
    from .models import User

    # to keep track of loggedin user
    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)

    # redirect unauthaurised users here
    @login_manager.unauthorized_handler
    def unauthorized_callback():
        return redirect('/')


    with app.app_context():
        from project.users.routes import users
        from project.bplans.routes import bplans
        from project.main.routes import main
        app.register_blueprint(users)
        app.register_blueprint(bplans)
        app.register_blueprint(main)

        return app