from flask_cors import CORS
from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token
from werkzeug.security import check_password_hash, generate_password_hash
from db import db

app = Flask(__name__)
CORS(app)

bcrypt = Bcrypt(app)
app.config['JWT_SECRET_KEY'] = 'your-secret-key'
jwt = JWTManager(app)

@app.route('/register', methods=['POST'])
def register():
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    user_collection = db.users
    existing_user = user_collection.find_one({'email': email})

    if existing_user:
        return jsonify({"msg": "Email already exists."}), 409

    hashed_password = generate_password_hash(password)
    user_collection.insert_one({'email': email, 'password_hash': hashed_password})
    return jsonify({"msg": "User registered successfully."}), 201

@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    user_collection = db.users
    user = user_collection.find_one({'email': email})

    if user and check_password_hash(user['password_hash'], password):
        access_token = create_access_token(identity=email)
        return jsonify(access_token=access_token), 200

    return jsonify({"msg": "Incorrect email or password."}), 401

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

@app.route('/profile', methods=['GET'])
def get_profile():
    return jsonify("Profile")

# if __name__ == '__main__':
#     app.run()
