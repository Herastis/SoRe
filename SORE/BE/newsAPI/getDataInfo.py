import requests
import spacy
from collections import Counter
from constants import constants as cst
import random

api_key = cst.api_key
end_point = '/top-headlines'  # /everything
language = 'us'
category = 'health'  # None, business, entertainment, general, health, science, sports, technology
pageSize = 30  # 20 to 100
country = 'us'  # random.choice(cst.country_codes)
interests = ['treatment', 'life']


def get_news_articles(interests, end_point, language, category=None, country=None):  # from,to
    # Load the English language model
    nlp = spacy.load("en_core_web_sm")
    # python -m spacy download en_core_web_sm

    # Replace 'YOUR_API_KEY' with your actual News API key
    base_url = cst.base_url + end_point
    params = {}
    if end_point == '/top-headlines':

        if category is not None and country is not None and language is not None:
            params = {
                'apiKey': api_key,
                'lang': language,
                'country': country,
                'category': category,
                'q': interests,
                'pageSize': pageSize
            }
        elif category is not None and country is not None:
            params = {
                'apiKey': api_key,
                'lang': 'en',
                'country': country,
                'category': category,
                'sortBy': 'relevancy',
                'q': interests,
                'pageSize': pageSize
            }
        elif country is not None:
            params = {
                'apiKey': api_key,
                'lang': 'en',
                'country': country,
                'sortBy': 'relevancy',
                'q': interests,
                'pageSize': pageSize
            }
        else:
            return "No parameters for the request"
    else:
        if language is not None and country is not None:
            params = {
                'apiKey': api_key,
                'lang': language,
                'searchIn': 'title,description,content',
                'sortBy': 'popularity',
                'q': interests,
                'pageSize': pageSize
            }
        else:
            return "No parameters for the request"

    response = requests.get(base_url, params=params)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Parse the JSON response
        news_data = response.json()
        # Extract and print relevant information
        articles = news_data['articles']

        return articles
    else:
        # Print an error message if the request was not successful
        print(f"Error: {response.status_code} - {response.text}")


#get_news_articles(interests, end_point, language, category, country)
