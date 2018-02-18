import json
import numpy
import nltk
import pickle

GG_tweet_id = "18667907"                      #@goldenglobes 

def readTwitterContent(file):
    #with open('gg2018.json') as f:
    with open(file) as f:
        #content = f.readlines()
        content = json.load(f)

    return content

# def filterById(twitterlist):
#     twitter = []
#     for i in range(0,len(twitterlist)):
#         id = twitterlist[i]["id_str"]
#         if id != GG_tweet_id:
#             continue
#         #text = twitterlist[i]["text"]
#         twitter.append(twitterlist[i])
#     print (len(twitter))
#     return twitter


# def correctAmpersands(tweet):
#     if "&amp;" in tweet:
#         return tweet.replace("&amp;","&")
#     return tweet


def cutRT(twitter_word_list):
    if (twitter_word_list[0:2]==["RT", "@"]):
        #print (twitter_word_list)
        #print (twitter_word_list[4:])
        return twitter_word_list[4:]
    return twitter_word_list


# def segmentAndRemoveStopWord(twitterlist): 
#     print (len(twitterlist)) 
#     #D = {};
#     twitter = []
#     #for i in range(0,len(twitterlist)):
#     for i in range(0,min(10,len(twitterlist))):
#         text = twitterlist[i]["text"]
#         words = text.split(" ")
#         twitter.append(words)
#         print (text)
#         print ("\n")



def getTwitterContent(file,twitterTokensFile,twitterLowerTokensFile):
    twitterlist = readTwitterContent(file)
    #twitterlist = parserTwitter.filterById(twitterlist)
    twitterTokens = []
    twitterLowerTokens = []
    #print (len(twitterlist))
    #for i in range (0,200):
    for i in range (0,len(twitterlist)):
        text = twitterlist[i]["text"]
        #text = correctAmpersands(text)
        #print (text)
        #word_list = nltk.word_tokenize(text)
        tokensList = nltk.tokenize.word_tokenize(text)
        twitterTokens.append(cutRT(tokensList))
        #twitterTokens.append(tokensList)
        tokensList = nltk.tokenize.word_tokenize(text.lower())
        twitterLowerTokens.append(cutRT(tokensList))
        #twitterLowerTokens.append(tokensList)

    pickle.dump(twitterTokens, open(twitterTokensFile, "wb"))
    pickle.dump(twitterLowerTokens, open(twitterLowerTokensFile, "wb"))
    return twitterTokens,twitterLowerTokens

def readTwitterTokens(twitterTokensFile,twitterLowerTokensFile):
    twitterTokens = pickle.load(open(twitterTokensFile, "rb"))
    twitterLowerTokens = pickle.load(open(twitterLowerTokensFile, "rb"))
    return twitterTokens,twitterLowerTokens







