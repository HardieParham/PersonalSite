from flask import Blueprint, jsonify, render_template


simple_page = Blueprint('simple_page', __name__, template_folder='templates')


#Create one of these for each 'page'
@simple_page.route('/hobbies')
def hobbies():
    # data = {
    #     'block': 'test'

    # }

    # return jsonify(data)
    return render_template('test.html')