#-*- coding: utf-8 -*-
import json;
import numpy;
import string;

#### Experiment:  Building the library of names (using host) ####
#### Experiment:  Finding most common names in dictionary ####
example_dict = {'Seth Meyers': 15, 'Seth': 10, 'Meyers': 2, 'sethmeyers': 20, 'Ricky Gervais': 8, 'Allen': 3, 'Mister Allen': 7}
example_dict_keys = example_dict.keys()

done = False;
count = 0
placeholder = 0

new_example_dict = {}

while(len(example_dict_keys) != 0):
	key = example_dict_keys.pop(0)
	found_match = False
	for i in range(0, len(example_dict_keys)):
		compare_key = example_dict_keys[i]
		if(len(key) > len(compare_key)):
			if(compare_key.lower() in key.lower()):
				found_match = True
				new_count = example_dict.get(key) + example_dict.get(compare_key)
				new_example_dict[key] = new_count
		elif(len(key) < len(compare_key)):
			if (key.lower() in compare_key.lower()):
				found_match = True
				new_count = example_dict.get(key) + example_dict.get(compare_key)
				new_example_dict[key] = new_count
		if(found_match != True):
			new_example_dict[key] = example_dict.get(key)
print new_example_dict

new_example_dict_keys = new_example_dict.keys()
print new_example_dict_keys

while(len(new_example_dict_keys) != 0):
	one = new_example_dict_keys[0]
	for k in range(1, len(new_example_dict_keys)):
		found = False
		if(k < len(new_example_dict_keys)):
			two = new_example_dict_keys[k]
			if (one != two): 
				one_b = one.replace(' ', '')
				two_b = two.replace(' ', '')
				one_b = one_b.lower()
				two_b = two_b.lower()
				result = one_b + " , " + two_b
				if(one_b in two_b):
					# string_to_print = "Match: " + one + " , " + two
					string_to_print = "Match: " + result
					print(string_to_print)
					new_example_dict[one] += new_example_dict[two]
					found = True
				elif(two_b in one_b):
					# string_to_print = "Match: " + one + " , " + two
					string_to_print = "Match: " + result
					print(string_to_print)
					new_example_dict[one] += new_example_dict[two]
					found = True
				else:
					# string_to_print = "No Match: " + one + " , " + two
					string_to_print = "No Match: " + result
					print(string_to_print)
		if found == True:
			new_example_dict_keys.remove(two)
			del new_example_dict[two]
	print new_example_dict_keys
	new_example_dict_keys.remove(one)


print new_example_dict 



########## CODE FOR LATTER ####################################################

# host_dict = {}

# with open('__filepath__') as f:
#     content = f.read().splitlines()
#
# for i in range(0, len(content)):
# 	tweet = content[i]
# 	## Building dictionary with form <data #, tweet>
# 	# If tweet contains "Host"
# 	if tweet.find("Host") != -1:
# 		## Extract name and add it to dict
# 		sample_data = 'data' + str(i)
# 		i_string = str(i)
# 		host_dict[i_string] = sample_data
# 	# If tweet contains "host"
# 	elif tweet.find("host") != -1:
# 		## Extract name and add it to dict
# 		sample_data = 'data' + str(i)
# 		i_string = str(i)
# 		host_dict[i_string] = sample_data
#
# print(host_dict['1368'])

#########################################################################################################



