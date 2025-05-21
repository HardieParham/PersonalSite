from flask import Flask, render_template, send_from_directory, send_file

from src.views import views
from src.dynamics import return_dynamics_results


def create_app():
    """Main Flask factory function. Will spin up an instance of the site. Use with Waitress.

    Returns:
        Flask: The running flask intance.
    """
    app = Flask(__name__, template_folder='dist')
    app.register_blueprint(views)

    # Main route used as the standard container for JQuery to append to
    @app.route('/')
    def main():
        print("Rendering Base Page.")
        return render_template('base.html')
    
    # Seconday route to show my personal resume in the browser
    @app.route('/resume')
    def view_resume():
        path = "files/Hardie Parham Resume 2024 V3.pdf"
        print("Viewing Resume.")
        return send_from_directory('static', path)
    
    # Seconday route to download my personal resume as an attachment
    @app.route('/sendresume')
    def send_resume():
        path = "static/files/Hardie Parham Resume 2024 V3.pdf"
        print("Sending Resume File.")
        return send_file(path, as_attachment=True)
    
    # Route for "Page not found"
    @app.errorhandler(404) 
    def not_found(e):
        print("Rendering 404 Page.")
        return render_template("404.html") 
    
    # Route for my dynamics hmwk
    @app.route('/dynamics')
    def dynamics():
        print("Rendering Dynamics Page.")
        results = return_dynamics_results()
        return render_template('dynamics.html', data=results)

    print("App created.")
    return app
