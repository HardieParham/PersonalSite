#Standard imports
import datetime

#External Imports
from flask import Flask, render_template, request

#Local Imports
from src.views import views
from src.config import config


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    app.register_blueprint(views)


    @app.route('/')
    def base():
        return render_template('base.html')

    
    return app
