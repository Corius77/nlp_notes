# STEMMER 
# usuwanie prefiksu/sufiksów wg ustalonej rangi
# np. boxing -> box

# LEMMATIZER
# działa na podstawie słownika i
# sieci powiązań pomiędzy słowami
# -> grupowanie słów pod względem znaczeń

from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()