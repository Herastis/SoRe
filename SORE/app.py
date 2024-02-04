from flask_cors import CORS
from flask import Flask, request, jsonify
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager, create_access_token
from werkzeug.security import check_password_hash, generate_password_hash
from db import db, execute_sparql_query
from datetime import timedelta


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
                                })

    #User = User.create_user_graph()
    #User.set_friends()


    return jsonify({"msg": "User registered successfully."}), 201

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

@app.route('/news', methods=['GET'])
def get_news():
    #return jsonify("News")
    query = """
        PREFIX ns1: <http://example.org/news#>

        SELECT ?title ?author ?description ?imageUrl WHERE {
            ?news a ns1:NewsArticle ;
                  ns1:hasTitle ?title ;
                  ns1:hasAuthor ?author ;
                  ns1:hasDescription ?description ;
                  ns1:hasImageUrl ?imageUrl .
        }
        LIMIT 10
        """
    results = execute_sparql_query(query)
    if results:
        news_items = results.get("results", {}).get("bindings", [])
        news = [{
            "title": item["title"]["value"],
            "author": item["author"]["value"],
            "description": item["description"]["value"],
            "image": item["imageUrl"]["value"]
        } for item in news_items]
        return jsonify(news)
    else:
        return jsonify({"error": "Could not retrieve news"}), 500

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
