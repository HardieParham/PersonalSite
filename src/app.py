from flask import Flask, render_template

from src.views import views


def create_app():
    """Main Flask factory function. Will spin up an instance of the site.

    Returns:
        Flask: The running flask intance.
    """
    app = Flask(__name__, template_folder='dist')
    app.register_blueprint(views)

    #Main route used as the standard container for JQuery to append to
    @app.route('/')
    def main():
        return render_template('base.html')
    
    return app
