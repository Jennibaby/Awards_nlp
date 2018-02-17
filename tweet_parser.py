from extract_names import get_human_names

search_terms = {"Host": ["Host", "Presenter"], "Best Actor": ["Best Actor", "Greatest Actor"]}
information = {"Host": [],
               "Best Motion Picture - Drama": [],
               "Best Motion Picture - Musical or Comedy": [],
               "Best Performance by an Actress in a Motion Picture - Drama": [],
               "Best Performance by an Actor in a Motion Picture - Drama": [],
               "Best Actress in a Motion Picture - Musical or Comedy": [],
               "Best Director": [],
               "Best Performance by an Actor in a Motion Picture - Musical or Comedy": [],
               "Best Supporting Actress in a Motion Picture": [],
               "Best Supporting Actor in a Motion Picture": [],
               "Best Original Score in a Motion Picture": [],
               "Best Original Song in a Motion Picture": [],
               "Best Screenplay in a Motion Picture": [],
               "Best Motion Picture - FOreign Language": [],
               "Best Animated Film": [],
               "Best TV series - Drama": [],
               "Best Performance by an Actress in a TV Series - Drama": [],
               "Best Performance by an Actor in a TV Series - Drama": [],
               "Best TV Series Musical or Comedy": [],
               "Best performance by an Actor in a TV series - Musical or Comedy": [],
               "Best Performance by an Actress in a TV series - Musical or Comedy": [],
               "Best Limited Series or Motion Picture Made for Television": [],
               "Best Performance by an Actor in a Limited Series or Motion Picture Made for Television": [],
               "Best Performance by an Actress in a Limited Series or Motion Picture Made for Television": [],
               "Best Performance by an Actor in a Supporting Role in a Series, Limited Series or Motion Picture Made for Television": [],
               "Best Performance by an Actress in a Supporting Role in a Series, Limited Series or Motion Picture Made for Television": [],
               }

text_file = open("Files\\ggTweets.txt", "r")
tweets = text_file.readlines()

placeholder = 0
num_exceptions = 0
for i in range(0, len(search_terms.keys())):
    for term in search_terms.get(search_terms.keys()[i]): #range(0, len(search_terms.get(search_terms.keys()[i]))):
        for t in tweets:
            if term in t:
                try:
                    name_list = get_human_names(t)
                except:
                    num_exceptions += 1
                placeholder += 1
                if(placeholder%10 == 0):
                    print(placeholder)
                ## extract name
print (placeholder)

print(search_terms.values())
print(information.keys())


#### Too Slow ####
# placeholder = 0
# num_exceptions = 0
# for i in range(0, len(search_terms.keys())):
#     for term in search_terms.get(search_terms.keys()[i]): #range(0, len(search_terms.get(search_terms.keys()[i]))):
#         for t in tweets:
#             if term in t:
#                 try:
#                     name_list = get_human_names(t)
#                 except:
#                     num_exceptions += 1
#                 placeholder += 1
#                 if(placeholder%10 == 0):
#                     print(placeholder)
#                 ## extract name
# print (placeholder)
