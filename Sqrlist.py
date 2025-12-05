import math

even_sqr = []
odd_sqr = []
decimal_sqr = []

player = int(input("Enter a number: "))
player2 = int(input("Enter another that is bigger: "))

for i in range(player, player2):
    root = math.sqrt(i)
    
   
    if root.is_integer():
        if int(root) % 2 == 0:  # Even integer]
            category = "even"
            even_sqr.append(root)
        else:  # Odd integer
            category = "odd"
            odd_sqr.append(root)
    else:  # Decimal (non-integer)
        category = "decimal"
        decimal_sqr.append(root)
    
    
    print(f"number: {i}, square root(rounded to 3 decimal places): \n{root:.3f}, which is {category}") 

# Final lists
print(f"\nEven square roots: {even_sqr}")
print(f"Odd square roots: {odd_sqr}")
print(f"Decimal square roots: {decimal_sqr}")

print(f"The amount of even/odd/decimal square roots are: {len(even_sqr)}/{len(odd_sqr)}/{len(decimal_sqr)}")