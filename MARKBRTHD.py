
print("Welcome to Marks Birthday Party!")
print("Please provide the following details and you need to be 12 to 15 to enter:")
try:
    age = int(input("Enter your age: "))
    if 12 <= age <= 15:
        name = input("Enter your name: ")
        print(f"Hello {name}, you are eligible to enter the party!")
    else:
        print("Sorry, you are not eligible to enter the party.")
except SyntaxError:
    print("Invalid input. Please enter a valid age.")
finally:
    print("Thank you for your interest!")
