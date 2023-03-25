from flask import Flask, render_template, jsonify, request, url_for





app = Flask(__name__)


@app.route('/')
def home():
    return render_template('home.html')
    

@app.route('/hobbies', methods=['GET'])
def hobbies():
    if request.method == 'GET':
        image_route='../static/images/'
        data = {
            "card-heading": "Test-Heading",
            "card-image": f"{image_route}what.png",
            "card-description": "Test description",
        }
        return jsonify(data)












































@app.route('/card', methods=['GET'])
def card():
    if request.method == 'GET':
        image_route='../static/images/'
        data = {
            "card-heading": "Test-Heading",
            "card-image": f"{image_route}what.png",
            "card-description": "Test description",
        }
        return jsonify(data)
    

@app.route('/card', methods=['GET', 'POST'])
def card_routing():
    if request.method == 'GET':
        pass

    if request.method == 'POST':
        pass










image_route='../static/images/'
card_list=[]
card_count=0

class Card():
    def __init__(self):
        self.id = 0
        self.heading = ''
        self.image = ''
        self.description = ''

    def set_all(self, heading, image, description, id):
        self.id = id
        self.heading = heading
        self.image = image_route + image
        self.description = description

    def get_all(self):
        data = {
            'id': self.id,
            'heading': self.heading,
            'image': self.image,
            'description': self.description
        }
        return data


    def set_id(self, id):
        self.id = id

    def get_id(self):
        return self.id

    def set_heading(self, heading):
        self.heading = heading

    def get_heading(self):
        return self.heading

    def set_image(self, image):
        self.image = image

    def get_image(self):
        return self.image

    def set_description(self, description):
        self.description = description

    def get_description(self):
        return self.description
