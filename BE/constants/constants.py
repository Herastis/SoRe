import random

# List of countries by continent
african_countries = [
    'Algeria', 'Angola', 'Benin', 'Botswana', 'Burkina Faso', 'Burundi', 'Cabo Verde', 'Cameroon',
    'Central African Republic', 'Chad', 'Comoros', 'Democratic Republic of the Congo', 'Djibouti',
    'Egypt', 'Equatorial Guinea', 'Eritrea', 'Eswatini', 'Ethiopia', 'Gabon', 'Gambia', 'Ghana',
    'Guinea', 'Guinea-Bissau', 'Ivory Coast', 'Kenya', 'Lesotho', 'Liberia', 'Libya', 'Madagascar',
    'Malawi', 'Mali', 'Mauritania', 'Mauritius', 'Morocco', 'Mozambique', 'Namibia', 'Niger', 'Nigeria',
    'Rwanda', 'Sao Tome and Principe', 'Senegal', 'Seychelles', 'Sierra Leone', 'Somalia', 'South Africa',
    'South Sudan', 'Sudan', 'Tanzania', 'Togo', 'Tunisia', 'Uganda', 'Zambia', 'Zimbabwe'
]

asian_countries = [
    'Afghanistan', 'Armenia', 'Azerbaijan', 'Bahrain', 'Bangladesh', 'Bhutan', 'Brunei', 'Cambodia',
    'China', 'Cyprus', 'Georgia', 'India', 'Indonesia', 'Iran', 'Iraq', 'Israel', 'Japan', 'Jordan',
    'Kazakhstan', 'Kuwait', 'Kyrgyzstan', 'Laos', 'Lebanon', 'Malaysia', 'Maldives', 'Mongolia', 'Myanmar',
    'Nepal', 'North Korea', 'Oman', 'Pakistan', 'Palestine', 'Philippines', 'Qatar', 'Saudi Arabia',
    'Singapore', 'South Korea', 'Sri Lanka', 'Syria', 'Taiwan', 'Tajikistan', 'Thailand', 'Timor-Leste',
    'Turkey', 'Turkmenistan', 'United Arab Emirates', 'Uzbekistan', 'Vietnam', 'Yemen'
]

european_countries = [
    'Albania', 'Andorra', 'Austria', 'Belarus', 'Belgium', 'Bosnia and Herzegovina', 'Bulgaria', 'Croatia',
    'Cyprus', 'Czech Republic', 'Denmark', 'Estonia', 'Finland', 'France', 'Germany', 'Greece', 'Hungary',
    'Iceland', 'Ireland', 'Italy', 'Kosovo', 'Latvia', 'Liechtenstein', 'Lithuania', 'Luxembourg', 'Malta',
    'Moldova', 'Monaco', 'Montenegro', 'Netherlands', 'North Macedonia', 'Norway', 'Poland', 'Portugal',
    'Romania', 'Russia', 'San Marino', 'Serbia', 'Slovakia', 'Slovenia', 'Spain', 'Sweden', 'Switzerland',
    'Ukraine', 'United Kingdom', 'Vatican City'
]

north_american_countries = [
    'Antigua and Barbuda', 'Bahamas', 'Barbados', 'Belize', 'Canada', 'Costa Rica', 'Cuba', 'Dominica',
    'Dominican Republic', 'El Salvador', 'Grenada', 'Guatemala', 'Haiti', 'Honduras', 'Jamaica', 'Mexico',
    'Nicaragua', 'Panama', 'Saint Kitts and Nevis', 'Saint Lucia', 'Saint Vincent and the Grenadines',
    'Trinidad and Tobago', 'United States'
]

oceania_countries = [
    'Australia', 'Fiji', 'Kiribati', 'Marshall Islands', 'Micronesia', 'Nauru', 'New Zealand', 'Palau',
    'Papua New Guinea', 'Samoa', 'Solomon Islands', 'Tonga', 'Tuvalu', 'Vanuatu'
]

south_american_countries = [
    'Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia', 'Ecuador', 'Guyana', 'Paraguay', 'Peru',
    'Suriname', 'Uruguay', 'Venezuela'
]
gender = ["Male", "Female"]

degrees = ["Bachelor's", "Master's", "PhD"]

age = random.randint(25, 45)

status_options = ["Single", "In Relationship", "Married"]

interests_dictionary = {
    'Travel': ['Adventure', 'Luxury', 'Backpacking', 'Cultural', 'Nature'],
    'Food': ['Cooking', 'Baking', 'Healthy', 'Reviews', 'Experiments'],
    'Fitness': ['Gym', 'Yoga', 'Running', 'CrossFit', 'Bodybuilding'],
    'Fashion': ['Streetwear', 'Vintage', 'HighFashion', 'Sustainable', 'DIY'],
    'Technology': ['Gadgets', 'Programming', 'AI', 'Cybersecurity', 'Development'],
    'Entertainment': ['Movies', 'TVShows', 'Celebrities', 'Concerts', 'Gaming'],
    'Books': ['Fiction', 'NonFiction', 'Fantasy', 'Mystery', 'ScienceFiction'],
    'Gaming': ['VideoGames', 'BoardGames', 'Esports', 'GameReviews', 'GameDevelopment'],
    'Photography': ['Landscape', 'Portrait', 'Mobile', 'Street', 'Wildlife'],
    'Parenting': ['NewbornCare', 'ParentingTips', 'Educational', 'FamilyTravel', 'ParentingHumor'],
    'Crafts': ['DIYCrafts', 'Knitting', 'Painting', 'Pottery', 'Scrapbooking'],
    'Politics': ['PoliticalNews', 'Activism', 'PolicyAnalysis', 'GlobalAffairs', 'LocalPolitics'],
    'Music': ['Genres', 'Concerts', 'MusicReviews', 'MusicProduction', 'VinylCollecting'],
    'Pets': ['Dogs', 'Cats', 'ExoticPets', 'PetCareTips', 'PetAdoption'],
    'SelfImprovement': ['Productivity', 'Mindfulness', 'MotivationalQuotes', 'GoalSetting', 'PersonalDevelopment'],
    'Art': ['FineArts', 'StreetArt', 'DigitalArt', 'Sculpture', 'ArtExhibitions'],
    'Movies': ['Genres', 'MovieReviews', 'FilmFestivals', 'ClassicFilms', 'IndieMovies'],
    'Sports': ['Football', 'Basketball', 'Tennis', 'Running', 'ExtremeSports'],
    'Health': ['MentalHealth', 'Nutrition', 'HolisticWellness', 'FitnessChallenges', 'HealthyRecipes'],
    'Education': ['OnlineLearning', 'EducationalTechnology', 'LearningResources', 'AcademicTips', 'CareerDevelopment']
}

api_key = '3520f08cf9bb4b94b614bf7fcfb7e8bf'
base_url = 'https://newsapi.org/v2'
country_codes = ['ae', 'ar', 'at', 'au', 'be', 'bg', 'br', 'ca', 'ch', 'cn', 'co', 'cr', 'cz', 'de', 'eg', 'fr', 'gb', 'gr', 'hk', 'hu', 'id', 'ie', 'il', 'in', 'it', 'jp', 'kr', 'lt', 'lv', 'ma', 'mx', 'my', 'ng', 'nl', 'no', 'nz', 'ph', 'pl', 'pt', 'ro', 'rs', 'ru', 'sa', 'se', 'sg', 'sk', 'th', 'tr', 'tw', 'ua', 'us', 've', 'za']
categories = ['business', 'entertainment', 'general', 'health', 'science', 'sports', 'technology']
language_codes = ['en', 'es', 'fr', 'de', 'it', 'ja', 'ko', 'zh', 'ru', 'ar']


