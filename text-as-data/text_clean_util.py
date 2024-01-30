"""
Text cleaning utilities
"""

import re
import nltk


stopwords_en = nltk.corpus.stopwords.words("english")


def clean_term(term, stopwords=None):
    """
    Must be very careful cleaning terms to allow for index matching (IE, don't
    remove words or break text ordering when text indices are important).
    If stopwords given, remove them from term.
    """
    if stopwords:
        return clean_whitespace(remove_all_punctuation(
            remove_stopwords(lower_text(term), stopwords=stopwords)))
    return clean_whitespace(remove_all_punctuation(lower_text(term)))

def clean_whitespace(text):
    return " ".join(text.split())

def remove_all_punctuation(text, exceptions=None):
    """
    Does a strict remove of anything that is not a character in the Unicode
    character properties database or any whitespace char

    @param exceptions: string containing characters to leave in string. Must be
        in REGEX format as part of a character set
    """
    if exceptions is not None:
        return re.sub(r"[^\w\s{}]".format(exceptions), "", text)
    else:
        return re.sub(r"[^\w\s]", "", text)

def remove_stopwords(text, stopwords=None):
    """
    Standard way to remove stopwords from text. Text is a string. Stopwords is
    a list of strings to remove. Returns cleaned string.

    Defaults to removing NLTK: English Stopwords
    """
    if stopwords is None:
        stopwords = stopwords_en

    text = " " + text + " "
    for w in stopwords:
        text = text.replace(" {} ".format(w), u" ")
    return text.strip()
