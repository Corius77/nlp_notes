import nltk
from nltk import word_tokenize

nltk.download('punkt_tab')

base = {'What is your name?': 'My name is Sebastian.',
           'What is your age?': '22',
           'How old are you?': "I'm 22 years old.",
           'What do you studying?': 'Data Analytics',
           'Where do you studying?': 'At University Of Lodz',
           'What is your degree?': 'Engineer at Data Analytics'}

prompts = [word_tokenize(prompt.lower()) for prompt in base.keys()]

prompt_user = word_tokenize(input('What is your question?\n').lower())
# prompt_user = word_tokenize('What is your name?'.lower())

# Metoda 1

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