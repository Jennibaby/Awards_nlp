import parserTwitter
import getMatchNameList


presenterFeature = [["presenter","presents","presented","presenting"]] # delete ["present"]
namesIgnoreList = ["best","name","film","television", "drama","actress","actor","woman","goldenglobes", "golden","globes", "globe","award","awards","Nominee","Nominees"]
hostFeature = [["host","hosts","hosted","hosting"]]
winnerFeature = [["wins", "won", "winning", "winner"]]
nominationFeature = [["nomination", "nominations", "nominate", "nominates","nominee","nominees","nominator","nominators"]]

# AwardFeature = {"Best Motion Picture - Drama": [["best"],["motion","picture"],["drama"]],
# "Best Motion Picture - Musical or Comedy": [["best"],["motion","picture"],["musical","comedy"]],
# "Best Performance by an Actress in a Motion Picture - Drama": [["best"],["performance"],["actress"],[""],["drama"]],
# "Best Performance by an Actor in a Motion Picture - Drama": [["best"],["performance"],["actor"],["motion","picture"],["drama"]],
# "Best Performance by an Actress in a Motion Picture - Musical or Comedy": [["best"],["performance"],["actress"],["motion","picture"],["musical","comedy"]],
# "Best Performance by an Actor in a Motion Picture - Musical or Comedy": [["best"],["performance"],["actor"],["motion","picture"],["musical","comedy"]],
# "Best Supporting Actress in a Motion Picture": [["best"],["supporting"],["actress"],["motion","picture"]],
# "Best Supporting Actor in a Motion Picture": [["best"],["supporting"],["actor"],["motion","picture"]],
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
# "Best Supporting Performance by an Actor in a Series, Miniseries or Television Film": [["best"],["supporting"],["actress"],["limited","miniseries","film"]],
# "Best Supporting Performance by an Actress iin a Series, Miniseries or Television Film": [["best"],["supporting"],["actor"],["limited","miniseries","film"]]
# }

def main():
    twitterTokensFile = "twitterTokens.txt"
    twitterLowerTokensFile = "twitterLowerTokens.txt"
    #read and tokenize gg2018.json, and then write them into to files 
    #only run once, and then comment the following line to reduce the runtime 
    #parserTwitter.getTwitterContent('gg2018.json',twitterTokensFile,twitterLowerTokensFile)

    
    (twitterTokens,twitterLowerTokens) = parserTwitter.readTwitterTokens(twitterTokensFile,twitterLowerTokensFile)
    print ("name of host")
    getMatchNameList.getHost(twitterTokens,twitterLowerTokens,hostFeature,namesIgnoreList)
    extract names of presenters
    print ("name of presenter")
    getMatchNameList.getPresenter(twitterTokens,twitterLowerTokens,presenterFeature,namesIgnoreList)
    # print ("candidates of presenter")
    # getMatchNameList.getMatchUnigramList(twitterTokens,twitterLowerTokens,presenterFeature,namesIgnoreList)
    print ("name of winner")
    getMatchNameList.getWinner(twitterTokens,twitterLowerTokens,winnerFeature,namesIgnoreList)
    print ("name of nominees")
    getMatchNameList.getWinner(twitterTokens,twitterLowerTokens,winnerFeature,nominationFeature)



if __name__ == "__main__":
    main()