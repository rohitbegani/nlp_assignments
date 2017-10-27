from collections import Counter
from decimal import Decimal
from collections import defaultdict
import os
import string
import math

def createDict(path, type):
    if type == 'pos':
        wordCount, wordDict = posWordCount, posWordDict
    else:
        wordCount, wordDict = negWordCount, negWordDict

    for file in os.listdir(positive_path):
        with open(os.path.join(positive_path, file)) as f:
            word_corpus = Counter(f.read().lower().translate(None, string.punctuation).split())
            for word in word_corpus:
                wordCount += 1
                if word in wordDict:
                    wordDict[word] += 1
                else:
                    wordDict[word] = 1

def calcProb(type):
    if type == 'pos':
        wordDict, wordCount = posWordDict, posWordCount
    else:
        wordDict, wordCount = negWordDict, negWordCount

    for i, j in wordDict.items():
        if i not in prob:
            prob[i] = math.log(Decimal(0.1)) - math.log(wordCount + 0.1 * len(wordDict))

if __name__ == '__main__':
    positive_path = 'train/pos/'
    negative_path = 'train/neg/'
    posWordCount = 0
    negWordCount = 0
    posWordDict = {}
    negWordDict = {}
    prob = {}

    createDict(positive_path, 'pos')
    createDict(negative_path, 'neg')
    calcProb('pos')
    calcProb('neg')
    print prob
