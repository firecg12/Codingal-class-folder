# create a new dictionary
my_dict = {'item1': 3, 'item2': 3, 'item3': 3, 'item4': 5, 'item5': 3}

# print the dictionary
print("The dictionary is:", str(my_dict))

# initialize the value K
K = 3

# how many times does K appear in the my_dict
result = 0

for key in my_dict:
    if my_dict[key] == K:
        result = result + 1

# print frequency of K
print("The frequency of K is", str(result))