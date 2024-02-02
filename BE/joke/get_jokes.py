import requests

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

print(response.text)

#https://official-joke-api.appspot.com/random_ten