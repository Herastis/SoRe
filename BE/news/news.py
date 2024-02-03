import spacy
from collections import Counter
from newsAPI.getDataInfo import get_news_articles
nlp = spacy.load("en_core_web_sm")
from constants import constants as cst

api_key = cst.api_key
end_point = '/everything'  # /everything /top-headlines
language = 'us'
category = None  # None, business, entertainment, general, health, science, sports, technology
pageSize = 20  # 20 to 100
country = 'us'  # random.choice(cst.country_codes)
interests = ['Gaming' ,'AI', 'Coding']


def news_articles(interests, end_point, language, country):

    top_interests = []
    arts = get_news_articles(interests, end_point, language, category, country)
    for art in arts:

        txt_combined = f"{art['title']} {art['description']}"
        # Process the combined text using spaCy
        doc = nlp(txt_combined)

        # Extract unique words and their frequencies
        word_freq = Counter(token.text for token in doc if not token.is_stop and token.is_alpha)

        top_words = [word for word, freq in word_freq.most_common(5)]

        top_interests.append(top_words)

    return arts, top_interests


'''articles, top = news_articles(interests, end_point, language, country)
print(top)
for article in articles:
    source_name = article['source']['name']
    # Concatenating the name parts separated by spaces
    news_name = '_'.join(source_name.split())
    print(f'Source: {news_name}')
    print(f"Title: {article['title']}")
    if article['author'] is not None:
        name = '_'.join(article['author'].split())
    else:
        name = ""
    print(f"Name: {name}")
    print(f"Description: {article['description']}")
    print(f'Published at: {article["publishedAt"]}')
    print(f'Picture: {article["urlToImage"]}')
    print(f"URL: {article['url']}")
    print(f'Content: {article["content"]}')
    # Combine title and description text
    text_combined = f"{article['title']} {article['description']}"'''