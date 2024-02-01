import requests
import spacy
from collections import Counter
from rdflib import Graph, Namespace, URIRef, Literal, XSD, RDF, RDFS

interests = ["AI", "Art", "Exploration", "Gaming", "Music"]


# Function to add triples for a news article
def add_news_triples(article, top_topics,i, file_path=".\\news_ind.rdf"):
    # Define the namespace for the ontology
    news_ns = Namespace("http://example.org/news#")

    # Load existing RDF graph from file if it exists
    g = Graph()
    try:
        # Use parse method to load RDF data from the file
        g.parse(file_path, format="turtle")
    except FileNotFoundError:
        # File doesn't exist yet, create an empty graph
        pass

    # Extract source name and concatenate for news_name
    source_name = article['source']['name']
    news_name = '_'.join(source_name.split())
    i =  str(i)
    news_name = news_name + i
    # Define a news article URI
    article_uri = URIRef(f"http://example.org/news/{news_name}")

    # Add triples for the news article
    g.add((article_uri, RDF.type, news_ns.NewsArticle))
    g.add((article_uri, news_ns.hasTitle, Literal(article['title'])))
    g.add((article_uri, news_ns.hasAuthor, Literal(article['author'])))
    g.add((article_uri, news_ns.hasDescription, Literal(article['description'])))
    g.add((article_uri, news_ns.hasDatePublished, Literal(article['publishedAt'], datatype=XSD.dateTime)))
    g.add((article_uri, news_ns.hasUrl, Literal(article['url'])))
    g.add((article_uri, news_ns.hasImageUrl, Literal(article['urlToImage'])))
    g.add((article_uri, news_ns.hasTopics, Literal(str(top_topics))))

    # Save the entire graph to the file
    g.serialize(destination=file_path, format="turtle")

def get_news_articles(interests):

    # Load the English language model
    nlp = spacy.load("en_core_web_sm")
    #python -m spacy download en_core_web_sm


    # Replace 'YOUR_API_KEY' with your actual News API key
    api_key = '3520f08cf9bb4b94b614bf7fcfb7e8bf'
    base_url = 'https://newsapi.org/v2/everything'

    # Specify parameters for the API request
    params = {
        'apiKey': api_key,
        'lang': 'en',
        'sortBy': 'popularity',
        'q': interests
    }

    # Make the API request
    response = requests.get(base_url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        news_data = response.json()

        # Extract and print relevant information
        articles = news_data['articles']
        i = 0
        for article in articles:
            source_name = article['source']['name']
            # Concatenating the name parts separated by spaces
            news_name = '_'.join(source_name.split())
            print(news_name)
            print(f"Title: {article['title']}")
            print(f"Name: {article['author']}")
            print(f"Description: {article['description']}")
            print(f'Published at: {article["publishedAt"]}')
            print(f'Picture: {article["urlToImage"]}')
            print(f"URL: {article['url']}")
            # Combine title and description text
            text_combined = f"{article['title']} {article['description']}"

            # Process the combined text using spaCy
            doc = nlp(text_combined)

            # Extract unique words and their frequencies
            word_freq = Counter(token.text for token in doc if not token.is_stop and token.is_alpha)

            # Select the top 3 most frequent words
            top_words = [word for word, freq in word_freq.most_common(3)]

            print(f"Top 3 Relevant Words: {top_words}")
            print('\n')
            add_news_triples(article, top_words, i)
            i = i + 1

    else:
        # Print an error message if the request was not successful
        print(f"Error: {response.status_code} - {response.text}")

get_news_articles(interests)


