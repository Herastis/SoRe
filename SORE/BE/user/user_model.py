from rdflib import Namespace, URIRef, Literal, Graph
from rdflib.namespace import FOAF, RDF, XSD, OWL, RDFS
import random
from BE.constants import constants as cst
from BE.news.news import news_articles
from BE.healthandlifestyle.medical_onto import medical_articles
from BE.joke.get_jokes import *

path = '../SoreOntology/sore.ttl'

# Define namespaces
sore = Namespace("http://visualdataweb.org/SoreOntology/")
person_ontology = Namespace("http://visualdataweb.org/SoreOntology/personOntology/")

#stop words

class User:
    def __init__(self, first_name, last_name, email, gender, status, interests, country, work, education, age, knows):
        self.graph = Graph()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.status = status
        self.interests = interests
        self.country = country
        self.work = work
        self.education = education
        self.age = age
        self.knows = knows
        print('User created')

    def add_health_info(self, interests, country, language):

        user_uri = URIRef(f"http://soreOntology.com/users/{self.first_name}_{self.last_name}")

        articles, top_words = medical_articles(interests, country, language)

        i = 0

        for article in articles:
            medical_onto_URI = article['title'].replace(' ', '')

            article_uri = URIRef(f"http://soreOntology.com/medicalNews/{medical_onto_URI}")
            self.graph.add((user_uri, person_ontology.hasRecommendedItem, article_uri))

            self.graph.add((article_uri, RDF.type, sore.Medical_and_Lifestyle))
            self.graph.add((article_uri, sore.hasTitle, Literal(article['title'], datatype=XSD.string)))
            if article['author'] is not None:
                author_name = '_'.join(article['author'].split())
                self.graph.add((article_uri, sore.hasAuthor, Literal(author_name, datatype=XSD.string)))
            else:
                self.graph.add((article_uri, sore.hasAuthor, Literal("undefined", datatype=XSD.string)))

            self.graph.add(
                (article_uri, sore.hasDescription, Literal(article['description'], datatype=XSD.string)))
            self.graph.add(
                (article_uri, sore.hasMedicalUrl, Literal(article['url'], datatype=XSD.string)))
            self.graph.add((article_uri, sore.hasContent, Literal(article['urlToImage'], datatype=XSD.string)))
            for topic in top_words[i]:
                topic_literal = Literal(topic, datatype=XSD.string)

                # Add RDF triples for the topicItemName property
                topic_uri = URIRef(f"http://soreOntology.com/topicsItem/{topic.replace(' ', '_')}")
                self.graph.add((article_uri, sore.hasTopic, topic_uri))
                self.graph.add((topic_uri, RDF.type, sore.topicItemName))
                self.graph.add((topic_uri, RDFS.label, topic_literal))

            #self.graph.add((article_uri, sore.hasTopic, Literal(topic, datatype=XSD.string)))
            i = i + 1

    def add_joke(self, category):
        user_uri = URIRef(f"http://soreOntology.com/users/{self.first_name}_{self.last_name}")

        jokes = call_joke_api(category)
        for joke_data in jokes:
            joke = Joke(**joke_data)

            joke_uri = URIRef(f"http://soreOntology.com/joke/{joke.frequent_words[0]}")

            self.graph.add((user_uri, person_ontology.hasJoke, joke_uri))
            self.graph.add((joke_uri, RDF.type, sore.Joke))

            self.graph.add((joke_uri, sore.type, Literal(joke.type)))
            self.graph.add((joke_uri, sore.isSafe, Literal(joke.is_safe)))
            self.graph.add((joke_uri, sore.category, Literal(joke.category)))
            self.graph.add((joke_uri, sore.setup, Literal(joke.setup)))
            self.graph.add((joke_uri, sore.delivery, Literal(joke.delivery)))


            for topic in joke.frequent_words:
                topic_literal = Literal(topic, datatype=XSD.string)

                # Add RDF triples for the topicItemName property
                topic_uri = URIRef(f"http://soreOntology.com/topicsJoke/{topic.replace(' ', '_')}")
                self.graph.add((joke_uri, sore.hasTopic, topic_uri))
                self.graph.add((topic_uri, RDF.type, sore.JokeTopic))
                self.graph.add((topic_uri, RDFS.label, topic_literal))

    def add_interest_news(self, interests, country, language):
        user_uri = URIRef(f"http://soreOntology.com/users/{self.first_name}_{self.last_name}")

        end_point = '/everything'  # /everything /top-headlines

        articles, top_words = news_articles(interests, end_point, country, language)
        i = 0
        for article in articles:

            news_name_URI = article['title'].replace(' ', '')
            article_uri = URIRef(f"http://soreOntology.com/news/{news_name_URI}")

            self.graph.add((user_uri, person_ontology.hasRecommendedItem, article_uri))
            # Add RDF triples for the news article
            self.graph.add((article_uri, RDF.type, sore.News))
            self.graph.add((article_uri, sore.hasTitle, Literal(article['title'], datatype=XSD.string)))

            if article['author'] is not None:
                author_name = '_'.join(article['author'].split())
                self.graph.add((article_uri, sore.hasAuthor, Literal(author_name, datatype=XSD.string)))
            else:
                self.graph.add((article_uri, sore.hasAuthor, Literal("undefined", datatype=XSD.string)))

            self.graph.add(
                (article_uri, sore.hasDescription, Literal(article['description'], datatype=XSD.string)))
            self.graph.add(
                (article_uri, sore.hasDatePublished, Literal(article['publishedAt'], datatype=XSD.string)))
            self.graph.add(
                (article_uri, sore.hasImageURL, Literal(article['urlToImage'], datatype=XSD.string)))
            self.graph.add((article_uri, sore.hasNewsUrl, Literal(article['url'], datatype=XSD.string)))
            for topic in top_words[i]:
                topic_literal = Literal(topic, datatype=XSD.string)

                # Add RDF triples for the topicItemName property
                topic_uri = URIRef(f"http://soreOntology.com/topicsItem/{topic.replace(' ', '_')}")
                self.graph.add((article_uri, sore.hasJokeTopic, topic_uri))
                self.graph.add((topic_uri, RDF.type, sore.topicItemName))
                self.graph.add((topic_uri, RDFS.label, topic_literal))

            #self.graph.add((article_uri, sore.hasTopic, Literal(topic, datatype=XSD.string)))
            i = i + 1

    def update_interests(self, updated_interests):
        pass

    def add_friends(self, knows):
        user_uri = URIRef(f"http://soreOntology.com/users/{self.first_name}_{self.last_name}")

        for known_email in knows:
            #known_uri = person_ns[known_email]
            #update later with the URI of the known user
            self.graph.add((user_uri, person_ontology.knows, Literal(known_email)))

    def to_rdf(self):
        user_uri = URIRef(f"http://soreOntology.com/users/{self.first_name}_{self.last_name}")

        # User instance
        self.graph.add((user_uri, RDF.type, person_ontology.User))
        self.graph.add((user_uri, person_ontology.firstName, Literal(self.first_name, datatype=XSD.string)))
        self.graph.add((user_uri, person_ontology.lastName, Literal(self.last_name, datatype=XSD.string)))
        self.graph.add((user_uri, person_ontology.gender, Literal(self.gender, datatype=XSD.string)))
        self.graph.add((user_uri, person_ontology.status, Literal(self.status, datatype=XSD.string)))
        self.graph.add((user_uri, person_ontology.hasAge, Literal(self.age, datatype=XSD.integer)))
        self.graph.add((user_uri, person_ontology.hasCountry, Literal(self.country, datatype=XSD.string)))
        self.graph.add((user_uri, person_ontology.workingPlace, Literal(self.work, datatype=XSD.string)))
        self.graph.add((user_uri, person_ontology.hasEducation, Literal(self.education, datatype=XSD.string)))
        self.graph.add((user_uri, person_ontology.hasEmail, Literal(self.email, datatype=XSD.string)))

        # Adding 'knows' relationship
        if self.knows:
            for known_email in self.knows:
                #known_uri = person_ns[known_email]
                #update later with the URI of the known user
                self.graph.add((user_uri, person_ontology.knows, Literal(known_email)))

        print('here')
        # Interests
        for interest in self.interests:
            interest_uri = URIRef(f"http://soreOntology.com/interestsUser/{interest}")
            self.graph.add((user_uri, person_ontology.hasInterest, interest_uri))
            self.graph.add((interest_uri, RDF.type, sore.Interest))
            self.graph.add((interest_uri, RDFS.label, Literal(interest, datatype=XSD.string)))

        return self.graph

first_name = "John"
last_name = "Doe"
email = "john.doe@example.com"
gender = random.choice(["Male", "Female"])
status = cst.status_options[random.randint(0, len(cst.status_options)-1)]
#
news_interests = ["Art", "Technology", "Travel", "Coding", "Gaming"]
jokes_category = ['Programming', 'Misc', 'Pun', 'Spooky', 'Christmas']
health_interests = ['treatment', 'health', 'covid']
#
country = random.choice(cst.european_countries)
work = random.choice(["Student", "Teacher", "Engineer"])
education = random.choice(["HighSchool", "Bachelor", "Master"])
age = cst.age
knows = ['user2@gmail.com', 'user3@gmail.com']
def create_user(file_path, first_name, last_name, email, gender, status, news_interests, jokes_category, health_interests,  country, work, education, age, knows):

    User1 = User(first_name, last_name, email, gender, status, news_interests, country, work, education, age, knows)

    user_graph = User1.to_rdf()
    # Print the resulting RDF graph
    #print(user_graph.serialize(format="turtle"))

    new_friends = ['user123@gmail.com', 'user456@gmail.com']
    User1.add_friends(new_friends)
    #print(user_graph.serialize(format="turtle"))

    User1.add_interest_news(news_interests, 'us', 'us')
    #print(user_graph.serialize(format="turtle"))



    User1.add_health_info(health_interests, 'us', 'us')
    #print(user_graph.serialize(format="turtle"))

    joke_category = random.choice(category_web)

    User1.add_joke(joke_category)
    #print(user_graph.serialize(format="turtle"))
    turtle_data = user_graph.serialize(format="turtle")

    user_graph.serialize(file_path + f'{email}.ttl', format="turtle")

    print(f"Graph saved successfully to {email}.ttl")

#file_path = './'
#create_user(file_path, first_name, last_name, email, gender, status, news_interests,jokes_category, health_interests, country, work, education, age, knows)


