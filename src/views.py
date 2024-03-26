from flask import Blueprint, jsonify, render_template, request


views = Blueprint('views', __name__, template_folder='templates')

#Routes for JQuery to fetch for each 'page'
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
