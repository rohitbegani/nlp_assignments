from collections import Counter
from decimal import Decimal
from collections import defaultdict
import os
import string
import math
import re

def createDict(path, dic):
    for file in os.listdir(path):
        nOfDocs[dic] += 1
        with open(os.path.join(path, file)) as f:
            word_corpus = Counter(f.read().lower().translate(None, string.punctuation).split())
            for word in word_corpus:
                nOfTerms[dic] += 1
                if word in wordDict[dic]:
                    wordDict[dic][word] += 1
                else:
                    wordDict[dic][word] = 1

def calcProb():
    for d, dic in enumerate(wordDict):
        for k, v in dic.items():
            if k not in probDoc:
                probDoc[k] = {0: 0, 1: 0}
                probDoc[k][1-d] = math.log(Decimal(alpha)/(nOfTerms[d]+alpha*len(wordDict[d])))
            probDoc[k][d] = math.log(Decimal(v+alpha)/(nOfTerms[d]+alpha*len(wordDict[d])))

######## TEST

def createTestDict(path, type):
    for file in os.listdir(path):
        with open(os.path.join(path, file)) as f:
            test_corpus = Counter(f.read().lower().translate(None, string.punctuation).split())
            c = classify(test_corpus)
            # print c
            # print c
            res[type][c] += 1
            # print res[type][c]
    return res

def classify(corpus):
    prob1 = math.log(Decimal(nOfDocs[0])) - math.log(nOfDocs[0] + nOfDocs[1])
    prob2 = math.log(Decimal(nOfDocs[1])) - math.log(nOfDocs[0] + nOfDocs[1])
    prob = Decimal(prob1 - prob2)

    for word in corpus:
        if word in probDoc:
            c1 = Decimal(probDoc[word][0])
            c2 = Decimal(probDoc[word][1])
            prob = prob + c1 - c2
    return (0 if prob>0 else 1)

## Recall, Precision and F1

def calculate_scores(res):
    # print res
    precision_pos = precision(res, 1)
    recall_pos = recall(res, 1)
    f1_pos = f1score(precision_pos, recall_pos)

    precision_neg = precision(res, 0)
    recall_neg = recall(res, 0)
    f1_neg = f1score(precision_neg, recall_neg)

    return precision_pos, recall_pos, f1_pos, precision_neg, recall_neg, f1_neg

def precision(res, c):
    return Decimal(res[c][c])/(Decimal(res[c][c]) + Decimal(res[1-c][c]))

def recall(res, c):
    return Decimal(res[c][c])/(Decimal(res[c][c]) + Decimal(res[c][1-c]))

def f1score(p, r):
    return (2*p*r)/(p+r)



if __name__ == '__main__':
    positive_path = 'train/pos/'
    negative_path = 'train/neg/'
    positive_test_path = 'test/pos/'
    negative_test_path = 'test/neg/'
    posWordCount = 0
    negWordCount = 0
    posDocs = 0
    negDocs = 0
    posWordDict = {}
    negWordDict = {}
    posProb = {}
    negProb = {}
    nOfTerms = [0, 0]
    nOfDocs = [0, 0]
    probDoc = {}
    alpha = 1

    res = [[0, 0], [0, 0]]

    posRes = [0, 0]
    negRes = [0, 0]
    wordDict = [{}, {}]

    createDict(positive_path, 1)
    createDict(negative_path, 0)
    calcProb()

    createTestDict(positive_test_path, 1)
    createTestDict(negative_test_path, 0)

    precision_pos, recall_pos, f1_pos, precision_neg, recall_neg, f1_neg = calculate_scores(res)

    print "positive"
    print precision_pos
    print recall_pos
    print f1_pos

    print "negative"
    print precision_neg
    print recall_neg
    print f1_neg
