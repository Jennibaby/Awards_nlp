import nltk
from nltk.tag import pos_tag
from collections import defaultdict
import re


''' Read in all twitter data and sort data by co-appearance of bigrams with list of tags'''
def get_bigram_list_match_tweets(tweets, words_to_match):
    d = defaultdict(int)
    for idx in range(0, len(tweets)):
        if match_all_words(tweets[idx], words_to_match):
            tagged_tweet = pos_tag(tweets[idx][0].split())
            proper_nouns = [pn.lower() for pn,pos in tagged_tweet if pos == 'NNP']
            bigramsList = list(nltk.bigrams(proper_nouns))

            for j in range(0, len(bigramsList)):
                token = bigramsList[j][0]+" "+bigramsList[j][1]
                d[token] += 1

    for key in ignore_list:
        for dKey in d.keys():
            if key in dKey:
                del d[dKey]

    sorted_vals = sorted(d.iteritems(), key =lambda (k,v): v, reverse=True)
    return sorted_vals

''' Read in all twitter data and sort data by co-appearance with list of tags'''
def get_list_match_tweets(tweets, words_to_match):
    d = defaultdict(int)
    for idx in range(0,len(tweets)):
        if match_all_words(tweets[idx], words_to_match):
            tagged_tweet = pos_tag(tweets[idx][0].split())
            proper_nouns = [pn.lower() for pn,pos in tagged_tweet if pos == 'NNP']
            for pnoun in proper_nouns:
                d[pnoun] += 1
    for key in ignore_list:
        if key in d.keys():
            del d[key]
    pos_hosts = sorted(d.iteritems(), key =lambda (k,v): v, reverse=True)
    return pos_hosts

def match_all_words(tweet, words_to_match):
    for word in words_to_match:
        if not findWholeWord(word)(tweet):
            return False
    return True

