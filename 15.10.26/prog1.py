import nltk
from nltk import word_tokenize

nltk.download('punkt_tab')

base = {
    # --- Powitania i small talk ---
    'Hello': 'Hi! How can I help you?',
    'Hi': 'Hello! Nice to meet you.',
    'Good morning': 'Good morning! How are you today?',
    'Good evening': 'Good evening! What would you like to know?',
    'How are you?': "I'm fine, thank you. And you?",
    "What's up?": 'Not much, just studying as usual.',
    'Nice to meet you': 'Nice to meet you too!',
    'Thank you': "You're welcome!",
    'Thanks': 'No problem!',
    'Goodbye': 'Goodbye! Have a nice day.',
    'Bye': 'See you later!',

    # --- Dane osobowe ---
    'What is your name?': 'My name is Sebastian.',
    "What's your name?": 'My name is Sebastian.',
    'Who are you?': "I'm Sebastian, a Data Analytics student.",
    'Tell me about yourself': "I'm Sebastian, I'm 22 years old and I study Data Analytics at the University of Lodz.",
    'What is your age?': '22',
    'How old are you?': "I'm 22 years old.",
    'Where are you from?': "I'm from Poland.",
    'Where do you live?': 'I live in Lodz.',
    'What languages do you speak?': 'I speak Polish and English.',

    # --- Studia ---
    'What are you studying?': 'Data Analytics',
    'What do you study?': 'Data Analytics',
    'Where are you studying?': 'At the University of Lodz',
    'Where do you study?': 'At the University of Lodz',
    'What is your degree?': 'Engineer in Data Analytics',
    'What year of studies are you in?': "I'm in my final year of engineering studies.",
    'Why did you choose Data Analytics?': 'Because I like working with data and finding patterns in it.',
    'Do you like your studies?': 'Yes, I find them very interesting.',
    'What is your favourite subject?': 'Machine learning.',
    'What is the topic of your thesis?': "I'm still working on it.",

    # --- Umiejętności ---
    'What programming languages do you know?': 'Python, SQL and R.',
    'Do you know Python?': 'Yes, Python is my main programming language.',
    'Do you know SQL?': 'Yes, I use SQL to work with databases.',
    'What tools do you use?': 'I use Python (pandas, NumPy, scikit-learn), SQL, Excel and Power BI.',
    'What is Data Analytics?': 'Data Analytics is the process of examining data to find useful information and support decision-making.',
    'What is machine learning?': 'Machine learning is a field of AI where computers learn patterns from data without being explicitly programmed.',

    # --- Praca i plany ---
    'Do you work?': "I'm currently focused on my studies, but I'm looking for an internship.",
    'What do you want to do in the future?': 'I want to work as a Data Analyst or Data Scientist.',
    'What are your plans after graduation?': "I'd like to find a job in data analysis and maybe continue with a master's degree.",

    # --- Zainteresowania ---
    'What are your hobbies?': 'I like programming, sports and watching movies.',
    'What do you do in your free time?': 'I spend time with friends, play games and learn new things.',
    'Do you like sports?': 'Yes, I like football.',
    'What is your favourite movie?': 'I like science fiction movies.',
    'What music do you like?': 'I listen to many genres, mostly pop and rock.',

    # --- O chatbocie ---
    'Are you a bot?': "I'm a simple chatbot that answers questions about Sebastian.",
    'What can you do?': 'I can answer questions about my name, age, studies, skills and hobbies.',
    'Help': 'You can ask me about my name, age, studies, skills, hobbies or plans.',
}

prompts = [prompt for prompt in base.keys()]
answers = [answer for answer in base.values()]

# prompt_user = word_tokenize('What is your name?'.lower())

# Metoda 1

def metoda1():
    prompt_user = word_tokenize(input('What is your question?\n').lower())
    cnt = []
    for prompt in prompts:
        licznik = 0
        prompt_user_ = prompt_user.copy()
        # porównujemy tokeny
        for tok1 in prompt:  
            i = 0
            while len(prompt_user_) > i:
                tok2 = prompt_user_[i]
                # print(f"tok1 = {tok1}, tok2 = {tok2}")
                # print(f"prompt1 = {prompt}, prompt2 = {prompt_user_}, i = {i}")
                # porównanie
                # usunięcie znalezionego tokena z listy `prompt`
                # liczba identycznych tokenów z `prompt` oraz `prom_tok`
                if tok1 == tok2:
                    # print(f"increse! prompt1 = {prompt}, prompt2 = {prompt_user_}, i = {i}")
                    licznik += 1
                    prompt_user_.remove(tok1)
                i += 1
        cnt.append(licznik)

    print(cnt)

    prompt_index = cnt.index(max(cnt))
    similiar_prompt = list(base.keys())[prompt_index]
    answer = base[similiar_prompt]
    print(answer)

# STEMMER 
# usuwanie prefiksu/sufiksów wg ustalonej rangi
# np. boxing -> box

# LEMMATIZER
# działa na podstawie słownika i
# sieci powiązań pomiędzy słowami
# -> grupowanie słów pod względem znaczeń

from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()
print([stemmer.stem(w) for w in word_tokenize("Adjustable formality stemming airliner")])

nltk.download('wordnet') # jednorazowe wywołanie

from nltk.stem import WordNetLemmatizer

lemmatize = WordNetLemmatizer()

# print([lemmatize.lemmatize(w) for w in word_tokenize('Adjustable formality stemming airliner')])

# STOPWORDS

from nltk.corpus import stopwords

nltk.download('stopwords')

english_stops = set(stopwords.words('english'))

words = ["Can't", 'is', "contraction"]
# print([word for word in words if word not in english_stops])

# NGRAMS
# tworzy n-krotki kolejnych tokenów
# występujących na liście

from nltk.util import ngrams

wtok = word_tokenize('wnet annoys you?')
# print(list(ngrams(wtok, 2)))

# WEKTORYZACJA
from nltk.tokenize import sent_tokenize

para = "Nice to see you. I hope it's also nice to see me. Please give me me a feedback"
pa = "A feedback is is needed"

snt = sent_tokenize(para)

from sklearn.feature_extraction.text import CountVectorizer

corpus = snt 
corpus.append(pa)
vectorizer = CountVectorizer()
# x = vectorizer.fit_transform(corpus)

# Dodać do korpusu prompty i odpowiedzi

corpus = corpus + prompts + answers
print(corpus)

x = vectorizer.fit_transform(corpus)

# PODOBIEŃSTWO COSINUSOWE
# x, y - wektory
# cos(alfa) = <x, y> / ||x|| ||y|| = SIGMA_i(x_i y_i) / [ sqrt(SIGMA_i(x_i^2)) sqrt(SIGMA_i(y_i^2)) ]

w1 = x.toarray()[1]
w2 = x.toarray()[2]
w3 = x.toarray()[3]

from math import sqrt

print(len(w1))

def calc_cos_similiarity(w1, w2):
    cosinus = w1.dot(w2) / sqrt(w1.dot(w1 * w2.dot(w2)))
    return cosinus

cosinus = calc_cos_similiarity(w1, w1)
print(f"cos = {cosinus}")