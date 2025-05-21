from flask import Blueprint, jsonify, render_template, request


views = Blueprint('views', __name__, template_folder='templates')

#Routes for JQuery to fetch for each 'page'
@views.route('/home')
def home():
    print("Rendering Home Page.")
    return render_template('home.html')

@views.route('/personal')
def personal():
    print("Rendering Personal Page.")
    return render_template('personal.html')

@views.route('/work')
def work():
    print("Rendering Work Page.")
    return render_template('work.html')

@views.route('/programming')
def programming():
    print("Rendering Programming Page.")
    return render_template('programming.html')

@views.route('/contact')
def contact():
    print("Rendering Contact Page.")
    return render_template('contact.html')

@views.route('/test')
def test_page():
    print("Rendering Test Page.")
    return render_template('test.html')
