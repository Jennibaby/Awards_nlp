import parserTwitter
import getMatchNameList

presenterFeature = [["presenter"], ["presents"], ["present"], ["presented"], ["presenting"]] # delete ["present"]
hostFeature = ["host","hosts","hosted","hosting"]

def main():
    twitterTokensFile = "twitterTokens.txt"
    twitterLowerTokensFile = "twitterLowerTokens.txt"
    #read and tokenize gg2018.json, and then write them into to files 
    #only run once, and then comment the following line to reduce the runtime 
    parserTwitter.getTwitterContent('gg2018.json',twitterTokensFile,twitterLowerTokensFile)

    
    (twitterTokens,twitterLowerTokens) = parserTwitter.readTwitterTokens(twitterTokensFile,twitterLowerTokensFile)
    # extract names of presenters
    getMatchNameList.getMatchUnigramList(twitterTokens,twitterLowerTokens,presenterFeature)


if __name__ == "__main__":
    main()