import parserTwitter
import re
import nltk

#presenterFeature = [["presenter"], ["presents"], ["present"], ["presented"], ["presenting"]]

# I use two methods to extract name, and find the second method is better
#ignoreList = ["â","golden","globe","awards","goldenglobes","ne"]
def getMatchUnigramList(twitters, twittersLower, featureList,ignoreList):
    #d = defaultdict(int)
    UnigramsListMethod1 = []
    UnigramsListMethod2 = []
    NameDict = {}
    i  = 0
    j = 0
    for idx in range(0, len(twitters)):
        if isMatchFeature(twittersLower[idx], featureList):

            # first method to extract name
            # taggedTwitter = nltk.pos_tag(twitters[idx])
            # name_last_index = -10
            # name_cur_index = 0
            # for pn,pos in taggedTwitter:
            #     if pos == 'NNP' and pn.lower() not in ignoreList:
            #         if name_cur_index - 1 == name_last_index:
            #             pn = UnigramsListMethod1.pop() + " " + pn
            #         UnigramsListMethod1.append(pn)
            #         name_last_index = name_cur_index

            #         print ("NNP :%s" % pn)
            #         i = i + 1

            #     name_cur_index = name_cur_index + 1

            #second method to extract name
            pos = nltk.pos_tag(twitters[idx])
            sentt = nltk.ne_chunk(pos, binary = False)
            person = []
            name = ""
            for subtree in sentt.subtrees(filter=lambda t: t.label() == 'PERSON'):
                for leaf in subtree.leaves():
                    person.append(leaf[0])
                if len(person) > 1: #avoid grabbing lone surnames
                    for part in person:
                        name += part + ' '
                    if name[:-1] not in UnigramsListMethod2 and notConsistIgnoreList(name[:-1],ignoreList):
                        print ("humanname:%s" % name[:-1])
                        j = j + 1
                        UnigramsListMethod2.append(name[:-1])
                    name = ''
                person = []
            #if j > 100:
            #    break
    #print (i)
    print (j)
    return UnigramsListMethod2


def isMatchFeature(twittertokens,featureList):
    #print (twittertokens)
    for fea in featureList:
        res = True
        #print (fea)
        for f in fea:
            #p = re.compile(f,re.I)
            #print (p.findall(twitter))
            if f not in twittertokens:
                res = False
                break
        if res:
            return True
    return False

def notConsistIgnoreList(name,ignoreList):
    names = name.split(" ")
    for n in names:
        if n.lower() in ignoreList:
            return False
    return True
    
    