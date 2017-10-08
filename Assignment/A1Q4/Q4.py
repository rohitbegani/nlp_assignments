import json
import os.path

def tokenize(file):
    train_dict = {}

    train_dict["UNK"] = {}
    train_dict["unigram"] = {}
    train_dict["bigram"] = {}
    train_dict["trigram"] = {}

    with open(file, mode='r') as f:
        for line in f.readlines():
            key = line.split()
            freq = int(key[0])

            if key[1].startswith("WORDTAG"):

                if key[3].strip() not in train_dict:
                    train_dict[key[3].strip()] = {key[2].strip(): freq}

                else:
                    train_dict[key[3].strip()].update({key[3].strip(): freq})

                # if key[2].st

            elif key[1].startswith("1-GRAM"):
                train_dict["unigram"][key[2].strip()] = freq
            elif key[1].startswith("2-GRAM"):
                train_dict["bigram"][key[2].strip()] = freq
            elif key[1].startswith("3-GRAM"):
                train_dict["trigram"][key[2].strip()] = freq

        return train_dict

def readTestfile(testfile):

    test_sentences = []
    sentence = []
    with open(testfile) as test:
        for word in test.readlines():
            if word.strip():
                sentence.append(word.strip())
            else:
                test_sentences.append(" ".join(sentence))
                sentence = []

    return test_sentences

def content_to_sentences(file):
    content = []
    single_sentence = []

    with open(file) as f:
        for word in f.readlines():
            if word.strip():
                single_sentence.append(word.strip())
            else:
                content.append(" ".join(single_sentence))
                single_sentence = []

    return content

def viterbi_algorithm(sentence):


if __name__ == '__main__':

    if not os.path.isfile("train_counts.json"):
        print "Converting train.counts into json format for ease of access...."
        convertJSON('train.counts')

    if os.path.isfile("predicted_tags.txt"):
        os.remove("predicted_tags.txt")

    with open("train_counts.json", 'r') as f:
        trainData = json.load(f)

    tokenized_data = tokenize('train.counts')
    sentence_corpus = content_to_sentences('test.words')

    for sentence in sentence_corpus:
        viterbi_algorithm(sentence)


    testSentences = readTestfile('test.words')

    tags = trainData["unigram"].keys()

    for sentence in testSentences:
        viterbi_algorithm(sentence)
