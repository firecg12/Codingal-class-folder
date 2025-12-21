# two list iteams
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = map(lambda x, y: x + y, list1, list2)

print("Addition of two lists is ")
print(list(result))
# using map to get square root
def square_root(x):
    return x*x
nums = [1, 2, 3, 4, 5]
square_roots = list(map(square_root, nums))
print("Square of the numbers is ", square_roots)
# list comprehension 
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
print("Even numbers are ", even_numbers)    
odd_numbers = [x for x in numbers if x % 2 != 0]
print("Odd numbers are ", odd_numbers)
