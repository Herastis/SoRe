from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/homepage', methods=['GET'])
def getHomepage():
    return jsonify("Homepage")

# if __name__ == '__main__':
#     app.run()
