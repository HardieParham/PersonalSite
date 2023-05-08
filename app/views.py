from flask import Blueprint, jsonify, render_template


views = Blueprint('views', __name__, template_folder='templates')


#A route for AJAX to fetch for each 'page'
@views.route('/overview')
def overview():
    return render_template('overview.html')

@views.route('/personal')
def personal():
    return render_template('personal.html')

@views.route('/programming')
def programming():
    return render_template('programming.html')

@views.route('/work')
def work():
    return render_template('work.html')

@views.route('/contact')
def contact():
    return render_template('contact.html')