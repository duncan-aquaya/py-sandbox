"""
Text tokenization utilities
"""

import re
import nltk
import logging
from itertools import islice
from collections import OrderedDict

_logger = logging.getLogger(__name__)

tokenizer = nltk.tokenize.WhitespaceTokenizer()

def ngramize(text, nrange=None, sep="_"):
    """
    Returns list of separated tokens and Ngrams. If n is None, 
    set to (1,2)

    @param text   - <str> Text to ngramize
    @param nrange - <Tuple> (low, high) range of N grams to compute
    @param sep    - <str> String to join NGrams with
    """
    if nrange is None:
        nrange = (1, 2)
    tokens = tokenize_text(text)
    grams = []
    for n in range(nrange[0], nrange[-1] + 1):
        grams += [sep.join(gram) for gram in window(tokens, n)]
    return grams

def tokenize_text(text):
    """
    Returns whitespace-separated list of tokens
    """
    return text.split()

def sentence_tokenize(text):
    """
    Returns list of sentence extracted from text and list of start indexes of
    each sentence
    """
    sents = nltk.tokenize.sent_tokenize(text)
    start_indexes = []
    prior_index = 0
    for s in sents:
        s_index = text.index(s, prior_index)
        start_indexes.append(s_index)
        prior_index = s_index
    return sents, start_indexes

def subsentence_tokenize(text):
    """
    Given text, returns a list of "subsentences" - tokenizes base sentences,
    then further tokenizes each sentence with breaks on other characters and
    separation indicators (eg: semicolons, list indicators, etc).

    Tokenization defined as custom within function
    """
    split_pat = r"(\s\([a-zA-Z0-9]{1,3}\)\s)|;"
    remove = ["and", "or"]
    
    subsentences = []
    start_indexes = []

    previous_start = 0
    for m in re.finditer(split_pat, text, flags=re.I):
        ss = text[previous_start:m.start()].strip()
        if ss and not ss.isspace() and ss not in remove:
            subsentences.append(ss)
            start_indexes.append(previous_start)
        previous_start = m.end()
    subsentences.append(text[previous_start:])
    start_indexes.append(previous_start)
    return subsentences, start_indexes

def generate_token_sets(text, size=3):
    """
    From text, generate all (overlapping) sets of given size. Yields triples:
        (
            <tuple of len=size> token set,
            <int>start index of set,
            <int> end index of set
        )
    """
    token_spans = zip(tokenizer.tokenize(text), tokenizer.span_tokenize(text))
    for s in window(token_spans, n=size):
        tokens = tuple([t[0] for t in s])
        start = s[0][1][0]
        end = s[-1][1][1]
        yield (tokens, start, end)

def window(seq, n=2):
    """
    Returns a sliding window (of width n) over data from the iterable
        s -> (s0,s1,...s[n-1]), (s1,s2,...,sn), ...
    """
    it = iter(seq)
    result = tuple(islice(it, n))
    if len(result) == n:
        yield result    
    for elem in it:
        result = result[1:] + (elem,)
        yield result