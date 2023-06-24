#Standard imports
import datetime

#External Imports
from flask import Flask, render_template, request
# from flask_mail import Mail, Message

#Local Imports
from src.views import views
from src.config import config


def create_app():
    app = Flask(__name__, template_folder='dist')
    app.config.from_object(config)
    app.register_blueprint(views)
    # mail = Mail(app)

    @app.route('/')
    def three():
        return render_template('home.html')

    @app.route('/old')
    def old():
        return render_template('base.html')

    # @app.route('/process_email', methods=['POST'])
    # def process_email():
    #     msg = Message('Test', sender='testaccount@gmail.com', recipients=['your@email.com'])
    #     msg.body = 'This is a test email' #Customize based on user input
    #     mail.send(msg)
    #     return 'done'


    return app
