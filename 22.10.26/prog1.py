import re

# METAZNAKI
# ^ - początek ciągu
# $ - koniec ciągu
# . - dowolny znak
# [abc] - pojedyncze wystąpienie każdego ze znaków w "[]"
# z? - z występuje 0 lub 1 raz 
# z* z występuje 0 lub więcej razy
# z+ z występuje 1 lub więcej razy
# [abc] (a|b|c) | - OR
# () - grupowanie
# (ab)+ -> ab, -> abab, -> ababab...
# ab+ -> ab, -> abb, -> abb...
# [A-Z] - duże litery
# [a-z] - małe litery
# [0-9] - cyfry
# [A-Za-z0-9] - \w
# \b - białe znaki
# [^A-Z] - wszystko oprócz wielkich liter 

# re.match(wzorzec, tekst, flagi) -> obiekt: info odnośnie 
# podciągu w tekst pasującego do wzorca
# re.findall(wzorzec, tekst, flagi) -> lista podciągów  

res = re.findall('H|Hobson|Cole', 'Hobson Lane, Cole Howard and Hans Max Hopke')
print(res)

res = re.match(r'(tim|sam|nam)e', 'Same time, save name', re.IGNORECASE) 
print(res)

res = re.findall(r'(tim|sam|nam)e', 'Same time, save name', re.IGNORECASE)
print(res)

res = re.match(r'(?:tim|sam|nam)e', 'Save time, save name', re.IGNORECASE)
print(res)

res = re.findall(r'(?:eas|heav)y{0,2}\.', 'Easy or heavyy.', re.IGNORECASE)
print(res)

txt = 'hello planet'

res = re.findall(r'(?:pla){1}net$', txt, re.IGNORECASE)

res = re.findall(r'(?:pla){1}net$', txt, re.IGNORECASE)
print(res)

def find_(txt):
    print(txt, re.findall(r'^(?:Hel)*lo.+net\.$', txt, re.IGNORECASE))

T = 'helhelhello planet.'
find_(T) # [T]
T = 'helloplanet.'
find_(T)
T = 'hellhel planet.'
find_(T)
T = 'lolonet.'
find_(T)
T = 'Hello planet.'
find_(T)
T = 'hellonet'
find_(T)

# Prompt zawiera: "My name is {name}" -> "Nice to meet you, {name}" 