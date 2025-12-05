#create a list 
L = [23,40,5,6,9,10,30,34,27]
print("Original List:", L)

#var to store sum of the list
count = 0

for i in L:
    count += i
    print("Sum of the List:", count)

#  get avg
avg = count / len(L)
print(f"The sum is: {count} and the average is: {avg}")

# sort the list
L.sort()
print("The smallest item is:", L[0])
print("The largest item is:", L[-1])
print("Sorted List:", L)    