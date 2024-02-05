from flask import Flask, render_template, request

from src.views import views


def create_app():
    app = Flask(__name__, template_folder='dist')
    app.register_blueprint(views)

    @app.route('/commands')
    def commands():
        return render_template('commands.html')

    @app.route('/')
    def old():
        return render_template('base.html')
    
    return app
