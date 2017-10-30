from collections import Counter
from decimal import Decimal
from collections import defaultdict
import os
import string
import math

def createDict(path, type):
    docs = 0
    wordCount = 0
    wordDict = {}
    for file in os.listdir(positive_path):
        docs += 1
        with open(os.path.join(positive_path, file)) as f:
            word_corpus = Counter(f.read().lower().translate(None, string.punctuation).split())
            for word in word_corpus:
                wordCount += 1
                if word in wordDict:
                    wordDict[word] += 1
                else:
                    wordDict[word] = 1
    return wordCount, wordDict, docs

def calcProb(type, wordCount, wordDict):
    global probDoc
    probDoc = {}
    alpha = 1
    for k, v in wordDict.items():
        probDoc[k] = math.log(Decimal(v+alpha)/(wordCount+alpha*len(wordDict)))
        # if i not in posProb:
        #     prob[i] = math.log(Decimal(0.1)) - math.log(wordCount + 0.1 * len(wordDict))
    return probDoc

######## TEST

def createTestDict(path, type):
    for file in os.listdir(path):
        with open(os.path.join(path, file)) as f:
            test_corpus = Counter(f.read().lower().translate(None, string.punctuation).split())
            c = classify(test_corpus)
            print c
            res[type][c] += 1
            print res[type][c]
    return res

def classify(corpus):
    c1, c2 = 0, 0
    prob1 = math.log(Decimal(posDocs)/(posDocs + negDocs))
    prob2 = math.log(Decimal(negDocs)/(negDocs + posDocs))
    prob = Decimal(prob1 - prob2)

    for word in corpus:
        if word in posProb or word in negProb:
            c1 = Decimal(posProb[word])
            c2 = Decimal(negProb[word])
        prob = prob + c1 - c2
        print prob
    return (0 if prob>1 else 1)


## Recall, Precision and F1

# def precision(res, c): return (res[c][c])/(res[c][c]+res[1-c][c])
#
# def recall(res, c): return (res[c][c])/(res[c][c]+res[c][1-c])
#
# def Fscore(p, r): return (2*p*r)/(p+r)
#
# def calculate_scores():
#     precision_pos = precision(posRes, negRes)
#     recall_pos = recall(posRes, negRes)
#     f1_pos = F1score(precision_pos, recall_pos)
#
#     precision_neg = precision(negRes, posRes)
#     recall_neg = recall(negRes, PosRes)
#     f1_neg = F1score(precision_neg, recall_neg)
#
# def precision(inFocus, alter):
#     return (inFocus/(inFocus + Alter))
#
# def recall(inFocus, alter):
#     return ()



if __name__ == '__main__':
    print "In main of train"
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

    res = [[0, 0], [0, 0]]

    posRes = [0, 0]
    negRes = [0, 0]

    posWordCount, posWordDict, posDocs = createDict(positive_path, 'pos')
    negWordCount, negWordDict, negDocs = createDict(negative_path, 'neg')

    posProb = calcProb('pos', posWordCount, posWordDict)
    negProb = calcProb('neg', negWordCount, negWordDict)

    createTestDict(positive_test_path, 0)
    createTestDict(negative_test_path, 1)

    # calculate_scores()
