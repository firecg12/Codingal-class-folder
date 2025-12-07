#try 1:
tup1 = (4,3,2,2,-1,18)
tup2 = (2,4,8,8,3,9)
 
print("Rose is a computer science student who wants to calculate the product of all numbers in the given tuples.")
print ("The tuples are:" , tup1, "and", tup2)
def product_of_tuple(tup):
    pruduct_of_tup1 = tup1[0] * tup1[1] * tup1[2] * tup1[3] * tup1[4] * tup1[5] * tup1[6] if len(tup1) > 6 else tup1[0] * tup1[1] * tup1[2] * tup1[3] * tup1[4] * tup1[5]
    pruduct_of_tup2 = tup2[0] * tup2[1] * tup2[2] * tup2[3] * tup2[4] * tup2[5] * tup2[6] if len(tup2) > 6 else tup2[0] * tup2[1] * tup2[2] * tup2[3] * tup2[4] * tup2[5]
    return pruduct_of_tup1, pruduct_of_tup2
result = product_of_tuple(tup1) 
result2 = product_of_tuple(tup2)
print("The product of all numbers in tup1 is:", result[0])
print("The product of all numbers in tup2 is:", result2[1])

# try 2:
print("Try 2: ")
tup1 = (4, 3, 2, 2, -1, 18)
tup2 = (2, 4, 8, 8, 3, 9)

def product_of_tuple(tup):
    product = 1
    for i in tup:      
        product *= i
    return product

result1 = product_of_tuple(tup1)
result2 = product_of_tuple(tup2)

print("The product of all numbers in tup1 is:", result1)
print("The product of all numbers in tup2 is:", result2)
