# create a new dictionary
test_dict = {'apple': 2, 'banana': 2, 'cherry': 4, 'dates': 2, 'elderberry': 7}

# print the dictionary
print("The dictionary is:", str(test_dict))

# initialize the value K
K = 2

# how many times does K appear in test_dict
count = 0

for item in test_dict:
    if test_dict[item] == K:
        count = count + 1

# print frequency of K
print("The frequency of K is", str(count))
