import parserTwitter
import getMatchNameList

presenterFeature = [["presenter"], ["presents"], ["present"], ["presented"], ["presenting"]] # delete ["present"]
presenterIgnoreList = ["best","name","film","television", "drama","actress","actor","woman","goldenglobes", "golden","globes", "globe","award","awards"]
hostFeature = [["host"],["hosts"],["hosted"],["hosting"]]
winnerFeature = [["wins"], ["won"], ["winning"], ["winner"]]

def main():
    twitterTokensFile = "twitterTokens.txt"
    twitterLowerTokensFile = "twitterLowerTokens.txt"
    #read and tokenize gg2018.json, and then write them into to files 
    #only run once, and then comment the following line to reduce the runtime 
    parserTwitter.getTwitterContent('gg2018.json',twitterTokensFile,twitterLowerTokensFile)

    
    (twitterTokens,twitterLowerTokens) = parserTwitter.readTwitterTokens(twitterTokensFile,twitterLowerTokensFile)
    # extract names of presenters
    print ("name of presenter")
    getMatchNameList.getMatchUnigramList(twitterTokens,twitterLowerTokens,presenterFeature,presenterIgnoreList)
    print ("name of host")
    getMatchNameList.getMatchUnigramList(twitterTokens,twitterLowerTokens,hostFeature,presenterIgnoreList)

if __name__ == "__main__":
    main()