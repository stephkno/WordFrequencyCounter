#!/usr/local/bin/python3
import wget
import re
from nltk.corpus import stopwords
import nltk
import sys
import os
# word frequency counter
# 04/09/21
#
# download specified text file and perform
# word frequency analysis, print results
#
# download nltk stopwords
#
# initialize vars
try:
    os.mkdir("books")
except:
    pass

word_frequency_dictionary = {}
n_words = 25
nltk.corpus.stopwords.ensure_loaded()
stopwords = stopwords.words('english')
stopwords.append("says")
stopwords.append("said")

if(len(sys.argv)>1):
    filename_url = sys.argv[1]
else:
    print("Please specify text file URL")
    quit()

#wget download function url -> string
def download(url):
    print("Downloading file: {}".format(url))
    file = wget.download(url, "books/{}".format(url.split('/')[-1]))
    with open(file, 'r') as x:
        text = x.read()
    return text

# get stdin
file = []

if not sys.stdin.isatty():
    for line in sys.stdin:
        file.append(line)

#determine input type and acquire text
if len(file) > 0:
    # if stdin is url
    if file[0][0:4] == "http":
        text = download(file[0])
    else:
        text = file[-1]
else:
    # no stdin, downloading default file
    text = download(filename_url)

# default the great gatsby
#
# split text into lines
title = text.splitlines()[0]
# clean text of punctuation and linebreaks
# split lines into words
text = [word.replace('\n', ' ').replace(',','').replace('.','').replace("\"","").replace("!","").replace("?","").replace("”","") for word in text.split()]

# run over each word over text
for word in text:
    # determine if word has been added to dictionary
    if word not in word_frequency_dictionary:
        word_frequency_dictionary[word.lower()]=1
    # increment count
    else:
        word_frequency_dictionary[word.lower()]+=1

# remove all stop words from dictionary
for word in stopwords:
    if word in word_frequency_dictionary:
        word_frequency_dictionary.pop(word)

# sort words by count
sorted_list = sorted(zip(word_frequency_dictionary.values(), word_frequency_dictionary.keys()))

# print stats
print("Word: Frequency")
for item in sorted_list:
    print("{}: {}".format(item[1], item[0]))

print("Word Frequency Analysis of:", title)
