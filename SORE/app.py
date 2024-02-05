import random
from rdflib import Namespace, URIRef, Literal, Graph

from flask_cors import CORS
from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token
from werkzeug.security import check_password_hash, generate_password_hash
from db import db, execute_sparql_query
from datetime import timedelta

from BE.user.user_model import create_user, User
import BE.constants.constants as cst


app = Flask(__name__)
CORS(app)

bcrypt = Bcrypt(app)
app.config['JWT_SECRET_KEY'] = 'your-secret-key'
jwt = JWTManager(app)

@app.route('/register', methods=['POST'])
def register():
    email = request.json.get('email', None)
    password = request.json.get('password', None)
    status = request.json.get('status', None)
    gender = request.json.get('gender', None)
    age = request.json.get('age', None)
    education = request.json.get('education', None)
    country = request.json.get('country', None)
    user_collection = db.users
    existing_user = user_collection.find_one({'email': email})
    first_name = request.json.get('firstName', None)
    last_name = request.json.get('lastName', None)

    if existing_user:
        return jsonify({"msg": "Email already exists."}), 409

    hashed_password = generate_password_hash(password)
    user_collection.insert_one({'email': email,
                                'password_hash': hashed_password,
                                'first_name': first_name,
                                'last_name': last_name,
                                'status': status,
                                'gender': gender,
                                'age': age,
                                'education': education,
                                'country': country,
                                #'work': work,
                                })



    jokes_category = ['Programming', 'Misc', 'Pun', 'Spooky', 'Christmas']
    words_to_pick = 3
    health_interests = random.sample(cst.interests_dictionary['Health'],words_to_pick)
    news_interests = random.sample(cst.interests_dictionary['Gaming'],words_to_pick)
    work = random.choice(['IT', 'Engineering', 'Finance', 'Marketing', 'Sales', 'HR'])
    knows = ['user2@gmail.com', 'user3@gmail.com']
    file_path = './users_graph/'

    create_user(file_path, first_name, last_name, email, gender, status, news_interests,jokes_category, health_interests, country, work, education, age, knows)

    return jsonify({"msg": "User registered successfully."}), 201

@app.route('/profile', methods=['POST'])
def save_profile():
    category_jokes = request.json.get('categoryJokes', None)
    health_interests = request.json.get('healthInterests', None)
    news_interests = request.json.get('newsInterests', None)
    # create_user
    # update_profile_to_display()
    # TO DO save profile for REGISTER and LOGIN

@app.route('/login', methods=['POST'])
def login():
    email = request.json.get('email', None)
    password = request.json.get('password', None)

    user_collection = db.users
    user = user_collection.find_one({'email': email})

    if user and check_password_hash(user['password_hash'], password):
        expires = timedelta(minutes=1)
        access_token = create_access_token(identity=email,  expires_delta=expires)
        return jsonify({
            'access_token': access_token,
            'firstName': user['first_name'],
            'lastName': user['last_name'],
            'email': user['email']
        }), 200

        #User = User.get_user_from_db()
        #User = User.get_user_graph()

        #get_news(User.graph) -> can apass pe events
        #get_health(User.grapph) - > can apass pe lifestyle
        #get_jokes(User.graph) -> can apass pe jokes


    return jsonify({"msg": "Incorrect email or password."}), 401

@app.route('/homepage', methods=['GET'])
def get_homepage():
    return jsonify("Homepage")

@app.route('/people', methods=['GET'])
def get_people():
    return jsonify("People")

@app.route('/news', methods=['POST'])
def get_news():
    email = request.json.get('email', None)

    # de inlocuit cu cel din request
    email = 'john.doe@example.com'

    sparql_query = f"""
    PREFIX ns1: <http://visualdataweb.org/SoreOntology/>
    PREFIX ns2: <http://visualdataweb.org/SoreOntology/personOntology/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

    SELECT DISTINCT ?news ?title ?author ?description ?publishedAt ?urlToImage ?url
    WHERE {{
      ?person ns2:hasEmail "{email}" .
      ?user ns2:hasRecommendedItem ?news .
      ?news a ns1:News .
      ?news ns1:hasTitle ?title .
      OPTIONAL {{ ?news ns1:hasAuthor ?author . }}
      OPTIONAL {{ ?news ns1:hasDescription ?description . }}
      OPTIONAL {{ ?news ns1:hasDatePublished ?publishedAt . }}
      OPTIONAL {{ ?news ns1:hasImageURL ?urlToImage . }}
      OPTIONAL {{ ?news ns1:hasNewsUrl ?url . }}
    }}
    """

    results = execute_sparql_query(sparql_query)
    if results:
        news_items = results.get("results", {}).get("bindings", [])
        news = [{
            "title": item.get('title', {}).get('value', 'No Title Provided'),
            "author": item.get('author', {}).get('value', 'No Author Provided'),
            "description": item.get('description', {}).get('value', 'No Description Provided'),
            "urlToImage": item.get('urlToImage', {}).get('value', None),
            "publishedAt": item.get('publishedAt', {}).get('value', None),
            "url": item.get('url', {}).get('value', None)
        } for item in news_items]
        return jsonify(news)
    else:
        return jsonify({"error": "Could not retrieve news"}), 500

@app.route('/health', methods=['POST'])
def get_health():
    #return jsonify("Health")

    email = request.json.get('email', None)

    # de inlocuit cu cel din request
    email = 'john.doe@example.com'

    sparql_query = f"""
    PREFIX ns1: <http://visualdataweb.org/SoreOntology/>
    PREFIX ns2: <http://visualdataweb.org/SoreOntology/personOntology/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    
    SELECT DISTINCT ?medicalNews ?title ?author ?description ?hasMedicalUrl
    WHERE {{
      ?person ns2:hasEmail "{email}" .
      ?user ns2:hasRecommendedItem ?medicalNews .
      ?medicalNews a ns1:Medical_and_Lifestyle .
      ?medicalNews ns1:hasTitle ?title .
      OPTIONAL {{ ?medicalNews ns1:hasAuthor ?author . }}
      OPTIONAL {{ ?medicalNews ns1:hasDescription ?description . }}
      OPTIONAL {{ ?medicalNews ns1:hasMedicalUrl ?url . }}
    }}
    """

    results = execute_sparql_query(sparql_query)
    if results:
        health_items = results.get("results", {}).get("bindings", [])
        health = [{
            "title": item.get('title', {}).get('value', 'No Title Provided'),
            "author": item.get('author', {}).get('value', 'No Author Provided'),
            "description": item.get('description', {}).get('value', 'No Description Provided'),
            "hasMedicalUrl": item.get('hasMedicalUrl', {}).get('value', None)
        } for item in health_items]
        return jsonify(health)
    else:
        return jsonify({"error": "Could not retrieve news"}), 500

@app.route('/humor', methods=['POST'])
def get_humor():
    #return jsonify("Humor")
    email = request.json.get('email', None)

    # de inlocuit cu cel din request
    email = 'john.doe@example.com'

    sparql_query = f"""
    PREFIX ns1: <http://visualdataweb.org/SoreOntology/>
    PREFIX ns2: <http://visualdataweb.org/SoreOntology/personOntology/>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
    
    SELECT DISTINCT ?joke ?category ?delivery ?setup ?hasTopic ?isSafe ?type
    WHERE {{
        ?user ns2:hasJoke ?joke .
        ?joke ns1:category ?category ;
        ns1:delivery ?delivery ;
        ns1:setup ?setup ;
        ns1:hasTopic ?hasTopic ;
        ns1:isSafe ?isSafe ;
        ns1:type ?type .
    }}
    """

    results = execute_sparql_query(sparql_query)
    if results:
        joke_items = results.get("results", {}).get("bindings", [])
        jokes = [{
            "category": item.get('category', {}).get('value', 'No Category Provided'),
            "delivery": item.get('delivery', {}).get('value', 'No Delivery Provided'),
            "setup": item.get('setup', {}).get('value', 'No Setup Provided'),
            "hasTopic": item.get('hasTopic', {}).get('value', None),
            "isSafe": item.get('isSafe', {}).get('value', None),
            "type": item.get('type', {}).get('value', None)
        } for item in joke_items]
        return jsonify(jokes)
    else:
        return jsonify({"error": "Could not retrieve news"}), 500

@app.route('/profile', methods=['GET'])
def get_profile():
    return jsonify("Profile")

if __name__ == '__main__':
    app.run()
