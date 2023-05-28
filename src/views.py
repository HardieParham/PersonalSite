import datetime

from flask import Blueprint, jsonify, render_template, request


views = Blueprint('views', __name__, template_folder='templates')

# A route for AJAX to fetch for each 'page'
@views.route('/home')
def home():
    return render_template('home.html')

@views.route('/personal')
def personal():
    return render_template('personal.html')

@views.route('/work')
def work():
    return render_template('work.html')

@views.route('/programming')
def programming():
    return render_template('programming.html')

@views.route('/contact')
def contact():
    return render_template('contact.html')

# @views.route('/email', methods=['POST'])
# def email():
#     sender_name = request.form.get('name')
#     subject = request.form.get('subject')
#     sender_email = request.form.get('email')
#     content = request.form.get('content')

#     msg = Message(
#         subject=f'{sender_name}: {subject}',
#         recipients=['hparham865@gmail.com'],
#         body=f'{sender_name}: {content}',
#         sender=sender_email,
#         date=datetime.datetime.now(),
#         )
#     # mail.send(msg)

#     return '<h1>Thanks!</h1>'
