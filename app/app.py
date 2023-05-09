#Standard imports
import datetime

#External Imports
from flask import Flask, render_template, request
from flask_mail import Mail, Message

#Local Imports
from app.views import views


def create_app():
    # mail = Mail()
    app = Flask(__name__)
    app.config['MAIL_DEFAULT_SENDER'] = 'hparham@smu.edu'
    app.register_blueprint(views)
    mail=Mail(app)
    # mail.init_app(app)

    @app.route('/')
    def base():
        return render_template('base.html')
    

    @app.route('/email', methods=['POST'])
    def email():
        sender_name = request.form.get('name')
        subject = request.form.get('subject')
        sender_email = request.form.get('email')
        content = request.form.get('content')

        msg = Message(
            subject=f'{sender_name}: {subject}',
            recipients=['hparham865@gmail.com'],
            body=f'{sender_name}: {sender_email}: {content}',
            date=datetime.datetime.now(),
            )
        
        mail.send(msg)

        return '<h1>Thanks!</h1>'
    
    return app
