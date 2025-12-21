# creating a comprehension for a list to find the square of numbers
squares = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
           11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def square(x):
    return x * x

squared_numbers = [square(x) for x in squares]
print("Squared numbers are:", squared_numbers)
# find even and odd numbers using list comprehension
even_numbers = [x for x in squares if x % 2 == 0]
odd_numbers = [x for x in squares if x % 2 != 0]
print("Even numbers are:", even_numbers)
print("Odd numbers are:", odd_numbers)

fruit = ["apple", "banana", "cherry", "date"]
# capitalize each fruit name using list comprehension
capitalized_fruits = [fruit.capitalize() for fruit in fruit]
print("Capitalized fruit names are:", capitalized_fruits)


