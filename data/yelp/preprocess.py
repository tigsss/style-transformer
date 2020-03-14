import sys
import nltk

file_names = ["dev.neg", "reference.pos", "test.pos", "train.pos", "dev.pos", "reference.neg", "test.neg", "train.neg"]

for name in file_names:
    fp = open('./' + name, 'r')
    line = fp.readline()
    while line:
        for sentence in nltk.sent_tokenize(line):
            with open("merged_file.arpa", "a") as text_file:
                text_file.write(' '.join(nltk.word_tokenize(sentence)).lower())   
        line = fp.readline()
