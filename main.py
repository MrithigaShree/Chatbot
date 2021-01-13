import numpy as np
import nltk
from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()


def tokenize(sentence):
    # split sentence into array of words/tokens
    # a token can be a word.txt or punctuation character, or number
    return nltk.word_tokenize(sentence)


def stem(word):
    # stemming = find the root form of the word.txt
    return stemmer.stem(word.lower())


def bag_of_words(tokenized_sentence, words):
    #   return bag of words array:
    #    1 for each known word.txt that exists in the sentence, 0 otherwise
    # sentence = ['hi','how','are','you']
    # words = ['hi','hello','bye','I','thank',you]
    # bag = [1,0,0,0,0,1]

    # stem each word.txt
    sentence_words = [stem(word) for word in tokenized_sentence]
    # initialize bag with 0 for each word.txt
    bag = np.zeros(len(words), dtype=np.float32)
    for idx, w in enumerate(words):
        if w in sentence_words:
            bag[idx] = 1

    return bag
