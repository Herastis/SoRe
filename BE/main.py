from rdflib import Namespace, URIRef, Literal, Graph
from rdflib.namespace import FOAF, RDF, XSD, OWL, RDFS
import random

first_names = ['John', 'Jane', 'Bob', 'Alice', 'Charlie', 'Emma', 'Michael', 'Elizabeth', 'William', 'Sophia']
last_names = ['Smith', 'Johnson', 'Williams', 'Brown', 'Jones', 'Garcia', 'Miller', 'Davis', 'Rodriguez', 'Martinez']
interests = ["Coding", "Sports", "Music", "Art", "Reading", "Writing", "Coding", "Exploration", "Hiking", "Cuisine","Documentaries", "Conferences", "Gaming","AI","Photography",
             "Music"]

# Helper to generate random person
def get_random_person():
    person = {
        'name': f"{random.choice(first_names)}{random.choice(last_names)}",
        'interests': random.sample(interests, 5),
    }
    return person

# Function to build graph for person
def build_person_graph(person):
    g = Graph()

    person_uri = URIRef(f'http://example.com/person/{person["name"]}')

    g.add((person_uri, RDF.type, FOAF.Person))
    g.add((person_uri, FOAF.name, Literal(person['name'])))

    for interest in person['interests']:
        g.add((person_uri, FOAF.interest, Literal(interest)))

    return g

# Generate 3 random persons
person1 = get_random_person()
person2 = get_random_person()
person3 = get_random_person()

# Build RDF graphs
graph1 = build_person_graph(person1)
graph2 = build_person_graph(person2)
graph3 = build_person_graph(person3)

# Serialize graphs
graph1.serialize(f'{person1["name"]}.rdf')
graph2.serialize(f'{person2["name"]}.rdf')
graph3.serialize(f'{person3["name"]}.rdf')
