import random
# Greet the user
print("Hello! I am AI Bot. What's your name?")
name = input()

print(f"Nice to meet you, {name}!")

while True:
    try:
        # Mood
        mood = input("How are you feeling today? (good/bad): ").lower()

        if mood == "good" or "great" in mood or "awesome" in mood:
            print("I'm glad to hear that!")
        elif mood == "bad" or "not good" in mood or "sad" in mood:
            print("I'm sorry to hear that. Hope things get better soon.")
        else:
            print("I see. Sometimes it's hard to put feelings into words.")

        # Color
        color = input("What is your favorite color?: ").lower()
        if color in ["red", "orange", "yellow", "green", "blue", "indigo", "violet", "pink", "black", "white", "gray"]:
            print(f"{color.capitalize()} is a beautiful color!")
        else:
            print("That's an interesting choice of color!")

        # Hobbies
        hobbies = input("What are your hobbies?: ").lower()
        print(f"Nice! {hobbies} sounds fun.")

        # Pets
        pets = input("Do you have any pets? (yes/no): ").lower()
        if pets == "yes":
            pet_type = input("What kind of pet?: ").lower()
            print(f"{pet_type.capitalize()}s are awesome!")
        elif pets == "no":
            print("Maybe you'll get one someday!")
        else:
            print("Got it!")
        age = int(input("How old are you?: "))
        if age < 18:
            print("You're quite young!")
        elif 18 <= age < 30:
            print("You're in the prime of your life!")
        elif 30 <= age < 50:
            print("You have a lot of experience!")
        else:
            print("You must have a lot of wisdom!")

    except ValueError:
        print("❌ Please enter a valid age.")
    except:
        print("❌ Something went wrong. Try again.")

    # Repeat or exit
    again = input("Do you want to chat again? (yes/no/idk): ").lower()
    if again != "yes":
        break
    if again == "idk":
        random_response = random.choice(["Sure, let's chat again!", "No problem, we can chat later!", "I'm here whenever you want to talk!"])
        print(random_response)
        if random_response == "Sure, let's chat again!":
            continue
        else:
            break
          

# End
print(f"It was nice chatting with you, {name}. Goodbye!")