import random

import requests
from collections import Counter
import BE.constants.constants as cst

languages = ['en', 'de', 'es','fr','pt', 'cs']
flags = 'nsfw,racist,sexist,explicit'
two_joke = 'twopart'
q = ['photo'] # ?
category_web = ['Programming', 'Misc', 'Dark', 'Pun', 'Spooky', 'Christmas']
category_any = 'Any'

param = ['Any']
amount = 10



def call_joke_api(category):
    flags = 'nsfw,racist,sexist,explicit'
    two_joke = 'twopart'
    cate = ""
    if category is not None:
        cate = category
    else:
        cate = 'Any'

    base_url = "https://v2.jokeapi.dev/joke"
    amount = 10

    url = base_url + '/' + category + f"?blacklistFlags={flags}&type={two_joke}&amount={amount}&language={languages[1]}"

    response = requests.get(url)

    data = response.json()

    jokes = data['jokes']
    return jokes
class Joke:
    def __init__(self, category, type, setup, delivery, flags, id, safe, lang):
        self.id = id
        self.delivery = delivery
        self.type = type
        self.is_safe = safe
        self.setup = setup
        self.category = category
        self.lang = lang
        self.flags = flags

        # Get most frequent 3 words in setup and delivery

        # Words from self.setup and self.delivery, converted to lowercase
        words = [word.lower() for word in self.setup.split() + self.delivery.split()]

        word_counts = Counter(word for word in words if word.lower() not in cst.stopwords)
        self.frequent_words = [word for word, count in word_counts.most_common(3)]



