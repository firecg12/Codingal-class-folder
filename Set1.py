#set of intigers 
Set_int = {6, 7, 17,}
print("Set of integers:", Set_int)
# creat set with different data types
Set_diff = {1, "Hello", 3.4, True, (-7, 6, 7)}
print("Set with different data types:", Set_diff)
# set cannot have duplicate values
set_NoDup = {1, 2, 2, 3, 4, 4, 5}
print("Set with no duplicate values:", set_NoDup)

# create a set from a list
st = [1, 2, 2, 3, 4, 4, 5]
set_from_list = set(st)  
print("Set made from a list:", set_from_list)

# we can make a set from a list removing any number chosen
lis =  int(input("Enter as many numbers of elements you dont want in list from 1-50: "))
list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50]
m = "do you want to remove more elements? (yes/no): "
set_from_list_removal = set(list) - {lis}
print(m)
if input().lower() == 'yes':
    while True:
        lis = int(input("Enter another number to remove: "))
        set_from_list_removal -= {lis}
        print(m)
        if input().lower() != 'yes':
            break
print("Set made from a list after removing an element:", set_from_list_removal)
