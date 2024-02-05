import spacy
from collections import Counter
from newsAPI.getDataInfo import get_news_articles
nlp = spacy.load("en_core_web_sm")
from constants import constants as cst

api_key = cst.api_key
end_point = '/everything'  # /everything /top-headlines
language = 'us'
category = None  # None, business, entertainment, general, health, science, sports, technology
pageSize = 30  # 20 to 100
country = 'us'  # random.choice(cst.country_codes)
interests = ['Gaming' ,'AI', 'Coding']

articles = get_news_articles(interests, end_point, language, category, country)
for article in articles:
    print(article)
    source_name = article['source']['name']
    # Concatenating the name parts separated by spaces
    news_name = '_'.join(source_name.split())
    print(f'Source: {news_name}')
    print(f"Title: {article['title']}")
    name = article['author']
    name = ''.join(article['author'].split())
    print(f"Name: {name}")
    print(f"Description: {article['description']}")
    print(f'Published at: {article["publishedAt"]}')
    print(f'Picture: {article["urlToImage"]}')
    print(f"URL: {article['url']}")
    print(f'Content: {article["content"]}')
    # Combine title and description text
    text_combined = f"{article['title']} {article['description']}"

    # Process the combined text using spaCy
    doc = nlp(text_combined)

    # Extract unique words and their frequencies
    word_freq = Counter(token.text for token in doc if not token.is_stop and token.is_alpha)

    top_words = [word for word, freq in word_freq.most_common(10)]

    print(f"Top 5 Relevant Words: {top_words}")
    print('\n')
