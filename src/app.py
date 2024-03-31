from flask import Flask, render_template, send_from_directory

from src.views import views


def create_app():
    """Main Flask factory function. Will spin up an instance of the site.

    Returns:
        Flask: The running flask intance.
    """
    app = Flask(__name__, template_folder='dist')
    app.register_blueprint(views)

    # Main route used as the standard container for JQuery to append to
    @app.route('/')
    def main():
        return render_template('base.html')
    
    # Seconday route to show my personal resume in the browser
    @app.route('/resume')
    def send_resume():
        path = "files/2024HardieParhamResumeV3.pdf"
        return send_from_directory('static', path)
    
    return app
