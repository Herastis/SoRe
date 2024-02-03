import requests
from collections import Counter

languages = ['en', 'de', 'es','fr','pt', 'cs']
flags = 'nsfw,racist,sexist,explicit'
two_joke = 'twopart'
q = ['photo'] # ?
category = ['Programming', 'Misc', 'Dark', 'Pun', 'Spooky', 'Christmas']
param = ['Any']
amount = 10
base_url = "https://v2.jokeapi.dev/joke"

category_any = 'Any'

url = base_url + '/' + category_any + f"?blacklistFlags={flags}&type={two_joke}&amount={amount}&language={languages[1]}"

response = requests.get(url)

data = response.json()

jokes = data['jokes']
print(jokes)
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
        words = self.setup.split() + self.delivery.split()
        word_counts = Counter(words)
        self.frequent_words = [word for word, count in word_counts.most_common(3)]


for joke_data in jokes:
    joke = Joke(**joke_data)
    print(joke.delivery)
    print(joke.type)
    print(joke.is_safe)
    print(joke.setup)
    print(joke.category)
    print(joke.frequent_words)
