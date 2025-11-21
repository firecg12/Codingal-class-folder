print("Welcome to Mark's Birthday Party!")
print("Please provide the following details. You need to be 12 to 15 to enter:")

try:
    age = int(input("Enter your age: ")) 

    if 12 <= age <= 15:
        name = input("Enter your name: ")
        print(f"Hello {name}, you are eligible to enter the party!")
    else:
        print("Sorry, you are not eligible to enter the party.")

except ValueError:  
    print("Invalid input. Please enter a valid age (numbers only).")

finally:
    print("Thank you for your interest!")



