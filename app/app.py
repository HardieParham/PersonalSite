#Standard imports
import datetime

#External Imports
from flask import Flask, render_template, request
from flask_mailman import Mail, EmailMessage

#Local Imports
from app.views import views
from app.config import config


def create_app():
    # mail = Mail()
    app = Flask(__name__)
    app.config.from_object(config)
    app.config['MAIL_DEFAULT_SENDER'] = 'hparham@smu.edu'
    app.register_blueprint(views)
    mail=Mail(app)


    @app.route('/')
    def base():
        return render_template('base.html')
    

    @app.route('/email', methods=['POST'])
    def email():
        with mail.get_connection() as conn:
            email = EmailMessage(
                subject=request.form.get('subject'),
                body='',
                from_email='hparham865@gmail.com',
                to='hparham865@gmail.com',
                connection=conn
            )
            try:
                email.send()
            except:
                return '<h1>This failed bro</h1>'

        return '<h1>Thanks!</h1>'
    
    return app
