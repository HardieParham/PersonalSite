from flask import Flask, render_template, request

from src.views import views


def create_app():

    """Main Flask factory function. Will spin up an instance of the site.

    Returns:
        Flask: The running flask intance.
    """
    
    app = Flask(__name__, template_folder='dist')
    app.register_blueprint(views)

    # @app.route('/commands')
    # def commands():
    #     return render_template('commands.html')

    @app.route('/')
    def home():
        return render_template('base.html')
    
    return app
