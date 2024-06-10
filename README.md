# py-sandbox
Python sample and scratch code

## [Project W Hierarchy](./hierarchy)

Code for visualizing and working with the Project W Categories Hierarchy (aka "taxonomy")


## [Assurance Fund Sandbox](./assurance-fund)

Code for Project W engagement with the Water Quality Assurance Fund (@Aquaya)

Mostly exploratory notebooks.

## [Text-as-data](./text-as-data)

Utilities for and examples of treating text as data:
- Tokenizing
- Cleaning
- Vectorizing
- Topic modeling
- ... etc ...

Packages:
- scikit-learn
- gensim
- nltk

`text_clean.py`
Contains manual implementations of many text / string cleaning methods, including translation dictionaries
for punctuation, contractions, etc. Only English language.

`text_clean_util.py`
Less manual, more efficient text cleaning utilities. Focuses on non-unicode character removal and stopword
removal. Features and example of importing NLTK's stopword corpus.

`text_tokenize_util.py`
Features an example of importing and using NLTK's English language tokenizers. Provides manual functions (implemented
better in existing packages now) for NGRAM creation, token generation, and multi-level tokenization (eg: 
sentence > sub-sentence)

`text_vector_similarity.ipynb`
A jupyter notebook demoing scitkit-learn's text vectorization tools (Count and TfIdf) and various appropriate /
inappropriate metrics for measuring text vector similarity (euclidean distance, cosine distance)
