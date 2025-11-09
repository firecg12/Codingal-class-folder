def add(P, Q):
    return P + Q
def subtract(P, Q):
    return P - Q
def multiply(P, Q):
    return P * Q
def divide(P, Q):
    if Q == 0:
        raise ValueError("Cannot divide by zero.")
    return P / Q

print("Calculator module loaded.")
print("+, -, *, / functions are available.")

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

choice = input("Enter operation (+, -, *, /): ")


if choice == '+':
    result = add(num1, num2)
elif choice == '-':
    result = subtract(num1, num2)
elif choice == '*':
    result = multiply(num1, num2)
elif choice == '/':
    result = divide(num1, num2)
else:
    print("Invalid operation.")
    exit()

print("The result is:", result);