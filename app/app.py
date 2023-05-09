from flask import Flask, render_template


from app.views import views


def create_app():
    app = Flask(__name__)
    app.register_blueprint(views)

    @app.route('/')
    def base():
        return render_template('base.html')
    
    return app
