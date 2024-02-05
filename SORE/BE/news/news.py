import spacy
from collections import Counter
from BE.newsAPI.getDataInfo import get_news_articles
nlp = spacy.load("en_core_web_sm")
from BE.constants import constants as cst

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
