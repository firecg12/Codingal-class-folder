# generate a random password with specified length, including letters, numbers, and special characters
import random
import string
password_length = int(input("Enter the desired password length: "))
if password_length < 1:
    print("Password length should be at least 1.")

def generate_password(length):
    # Fundamental characters for password
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate random password
    password = ''.join(random.choice(characters) for _ in range(length))
    return password
# Generate and print the random password
random_password = generate_password(password_length)
# Output the generated password
print("Generated Password:", random_password)
