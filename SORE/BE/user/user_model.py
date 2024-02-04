from urllib.parse import quote

from rdflib import Namespace, URIRef, Literal, Graph
from rdflib.namespace import RDF, XSD, RDFS

from BE.healthandlifestyle.medical_onto import medical_articles
from BE.joke.get_jokes import *
from BE.news.news import news_articles
from BE.constants.constants import age

path = '../SoreOntology/sore.ttl'

# Define namespaces
sore = Namespace("http://visualdataweb.org/SoreOntology/")
person_ontology = Namespace("http://visualdataweb.org/SoreOntology/personOntology/")


# stop words

# first , last, email, status, geneder, age, workingplace, education, country, language -> get after country
class User:
    def __init__(self, first_name, last_name, email, gender, status, country, work, interests, education, age):
        self.graph = Graph()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.gender = gender
        self.status = status
        self.country = country
        self.work = work
        self.interests = interests
        self.education = education
        self.age = age
        self.knows = []
        print('User created')

    def get_user_rdf(self):
        user_uri = URIRef(f"http://soreOntology.com/users/{self.first_name}_{self.last_name}_{self.email}")
        return self.graph, user_uri

    def set_interests(self, new_interests):
        self.interests = new_interests
        g, user_uri = self.get_user_rdf()
        for interest in self.interests:
            interest_uri = URIRef(f"http://soreOntology.com/interestsUser/{interest}")
            g.add((user_uri, person_ontology.hasInterest, interest_uri))
            g.add((interest_uri, RDF.type, sore.Interest))
            g.add((interest_uri, RDFS.label, Literal(interest, datatype=XSD.string)))

    def get_first_name(self):
        return self.first_name

    def get_last_name(self):
        return self.last_name

    def get_email(self):
        return self.email

    def get_gender(self):
        return self.gender

    def get_status(self):
        return self.status

    def get_country(self):
        return self.country

    def get_work(self):
        return self.work

    def get_interests(self):
        return self.interests

    def get_education(self):
        return self.education

    def get_age(self):
        return self.age

    def get_graph(self):
        return self.graph


    def add_health_info(self, interests, country, language):  # health_interests

        g, user_uri = self.get_user_rdf()


        articles, top_words = medical_articles(interests, country, language)

        i = 0

        for article in articles:
            medical_onto_URI = article['title'].replace(' ', '')

            encoded_frequent_word = quote(medical_onto_URI)

            article_uri = URIRef(f"http://soreOntology.com/medicalNews/{encoded_frequent_word}")
            g.add((user_uri, person_ontology.hasRecommendedItem, article_uri))

            g.add((article_uri, RDF.type, sore.Medical_and_Lifestyle))
            g.add((article_uri, sore.hasTitle, Literal(article['title'], datatype=XSD.string)))
            if article['author'] is not None:
                author_name = '_'.join(article['author'].split())
                g.add((article_uri, sore.hasAuthor, Literal(author_name, datatype=XSD.string)))
            else:
                g.add((article_uri, sore.hasAuthor, Literal("undefined", datatype=XSD.string)))

            g.add(
                (article_uri, sore.hasDescription, Literal(article['description'], datatype=XSD.string)))
            g.add(
                (article_uri, sore.hasMedicalUrl, Literal(article['url'], datatype=XSD.string)))
            g.add((article_uri, sore.hasContent, Literal(article['urlToImage'], datatype=XSD.string)))
            for topic in top_words[i]:
                topic_literal = Literal(topic, datatype=XSD.string)

                # Add RDF triples for the topicItemName property
                topic_uri = URIRef(f"http://soreOntology.com/topicsItem/{topic.replace(' ', '_')}")
                g.add((article_uri, sore.hasTopic, topic_uri))
                g.add((topic_uri, RDF.type, sore.topicItemName))
                g.add((topic_uri, RDFS.label, topic_literal))

            # self.graph.add((article_uri, sore.hasTopic, Literal(topic, datatype=XSD.string)))
            i = i + 1

    def add_jokes_info(self, category):  # joke_category, email
        g,user_uri = self.get_user_rdf()

        jokes = call_joke_api(category)
        for joke_data in jokes:
            joke = Joke(**joke_data)

            encoded_frequent_word = quote(joke.frequent_words[0])

            joke_uri = URIRef(f"http://soreOntology.com/joke/{encoded_frequent_word}")

            g.add((user_uri, person_ontology.hasJoke, joke_uri))
            g.add((joke_uri, RDF.type, sore.Joke))

            g.add((joke_uri, sore.type, Literal(joke.type)))
            g.add((joke_uri, sore.isSafe, Literal(joke.is_safe)))
            g.add((joke_uri, sore.category, Literal(joke.category)))
            g.add((joke_uri, sore.setup, Literal(joke.setup)))
            g.add((joke_uri, sore.delivery, Literal(joke.delivery)))

            for topic in joke.frequent_words:
                topic_literal = Literal(topic, datatype=XSD.string)

                # Add RDF triples for the topicItemName property
                topic_uri = URIRef(f"http://soreOntology.com/topicsJoke/{topic.replace(' ', '_')}")
                g.add((joke_uri, sore.hasTopic, topic_uri))
                g.add((topic_uri, RDF.type, sore.JokeTopic))
                g.add((topic_uri, RDFS.label, topic_literal))

    def add_news_info(self, interests, country, language):  # interest_news_interests, country, language, email
        g, user_uri = self.get_user_rdf()

        end_point = '/everything'  # /everything /top-headlines

        articles, top_words = news_articles(interests, end_point, country, language)
        i = 0
        for article in articles:

            news_name_URI = article['title'].replace(' ', '')

            encoded_frequent_word = quote(news_name_URI)

            article_uri = URIRef(f"http://soreOntology.com/news/{encoded_frequent_word}")

            g.add((user_uri, person_ontology.hasRecommendedItem, article_uri))
            # Add RDF triples for the news article
            g.add((article_uri, RDF.type, sore.News))
            g.add((article_uri, sore.hasTitle, Literal(article['title'], datatype=XSD.string)))

            if article['author'] is not None:
                author_name = '_'.join(article['author'].split())
                g.add((article_uri, sore.hasAuthor, Literal(author_name, datatype=XSD.string)))
            else:
                g.add((article_uri, sore.hasAuthor, Literal("undefined", datatype=XSD.string)))

            g.add(
                (article_uri, sore.hasDescription, Literal(article['description'], datatype=XSD.string)))
            g.add(
                (article_uri, sore.hasDatePublished, Literal(article['publishedAt'], datatype=XSD.string)))
            g.add(
                (article_uri, sore.hasImageURL, Literal(article['urlToImage'], datatype=XSD.string)))
            g.add((article_uri, sore.hasNewsUrl, Literal(article['url'], datatype=XSD.string)))
            for topic in top_words[i]:
                topic_literal = Literal(topic, datatype=XSD.string)

                # Add RDF triples for the topicItemName property
                topic_uri = URIRef(f"http://soreOntology.com/topicsItem/{topic.replace(' ', '_')}")
                g.add((article_uri, sore.hasJokeTopic, topic_uri))
                g.add((topic_uri, RDF.type, sore.topicItemName))
                g.add((topic_uri, RDFS.label, topic_literal))

            # self.graph.add((article_uri, sore.hasTopic, Literal(topic, datatype=XSD.string)))
            i = i + 1


    def add_friends(self, knows):  # knows, email

        g, user_uri = self.get_user_rdf()

        for known_email in knows:
            # known_uri = person_ns[known_email]
            # update later with the URI of the known user
            g.add((user_uri, person_ontology.knows, Literal(known_email)))

    def to_rdf(self):
        user_uri = URIRef(f"http://soreOntology.com/users/{self.first_name}_{self.last_name}_{self.email}")

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

        print('here')
        # Interests #descos
        for interest in self.interests:
            interest_uri = URIRef(f"http://soreOntology.com/interestsUser/{interest}")
            self.graph.add((user_uri, person_ontology.hasInterest, interest_uri))
            self.graph.add((interest_uri, RDF.type, sore.Interest))
            self.graph.add((interest_uri, RDFS.label, Literal(interest, datatype=XSD.string)))

        return self.graph



def create_user(file_path,  first_name, last_name, email, gender, status, country, work, interests, education, age):

    user = User(first_name, last_name, email, gender, status, country, work, interests, education, age)

    user_graph = user.to_rdf()

    user_graph.serialize(file_path + f'{email}.ttl', format="turtle")

    print(f"Graph saved successfully to {email}.ttl")

    return user

file_path = './'
first_name = 'John'
last_name = 'Smith'
email = 'john_smith@example.com'
gender = 'male'
status = 'Single'
country = 'United States'
work = 'United States'
interests = ['sports', 'technology', 'politics', 'AI', 'gaming']
education = 'Bachelor'
AGE = age

usr = create_user(file_path,  first_name, last_name, email, gender, status, country, work, interests, education, AGE)
g, user_uri = usr.get_user_rdf()


def update_profile_to_display(usr, news_interests, health_interests, joke_category, country, language):
    usr.add_health_info(news_interests, country, language)
    usr.add_news_info(health_interests, country, language)
    usr.add_jokes_info(joke_category)

    g, user_uri = usr.get_user_rdf()
    g.serialize(file_path + f'{email}.ttl', format="turtle")

    print(f"Graph saved successfully to {email}.ttl")


news_interests = ['sports', 'technology', 'politics',  'gaming']
health_interests = ['covid', 'vaccine', 'treatment', 'technology']
joke_category = 'Christmas'
country_code = cst.country_mapping[country]
language = cst.languages_reversed[country]
update_profile_to_display(usr, news_interests , health_interests, joke_category, country, language)

print(g.serialize(format="turtle"))
print(user_uri)

