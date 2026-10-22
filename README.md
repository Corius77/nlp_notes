# NLP – Notes and Project

Notes and example code from a Natural Language Processing (NLP) course, plus a course project: a chatbot (`chatbot.py`).

Each directory named after a date (`DD.MM.YY`, e.g. `15.10.26`) contains materials from that class: code in `prog1.py` with comments describing the new tools introduced by the instructor that can be used in the project.

> **Note:** the comments and notes inside the code files are written in Polish.

## Repository structure

| Path | Contents |
|---|---|
| `08.10.26/` | First classes – a simple chatbot based on token matching |
| `15.10.26/` | Stemming, lemmatization, stopwords, n-grams, vectorization, cosine similarity |
| `22.10.26/` | Regular expressions (`re`) |
| `chatbot.py` | Project – chatbot (work in progress) |

## Class notes

### 08.10.26 – tokenization and question matching
- The knowledge base is a `question -> answer` dictionary.
- Text is tokenized with `nltk.word_tokenize` (after lowercasing).
- **Method 1** – for each question in the base, count the tokens shared with the user's question; the answer comes from the question with the highest count.

### 15.10.26 – text preprocessing and vectorization
- **Stemming** (`PorterStemmer`) – rule-based removal of prefixes/suffixes (e.g. *boxing → box*).
- **Lemmatization** (`WordNetLemmatizer`) – reducing words to their base form using a dictionary and a network of word relations.
- **Stopwords** (`nltk.corpus.stopwords`) – removing words with little informational value.
- **N-grams** (`nltk.util.ngrams`) – tuples of consecutive tokens.
- **Sentence tokenization** (`sent_tokenize`).
- **Vectorization** – `CountVectorizer` (scikit-learn), bag-of-words representation; the corpus includes the questions and answers from the knowledge base.
- **Cosine similarity** – `cos(α) = <x, y> / (‖x‖ · ‖y‖)`; the user's question is compared with the vectors of the questions in the base and the most similar one is chosen (`answer_with_cos`).
- Extended knowledge base of about 50 question–answer pairs (small talk, personal info, studies, skills, plans, interests).

### 22.10.26 – regular expressions
The `re` module and a metacharacter cheat sheet:

| Pattern | Meaning |
|---|---|
| `^`, `$` | start / end of string |
| `.` | any character |
| `[abc]`, `[^A-Z]` | one of the listed characters / any character except those |
| `[A-Z]`, `[a-z]`, `[0-9]` | character ranges |
| `z?`, `z*`, `z+` | 0 or 1, 0 or more, 1 or more occurrences |
| `(a\|b\|c)` | alternation (OR) |
| `()` | grouping, e.g. `(ab)+` |

Functions: `re.match(pattern, text, flags)` (info about the substring matching the pattern) and `re.findall(pattern, text, flags)` (list of matching substrings).

## Project: chatbot

`chatbot.py` will contain the course project, using the tools introduced in class (tokenization, text normalization, vectorization, cosine similarity, regular expressions).

> Status: work in progress.

## Requirements and usage

- Python 3.10+ (conda environment)
- Libraries: `nltk`, `scikit-learn`, `numpy`

```bash
pip install nltk scikit-learn numpy
python 15.10.26/prog1.py
```

NLTK resources (`punkt_tab`, `wordnet`, `stopwords`) are downloaded automatically on the first run of the scripts.
