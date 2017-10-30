import naive_bayes_train
import os
from collections import Counter
from decimal import Decimal
import string
import math

def createDict(path, type):
    if type == 'pos':
        count, wordDict = posCount, posWordDict
    else:
        count, wordDict = negCount, negWordDict

    for file in os.listdir(positive_path):
        with open(os.path.join(positive_path, file)) as f:
            word_corpus = Counter(f.read().lower().translate(None, string.punctuation).split())
            c = classify(word_corpus)
            count[c] += 1

def classify(corpus):
    prob1 = math.log(Decimal(naive_bayes_train.posDocs)/math.log(naive_bayes_train.posDocs + naive_bayes_train.negDocs))
    prob2 = math.log(Decimal(naive_bayes_train.negDocs)/math.log(naive_bayes_train.negDocs + naive_bayes_train.posDocs))
    prob = Decimal(prob1 - prob2)

    for word in corpus:
        if w in naive_bayes_train.posProb:
            c1 = Decimal(naive_bayes_train.posProb[w])
        elif w in naive_bayes_train.negProb:
            c2 = Decimal(naive_bayes_train.negProb[w])
        prob = prob + c1 - c2
        print prob
    return (0 if prob>1 else 1)


if __name__ == '__main__':
    positive_path = 'test/pos/'
    negative_path = 'test/neg/'
    posCount = 0
    negCount = 0
    posWordDict = {}
    negWordDict = {}
    posDoc = {}
    negDoc = {}

    createDict(positive_path, 'pos')
    createDict(negative_path, 'neg')
    calcProb('pos')
    calcProb('neg')
