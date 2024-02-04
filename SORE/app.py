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

BLAZEGRAPH_URL = 'http://localhost:9999/blazegraph/namespace/yournamespace/sparql'

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
            'lastName': user['last_name']
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

@app.route('/news', methods=['GET'])
def get_news():
    #return jsonify("News")
    # Define the SPARQL query

    ttl_file = './users_graph/ab@gmail.com.ttl'

    email = request.json.get('email', None)

    sparql_query = f"""
    PREFIX ns1: <http://visualdataweb.org/SoreOntology/>
    PREFIX ns2: <http://visualdataweb.org/SoreOntology/personOntology/>
    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
    PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

    SELECT ?news ?title ?author ?description ?publishedAt ?urlToImage ?url
    WHERE {{
      ?user ns2:hasEmail "{email}"^^xsd:string .
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

    g = Graph()
    # Load the graph
    g.parse(ttl_file, format="turtle")  # Replace "your_rdf_file.ttl" with your actual RDF file

    # Execute the SPARQL query
    query_results = g.query(sparql_query)

    # Convert the results to JSON
    news_data = []
    for result in query_results:
        news_entry = {
            'news': str(result['news']),
            'title': str(result['title']),
            'author': str(result['author']) if result['author'] else None,
            'description': str(result['description']) if result['description'] else None,
            'publishedAt': str(result['publishedAt']) if result['publishedAt'] else None,
            'urlToImage': str(result['urlToImage']) if result['urlToImage'] else None,
            'url': str(result['url']) if result['url'] else None,
        }
        news_data.append(news_entry)

    import json
    print(json.dumps(news_data, indent=2))

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

if __name__ == '__main__':
    app.run()
