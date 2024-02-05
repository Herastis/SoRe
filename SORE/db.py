# db.py
from pymongo import MongoClient
import requests

client = MongoClient("mongodb://localhost:27017/")
db = client["SORE"]

BLAZEGRAPH_URL = 'http://localhost:9999/blazegraph/sparql'

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

