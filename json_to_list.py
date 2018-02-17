import json;
import numpy;

search_terms = (('host', 'presenter'), ('best actor'), ('best actress'))

with open('Files\\gg2018.json') as json_file:
    json_data = json.load(json_file)
    print (len(json_data))
    print(json_data[0])

json_list = []
for i in range(0, len(json_data)):
    temp_dict = json_data[i]
    temp_lists = temp_dict.values()
    tweet = temp_lists[0]
    json_list.append(tweet)
# numpy.savetxt('shorter_ggjson2.json', json_list, fmt='%s')
print(len(json_list))
print(json_list[0])

# numpy.savetxt('Files\\ggTweets.json', json_list, fmt='%s')
# print("done")

tweetFile = open('Files\\ggTweets.txt', 'w')
for item in json_list:
    temp = item.encode('utf-8')
    tweetFile.write("%s\n" % temp) ## Could not encode all characters (probably because of emojis?
print("done")
# print(json_list[0][0])

# split = json_list[0].split(',')
# print(split)
# for j in range(0, len(json_list)):
#     temp = json_list[j]
#     split = temp.split(',')


# l = ('hi')
# for i in range(0, len(json_list)):
#     l = l + json_list[i].values()
# print(l[0])