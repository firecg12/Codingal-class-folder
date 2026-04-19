import re
import random
import time
from datetime import datetime
from colorama import Fore, init

init(autoreset=True)

# ---------------- DATA ----------------
destinations = {
    "beaches": ["Maldives", "Bora Bora", "Maui", "Phuket", "Seychelles"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas", "Andes", "Pyrenees"],
    "cities": ["Paris", "New York", "Tokyo", "Rome", "Barcelona"],
    "historical": ["Athens", "Rome", "Cairo", "Jerusalem", "Machu Picchu"],
    "adventure": ["Costa Rica", "New Zealand", "Iceland", "Peru", "South Africa"],
    "cultural": ["Kyoto", "Istanbul", "Marrakech", "Fez", "Varanasi"],
}

jokes = [
    "Why don't scientists trust atoms?\nBecause they make up everything!",
    "Why did the scarecrow win an award?\nBecause he was outstanding in his field!",
]

# ---------------- UTIL ----------------
def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

def is_name_question(text):
    triggers = ["what is my name", "what's my name", "whats my name", "who am i", "do you know my name", "guess my name", "what am i"]
    return any(t in text for t in triggers)

def funny_name_reply(name):
    return random.choice([
        f"{name}… I think? 😅",
        f"Oh right — you're {name}! (almost forgot lol)",
        f"You're {name}. I'm pretty sure 🤔",
        f"im sorry {name}, I can't remember your name for some reason.",
        f"BRO WHAT WAS YOUR NAME AGAIN? I FORGOT ALREADY 😂",
        f"FR? You cant even remember your own name {name}? That's rough 😬",
    ])

# ---------------- FEATURES ----------------
def get_recommend():
    invalid_count = 0

    while True:
        print(Fore.CYAN + "TravelBOT: Choose a type (beaches, mountains, cities, historical, adventure, cultural)")
        preference = normalize_input(input(Fore.GREEN + "You: "))

        if preference in ["exit", "quit"]:
            print(Fore.YELLOW + "TravelBOT: Returning to main menu...")
            return

        if preference in destinations:
            invalid_count = 0

            suggestion = random.choice(destinations[preference])
            print(Fore.CYAN + f"TravelBOT: Try {suggestion}! Do you like it? (yes/no)")

            answer = normalize_input(input(Fore.GREEN + "You: "))

            if answer in ["exit", "quit"]:
                return

            if answer == "yes":
                print(Fore.CYAN + f"TravelBOT: Awesome! Enjoy {suggestion} 😎")
                return
            elif answer == "no":
                print(Fore.YELLOW + "TravelBOT: Let's try another one...")
            else:
                print(Fore.RED + "TravelBOT: Please answer yes or no.")

        else:
            invalid_count += 1
            print(Fore.RED + "TravelBOT: Invalid category, try again.")

            if invalid_count >= 3:
                print(Fore.MAGENTA + "TravelBOT: Feeling adventurous? How about Mars? 🚀")
                invalid_count = 0

def packing_tips():
    destination = input(Fore.GREEN + "Where are you going? ")
    days = input(Fore.GREEN + "How many days? ")

    print(Fore.CYAN + f"TravelBOT: Packing tips for {destination} ({days} days):")
    print(Fore.GREEN + "- Pack layers")
    print(Fore.GREEN + "- Bring chargers/adapters")
    print(Fore.GREEN + "- Water bottle")
    print(Fore.GREEN + "- Check weather")

def tell_joke():
    print(Fore.CYAN + "TravelBOT: 😂")
    print(Fore.GREEN + random.choice(jokes))

def weather():
    city = input(Fore.GREEN + "Which city? ")
    condition = random.choice(["Sunny ☀️", "Rainy 🌧️", "Cloudy ☁️", "Windy 🌬️"])
    print(Fore.CYAN + f"TravelBOT: Weather in {city}: {condition}")

def time_info():
    now = datetime.now()
    print(Fore.CYAN + f"TravelBOT: Current time: {now.strftime('%H:%M:%S')}")

def news():
    print(Fore.CYAN + "TravelBOT: 📰 Travel News:")
    print(Fore.GREEN + "- Flights are cheaper this week!")
    print(Fore.GREEN + "- New destinations trending now!")

def show_help():
    print(Fore.MAGENTA + "\nCommands:")
    print("1 / recommend → destination ideas")
    print("2 / pack → packing tips")
    print("3 / joke → random joke")
    print("weather → weather info")
    print("time → current time")
    print("news → travel news")
    print("help → show this")
    print("exit → quit\n")

# ---------------- MAIN CHAT ----------------
def chat():
    print(Fore.CYAN + "Welcome to TravelBOT ✈️")

    name = input(Fore.GREEN + "What's your name?\n>> ").strip()
    name_norm = normalize_input(name)

    print(Fore.CYAN + f"Nice to meet you, {name}!")

    print(Fore.CYAN + "Loading TravelBOT features", end="", flush=True)
    for _ in range(8):
        time.sleep(0.25)
        print(".", end="", flush=True)
    print("\n")

    show_help()

    while True:
        user_input = normalize_input(input(Fore.GREEN + ">> "))

        if not user_input:
            continue

        # 👇 NAME QUESTIONS (WHO AM I STYLE)
        if is_name_question(user_input):
            print(Fore.CYAN + "TravelBOT: " + funny_name_reply(name))

        # 👇 IF USER TYPES THEIR NAME
        elif user_input == name_norm:
            print(Fore.CYAN + f"TravelBOT: Oh right 😅 you're {name}!")

        elif any(word in user_input for word in ["1", "recommend", "destination"]):
            get_recommend()

        elif any(word in user_input for word in ["2", "pack", "packing"]):
            packing_tips()

        elif any(word in user_input for word in ["3", "joke"]):
            tell_joke()

        elif "weather" in user_input:
            weather()

        elif "time" in user_input:
            time_info()

        elif "news" in user_input:
            news()

        elif "help" in user_input:
            show_help()

        elif any(word in user_input for word in ["exit", "quit"]):
            print(Fore.CYAN + f"TravelBOT: Goodbye {name}! ✈️")
            break

        else:
            print(Fore.RED + "TravelBOT: I didn't understand. Type 'help'.")

# ---------------- RUN ----------------
if __name__ == "__main__":
    chat()