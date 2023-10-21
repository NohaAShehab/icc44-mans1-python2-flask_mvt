# import flask
# load configuration

from flask import Flask

# get db object
from app.models import  db

from app.config import projectConfig as AppConfig

def create_app(config_name='dev'):
    app = Flask(__name__)
    current_config = AppConfig[config_name]   # config class
    app.config['SQLALCHEMY_DATABASE_URI']=current_config.SQLALCHEMY_DATABASE_URI
    # search in the class about class variable with the given name
    app.config['SQLALCHEMY_DATABASE_URI'] = current_config
    app.config.from_object(current_config)



    ## register blueprint in the application
    from app.students import student_blueprint
    app.register_blueprint(student_blueprint)


    return app
