import spacy
from collections import Counter
from newsAPI.getDataInfo import get_news_articles
nlp = spacy.load("en_core_web_sm")

end_point = '/top-headlines'  # /everything
language = 'us'
category = 'health'  # None, business, entertainment, general, health, science, sports, technology
pageSize = 30  # 20 to 100
country = 'us'  # random.choice(cst.country_codes)
interests = ['treatment', 'life']

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
    print(f"Name: {article['author']}")
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

'''{'source': {'id': None, 'name': 'Medical Xpress'}, 'author': 'Science X', 'title': 'New treatment shows promise against fatal neurological disease: Study - Medical Xpress', 'description': 'A new treatment shows promise against the deadly neurodegenerative disease ALS, a study based on mice showed Tuesday.', 'url': 'https://medicalxpress.com/news/2024-01-treatment-fatal-neurological-disease.html', 'urlToImage': 'https://scx2.b-cdn.net/gfx/news/2024/french-musician-guilhe.jpg', 'publishedAt': '2024-01-31T09:39:03Z', 'content': "A new treatment shows promise against the deadly neurodegenerative disease ALS, a study based on mice showed Tuesday.\r\nAmyotrophic lateral sclerosis, sometimes called Lou Gehrig's disease after the f… [+2755 chars]"}
Source: Medical_Xpress
Title: New treatment shows promise against fatal neurological disease: Study - Medical Xpress
Name: Science X
Description: A new treatment shows promise against the deadly neurodegenerative disease ALS, a study based on mice showed Tuesday.
Published at: 2024-01-31T09:39:03Z
Picture: https://scx2.b-cdn.net/gfx/news/2024/french-musician-guilhe.jpg
URL: https://medicalxpress.com/news/2024-01-treatment-fatal-neurological-disease.html
Content: A new treatment shows promise against the deadly neurodegenerative disease ALS, a study based on mice showed Tuesday.
Amyotrophic lateral sclerosis, sometimes called Lou Gehrig's disease after the f… [+2755 chars]
Top 5 Relevant Words: ['treatment', 'shows', 'promise', 'disease', 'New', 'fatal', 'neurological', 'Study', 'Medical', 'Xpress']'''