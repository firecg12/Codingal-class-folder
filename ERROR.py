RED = '\033[31m'


try:
    num1, num2 = eval(input("Enter two numbers separated by a comma: "))
    result = num1 / num2
    print("The result is:", result)

except ZeroDivisionError:
    print(f"{RED}Error: Division by zero is not allowed.{RED}")

except SyntaxError:
    print(f"{RED}Error: Invalid input syntax.n\Please enter two numbers separated by a comma!!{RED}")

except:
    print(f"{RED}An unexpected error occurred.\nPlease try again with the right input!!!{RED}")
finally:
    print("This Execution is executed no matter what completed.")