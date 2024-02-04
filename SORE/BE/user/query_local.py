from rdflib import Graph, URIRef, Literal, RDF, RDFS, XSD

# Assuming user_graph is your RDF graph containing user data
user_graph = "./users_graph/"

# Define the SPARQL query
sparql_query = """
PREFIX ns1: <http://visualdataweb.org/SoreOntology/>
PREFIX ns2: <http://visualdataweb.org/SoreOntology/personOntology/>
PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX xsd: <http://www.w3.org/2001/XMLSchema#>

SELECT ?newsItem ?title ?author ?description ?datePublished ?imageUrl ?newsUrl
WHERE {
  ?user a ns2:User ;
        ns2:hasEmail 'john_smith@example.com'^^xsd:string ;
        ns2:hasRecommendedItem ?newsItem .

  ?newsItem rdf:type ns1:News ;
            ns1:hasTitle ?title ;
            ns1:hasAuthor ?author ;
            ns1:hasDescription ?description ;
            ns1:hasDatePublished ?datePublished ;
            ns1:hasImageURL ?imageUrl ;
            ns1:hasNewsUrl ?newsUrl .
}
"""

# Execute the SPARQL query
query_results = user_graph.query(sparql_query)

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

# Print the news data as JSON
import json
print(json.dumps(news_data, indent=2))