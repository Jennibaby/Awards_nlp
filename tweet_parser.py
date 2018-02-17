text_file = open("Files\\ggTweets.txt", "r")
tweets = text_file.readlines()
print(len(tweets)) #  Correct size, read in correctly
print(tweets[0]) # printed first tweet that was saw in json_to_list.py so it looks to have written and read back in correctly
