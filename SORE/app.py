from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/homepage', methods=['GET'])
def get_homepage():
    return jsonify("Homepage")

@app.route('/news', methods=['GET'])
def get_news():
    return jsonify("News")

@app.route('/events', methods=['GET'])
def get_events():
    return jsonify("Events")

@app.route('/music', methods=['GET'])
def get_music():
    return jsonify("Music")

@app.route('/movies', methods=['GET'])
def get_movies():
    return jsonify("Movies")

@app.route('/health', methods=['GET'])
def get_health():
    return jsonify("Health")

@app.route('/technology', methods=['GET'])
def get_technology():
    return jsonify("Technology")

@app.route('/lifestyle', methods=['GET'])
def get_lifestyle():
    return jsonify("Lifestyle")

@app.route('/humor', methods=['GET'])
def get_humor():
    return jsonify("Humor")

@app.route('/education', methods=['GET'])
def get_education():
    return jsonify("Education")

# if __name__ == '__main__':
#     app.run()
