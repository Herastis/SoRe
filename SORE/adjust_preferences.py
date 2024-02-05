import sklearn
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np
from BE.constants.constants import *

from rdflib import Graph

import requests




def get_medical_news_for_email(g, email):
    sparql_query_medical = f"""
        PREFIX ns1: <http://visualdataweb.org/SoreOntology/>
        PREFIX ns2: <http://visualdataweb.org/SoreOntology/personOntology/>
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>
        
        SELECT DISTINCT ?medicalNews ?title ?author ?description ?hasMedicalUrl
        WHERE {{
          ?user ns2:hasEmail "{email}" .
          ?user ns2:hasRecommendedItem ?medicalNews .
          ?medicalNews a ns1:Medical_and_Lifestyle .
          ?medicalNews ns1:hasTitle ?title .
          OPTIONAL {{ ?medicalNews ns1:hasAuthor ?author . }}
          OPTIONAL {{ ?medicalNews ns1:hasDescription ?description . }}
          OPTIONAL {{ ?medicalNews ns1:hasMedicalUrl ?url . }}
        }}
        """
    print('here')

    results = g.query(sparql_query_medical)

    medical_data = []
    for result in results:
        medical_entry = {
            'medicalNews': str(result['medicalNews']),
            'title': str(result['title']),
            'author': str(result['author']) if result['author'] else None,
            'description': str(result['description']) if result['description'] else None,
            'hasMedicalUrl': str(result['hasMedicalUrl']) if result['hasMedicalUrl'] else None,
        }
        print(medical_entry)
        medical_data.append(medical_entry)

    return medical_data


def get_news_for_email(g, email):
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

    results = g.query(sparql_query)

    # Convert the results to JSON
    news_data = []
    for result in results:
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

    return news_data



def get_most_words_news(users_graph_directory, email):
    g = Graph()
    file = f'{email}.ttl'
    g.parse(users_graph_directory + file, format="turtle")
    #g.serialize(format="turtle")
    text = get_news_for_email(g, email)

    article_text = ""
    for news_item in text:
        title = news_item.get('title', 'No Title Provided')
        description = news_item.get('description', 'No Description Provided')
        article_text += title + " " + description

    tokens = article_text.lower().split()

    filtered_tokens = ' '.join(word for word in tokens if word not in stopwords)

    words_news = get_most_relevant_words(filtered_tokens)

    text = get_medical_news_for_email(g, email)
    print(text)

    words_medical_news = ['test']


    return words_news, words_medical_news


def get_most_relevant_words(article_text):
    # Example article text

    # Preprocess text and compute TF-IDF
    vectorizer = TfidfVectorizer(stop_words='english', lowercase=True)
    tfidf_matrix = vectorizer.fit_transform([article_text])

    # Get feature names (words) from the vectorizer
    feature_names = np.array(vectorizer.get_feature_names_out())

    # Get TF-IDF scores for each word in the article
    tfidf_scores = tfidf_matrix[0].toarray()[0]

    # Sort words based on TF-IDF scores and get the most relevant words
    most_relevant_words_indices = tfidf_scores.argsort()[::-1]  # Sort in descending order
    num_top_words = 5  # Set the number of top words you want to extract
    top_words = feature_names[most_relevant_words_indices][:num_top_words]

    # Print the most relevant words
    print("Most Relevant Words:")
    return top_words


#Testing
users_graph_directory = "./users_graph/"
email = "stoleriumihai@gmail.com"
new_news_interest,new_medical_news_interest = get_most_words_news(users_graph_directory,email)

print(new_news_interest,new_medical_news_interest)

email = "tudor.tomescu@gmail.com"
users_graph_directory = './users_graph/'
new_news_interest1,new_medical_news_interest1 = get_most_words_news(users_graph_directory,email)

print(new_news_interest1,new_medical_news_interest1)






