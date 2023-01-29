# Standard Imports

# External Imports
from flask import Flask
#from flask_bootstrap import Bootstrap

# Local Imports
from app.extensions.views import create_views


class Factory:
    def create_app():
        app = Flask(__name__)
        #Bootstrap(app)        
        create_views(app)

        return app


    def run(app):
        app.run()