# set symetric difference
Set_A = {1, 2, 3, 4, 5}
Set_B = {4, 5, 6, 7, 8}
print("Set_A:", Set_A)
print("Set_B:", Set_B)

sym_diff = Set_A.symmetric_difference(Set_B)
print("Symmetric difference between Set_A and Set_B:", sym_diff)

# print symilar numbers in both sets
common_elements = Set_A.intersection(Set_B)
print("Common elements in both sets:", common_elements)
# add elements to Set_A
addsetelement_to_A = int(input("Enter an integer to add to Set_A: "))
Set_A.add(addsetelement_to_A)
print("Set_A after adding an element:", Set_A)
# remove elements from Set_B
removesetelement_from_B = int(input("Enter an integer to remove from Set_B: "))
Set_B.discard(removesetelement_from_B)
print("Set_B after removing an element:", Set_B)
