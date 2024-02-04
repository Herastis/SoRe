# db.py
from pymongo import MongoClient
import requests

client = MongoClient("mongodb://localhost:27017/")
db = client["SORE"]

# URL-ul endpoint-ului SPARQL al instanței Blazegraph
BLAZEGRAPH_URL = 'http://localhost:9999/blazegraph/sparql'

# news_query = """
#     PREFIX ex: <http://example.org/schema/>
#
#     SELECT ?title ?description WHERE {
#         ?news ex:title ?title ;
#               ex:description ?description .
#     }
#     LIMIT 10
#     """
def execute_sparql_query(query):
    response = requests.post(
        BLAZEGRAPH_URL,
        data={"query": query},
        headers={"Accept": "application/sparql-results+json"}
    )
    if response.status_code == 200:
        return response.json()
    else:
        return None

