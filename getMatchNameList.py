#-*- coding: utf-8 -*-
import parserTwitter
import re
import nltk # says that it is not installed but program ran correctly

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
                        print (twitters[idx])
                        j = j + 1
                        UnigramsListMethod2.append(name[:-1])
                    name = ''
                person = []
            #if j > 100:
            #    break
    #print (i)
    print (j)
    return UnigramsListMethod2

# return presenterDict - key is the name of award
def getPresenter(twitters, twittersLower, featureList,ignoreList):
    PresenterDict = {}
    j = 0
    for idx in range(0, len(twitters)):
        if isMatchFeature(twittersLower[idx], featureList):
            (award,isPerson) = classifyAwards(twittersLower[idx])
            if award == "":
                continue
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
                    if not notConsistIgnoreList(name[:-1],ignoreList):
                        continue
                    
                    if award not in PresenterDict:
                        PresenterDict[award] = {} 
                        PresenterDict[award][name[:-1]] = 1
                        #print ("humanname:%s" % name[:-1])
                        j = j + 1
                    elif name[:-1] not in PresenterDict[award]:
                        PresenterDict[award][name[:-1]] = 1
                        #print ("humanname:%s" % name[:-1])
                        #print (twitters[idx])   
                        j = j + 1      
                    else:
                        PresenterDict[award][name[:-1]] = PresenterDict[award][name[:-1]] + 1

                    name = ''
                person = []

    print (j)
    print (PresenterDict)
    return PresenterDict

# AwardFeature = {"Best Motion Picture - Drama": [["best"],["motion","picture"],["drama"]],
# "Best Motion Picture - Musical or Comedy": [["best"],["motion","picture"],["musical","comedy"]],
# "Best Performance by an Actress in a Motion Picture - Drama": [["best"],["performance"],["actress"],[""],["drama"]],
# "Best Performance by an Actor in a Motion Picture - Drama": [["best"],["performance"],["actor"],["motion","picture"],["drama"]],
# "Best Performance by an Actress in a Motion Picture - Musical or Comedy": [["best"],["performance"],["actress"],["motion","picture"],["musical","comedy"]],
# "Best Performance by an Actor in a Motion Picture - Musical or Comedy": [["best"],["performance"],["actor"],["motion","picture"],["musical","comedy"]],
# "Best Supporting Performance Actress in a Motion Picture": [["best"],["supporting"],["actress"],["motion","picture"]],
# "Best Supporting Performance Actor in a Motion Picture": [["best"],["supporting"],["actor"],["motion","picture"]],
# "Best Director": [["best","director"]],
# "Best Screenplay":[["best","screenplay"]]
# "Best Original Score": [["best","orginal","score"]],
# "Best Original Song": [["best"],["orginal"],"song"],
# "Best Animated Feature Film": [["best"],["animated","animation"],["film"]],
# "Best Foreign Language Film": [["best"],["foreign"],["language"],["film"]],

# "Best TV series - Drama": [["best"],["series"],["drama"]],
# "Best TV series - Musical or Comedy": [["best"],["series"],["musical","comedy"]],
# "Best Performance by an Actress in a TV Series - Drama": [["best"],["performance"],["actress"],["series"],["drama"]],
# "Best Performance by an Actor in a TV Series - Drama": [["best"],["performance"],["actor"],["series"],["drama"]],
# "Best performance by an Actress in a TV series - Musical or Comedy": [["best"],["performance"],["actress"],["series"],["musical","comedy"]],
# "Best Performance by an Actor in a TV series - Musical or Comedy": [["best"],["performance"],["actor"],["series"],["musical","comedy"]],
# "Best Miniseries or Television Film": [["best"],["limited","miniseries","film"]],
# "Best Performance by an Actress in a Miniseries or Television Film": [["best"],["actress"],["limited","miniseries","film"]],
# "Best Performance by an Actor in a Miniseries or Television Film": [["best"],["actor"],["limited","miniseries","film"]],
# "Best Supporting Performance by an Actress in a Series, Miniseries or Television Film": [["best"],["supporting"],["actress"],["limited","miniseries","film"]],
# "Best Supporting Performance by an Actor iin a Series, Miniseries or Television Film": [["best"],["supporting"],["actor"],["limited","miniseries","film"]]
# }
def classifyAwards(twittertokens):
    # if "best" not in twittertokens:
    #     return "",False

    if "director" in twittertokens:
        return "Best Director",True

    if "screenplay" in twittertokens:
        return "Best Screenplay",False

    if "score" in twittertokens:
        return "Best Original Score",False

    if "song" in twittertokens:
        return "Best Original Song",False

    if "film" in twittertokens:
        if "animated" in twittertokens or "animation" in twittertokens:
            return "Best Animated Feature Film",False
        if "foreign" in twittertokens and "language" in twittertokens:
            return "Best Foreign Language Film",False

    isActor = False
    if "actor" in twittertokens:
        isActor = True

    isActress = False
    if "actress" in twittertokens:
        isActress = True
    
    isPerformance = True
    # if "performance" in twittertokens:
    #     isPerformance = True

    isSupporting = False
    if "supporting" in twittertokens:
        isSupporting = True
    
    isDrama = False
    if "drama" in twittertokens:
        isDrama = True


    isMusicalOrComedy = False
    if "musical" in twittertokens or "comedy" in twittertokens:
        isMusicalOrComedy = True

    isLimited = False
    if "limited" in twittertokens or "miniseries" in twittertokens or "film" in twittertokens:
        isLimited = True

    isSeries = False
    if "tv" in twittertokens or "television" in twittertokens or "series" in twittertokens:
        isSeries = True

    isMotionPicture = False
    if "motion" in twittertokens or "picture" in twittertokens:
        isMotionPicture = True

    if isActor:
        if isMotionPicture:
            if isSupporting:
                return "Best Supporting Performance Actor in a Motion Picture",True
            elif isPerformance:
                if isDrama:
                    return "Best Performance by an Actor in a Motion Picture - Drama",True
                if isMusicalOrComedy:
                    return "Best Performance by an Actor in a Motion Picture - Musical or Comedy",True
            
        if isSeries:
            if isSupporting:
                return "Best Supporting Performance by an Actor in a Series, Miniseries or Television Film",True
            elif isPerformance:
                if isDrama:
                    return "Best Performance by an Actor in a TV Series - Drama",True
                if isMusicalOrComedy:
                    return "Best Performance by an Actor in a TV series - Musical or Comedy",True
                if isLimited:
                    return "Best Performance by an Actor in a Miniseries or Television Film",True
                

    if isActress:
        if isMotionPicture:
            if isSupporting:
                return "Best Supporting Performance Actress in a Motion Picture",True
            elif isPerformance:
                if isDrama:
                    return "Best Performance by an Actress in a Motion Picture - Drama",True
                if isMusicalOrComedy:
                    return "Best Performance by an Actress in a Motion Picture - Musical or Comedy",True
            
        if isSeries:
            if isSupporting:
                return "Best Supporting Performance by an Actress in a Series, Miniseries or Television Film",True
            elif isPerformance:
                if isDrama:
                    return "Best Performance by an Actress in a TV Series - Drama",True
                if isMusicalOrComedy:
                    return "Best Performance by an Actress in a TV series - Musical or Comedy",True
                if isLimited:
                    return "Best Performance by an Actress in a Miniseries or Television Film",True
    
    if isMotionPicture:
        if isDrama:
            return "Best Motion Picture - Drama",False
        if isMusicalOrComedy:
            return "Best Motion Picture - Musical or Comedy",False
        
    if isSeries:
        if isDrama:
            return "Best TV series - Drama",False
        if isMusicalOrComedy:
            return "Best TV series - Drama",False
        if isLimited:
            return "Best Miniseries or Television Film",False

    return "",False

# temptokens = ['3', '.', 'tv', 'comedy', 'actress', 'â', 'presented', 'by', 'Jennifer', 'Aniston', ',', 'Carol', 'Burnett', '4', '.', 'TV', 'drama', 'actress', 'â', 'presented', 'by', 'Jennifer', 'Aniston', ',', 'â¦']
# print (classifyAwards(temptokens))


def getHost(twitters, twittersLower, featureList,ignoreList):

    HostDict = {}
    j = 0
    for idx in range(0, len(twitters)):
        if isMatchFeature(twittersLower[idx], featureList):
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
                    if not notConsistIgnoreList(name[:-1],ignoreList):
                        continue
                    
                    if name[:-1] not in HostDict:
                        HostDict[name[:-1]] = 1
                        #print ("humanname:%s" % name[:-1])
                        #print (twitters[idx])   
                        j = j + 1      
                    else:
                        HostDict[name[:-1]] = HostDict[name[:-1]] + 1
                        
                    name = ''
                person = []

    L = sorted(HostDict.items(), key=lambda x: x[1], reverse = True)
    print (L[0][0])
    
    return L[0][0]


def isMatchFeature(twittertokens,featureList):
    #print (twittertokens)
    for fea in featureList:
        res = False
        #print (fea)
        for f in fea:
            #p = re.compile(f,re.I)
            #print (p.findall(twitter))
            if f in twittertokens:
                res = True
                break
        if not res:
            return False
    return True



def notConsistIgnoreList(name,ignoreList):
    names = name.split(" ")
    for n in names:
        if n.lower() in ignoreList:
            return False
    return True

# return winnerDict - key is the name of award
def getWinner(twitters, twittersLower, featureList,ignoreList):
    winnerDict = {}
    j = 0
    for idx in range(0, len(twitters)):
        if isMatchFeature(twittersLower[idx], featureList):
            (award,isPerson) = classifyAwards(twittersLower[idx])
            if award == "":
                continue
            #second method to extract name
            pos = nltk.pos_tag(twitters[idx])
            sentt = nltk.ne_chunk(pos, binary = False)
            person = []
            name = ""
        
            for subtree in sentt.subtrees():
                if isPerson:
                    if subtree.label() != 'PERSON':
                        continue

                else:
                    continue


                for leaf in subtree.leaves():
                    person.append(leaf[0])
                if len(person) > 1: #avoid grabbing lone surnames
                    for part in person:
                        name += part + ' '

                    if not notConsistIgnoreList(name[:-1],ignoreList):
                        continue
                    
                    if award not in winnerDict:
                        winnerDict[award] = {} 
                        winnerDict[award][name[:-1]] = 1
                        #print ("humanname:%s" % name[:-1])
                        # print (twitters[idx]) 
                        j = j + 1
                    elif name[:-1] not in winnerDict[award]:
                        winnerDict[award][name[:-1]] = 1
                        #print ("humanname:%s" % name[:-1])
                        # print (twitters[idx])   
                        j = j + 1      
                    else:
                        # print (twitters[idx]) 
                        winnerDict[award][name[:-1]] = winnerDict[award][name[:-1]] + 1

                    name = ''
                person = []

    print (j)
    print (winnerDict)
    return winnerDict  


#winnerFeature = [["wins", "won", "winning", "winner"]]
#nominationFeature = [["nomination", "nominations", "nominate", "nominates","nominee","nominees","nominator","nominators"]]

    # def extractNameOfProduct(twittertokens):
    #     xxx wins/won/winning/winner xxx
        
    #     return name 

    # (1) xxx xxx won xxx drama xxx  
    # (2) 


