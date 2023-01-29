# Standard Imports

# External Imports
from flask import render_template

# Local Imports

def create_views(app):
    @app.route('/')
    def home():
        return render_template('base.html')


    @app.route('/personal')
    def personal():
        pass


    @app.route('/work')
    def work():
        pass


    @app.route('/hobbies')
    def hobbies():
        pass


    @app.route('/<id>')
    def card(id):
        pass