import re, random
from colorama import Fore, init


init(autoreset=True)


destinations = {
    "beaches": ["Maldives", "Bora Bora", "Maui", "Phuket", "Seychelles"],
    "mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas", "Andes", "Pyrenees"],
    "cities": ["Paris", "New York", "Tokyo", "Rome", "Barcelona"],    
    "historical": ["Athens", "Rome", "Cairo", "Jerusalem", "Machu Picchu"],
    "adventure": ["Costa Rica", "New Zealand", "Iceland", "Peru", "South Africa"],
    "cultural": ["Kyoto", "Istanbul", "Marrakech", "Fez", "Varanasi"],
}

jokes = [
    f"Why don't scientists trust atoms? \nBecause they make up everything!",
    f"Why did the scarecrow win an award? \nBecause he was outstanding in his field!",
    f"Why don't skeletons fight each other? \nThey don't have the guts!",
    f"Why did the bicycle fall over? \nBecause it was two-tired!",
    f"Why did the math book look sad? \nBecause it had too many problems!"
    f"Why did the tomato turn red? \nBecause it saw the salad dressing!"
    f"Why did the golfer bring two pairs of pants? \nIn case he got a hole in one!"
    f"Why did the coffee file a police report? \nIt got mugged!"
    f"Why did the cookie go to the doctor? \nBecause it felt crummy!"
    f"Why did the computer go to the doctor? \nBecause it had a virus!"
]

def normalize_input(user_input):
    return re.sub(r"\s+", " ", user_input.strip().lower())

def get_recommend():
    print(Fore.CYAN + f"TravelBOT: What type of destination are you interested in? \n(beaches, mountains, cities, historical, adventure, cultural)")
    preference = input(Fore.GREEN + "You: ")
    preference = normalize_input(preference)

    if preference in destinations:
        suggestion = random.choice(destinations[preference])
        print(Fore.CYAN + f"TravelBOT: I recommend visiting {suggestion}! It's a great {preference} destination. \n do you like it(yes/no)?")
        answer = input(Fore.GREEN + "You: ").lower()


        if answer == "yes":
            print(Fore.CYAN + f"TravelBOT: Great! I'm sure you'll have an amazing time in {suggestion}!")
        elif answer == "no":
            print(Fore.CYAN + f"TravelBOT: No worries! Let's try another suggestion.")
            get_recommend()
        else:
            print(Fore.RED + f"TravelBOT: I didn't understand that. Let's try again.")
            get_recommend() 
    else:
        print(Fore.CYAN + f"TravelBOT: Sorry, I don't have recommendations for that type of destination. Please choose from the options provided.")
        get_recommend()
    

def packing_tips():
    print(Fore.CYAN + f"TravelBOT: Where to?")
    destination = input(Fore.GREEN + "You: ")
    print(Fore.CYAN + f"How many days will you be staying?")
    days = input(Fore.GREEN + "You: ")


    print(Fore.GREEN + f"TravelBOT: packing tips for {days} days in {destination}:")
    print(Fore.GREEN + f"~~ Pack versatile clothing that can be layered.")
    print(Fore.GREEN + f"~~ Don't forget your chargers and adapters.")
    print(Fore.GREEN + f"~~ Bring a reusable water bottle.")
    print(Fore.GREEN + f"~~ Check the weather forecast and pack accordingly.")
# tell a random joke
def tell_joke():
    print(Fore.CYAN + f"TravelBOT: Here's a joke for you:")
    print(Fore.GREEN + f"{random.choice(jokes)}")   


def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.MAGENTA + "1. Recommend destinations based on your preferences.")
    print(Fore.MAGENTA + "2. Provide packing tips for your trip.")
    print(Fore.MAGENTA + "3. Tell you a joke to brighten your day.")
    print(Fore.MAGENTA + "Show this help message again.(help)")
    print(Fore.MAGENTA + "Exit the chatbot.(exit or quit)\n")
def chat():
    print(Fore.CYAN + "Welcome to TravelBOT!")
    name = input(Fore.GREEN + "What's your name? ")
    print(Fore.CYAN + f"Nice to meet you, {name}! How can I assist you with your travel plans today(enter a number)?")

    show_help()

    while True:
        user_input = input(Fore.GREEN + "You: ")
        user_input = normalize_input(user_input)

        if "1" in user_input:
            get_recommend()
        elif "2" in user_input:
            packing_tips()
        elif "3" in user_input:
            tell_joke()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "quit" in user_input:
            print(Fore.CYAN + f"TravelBOT: Safe travels, {name}! Goodbye!")
            break
        else:
            print(Fore.RED + f"TravelBOT: I'm sorry, I didn't understand that. Please try again or type 'help' for options.")
        if user_input in ["exit", "quit"]:
            print(Fore.CYAN + f"TravelBOT: Safe travels, {name}! Goodbye!")
            break
        if user_input in ["help"]:
            show_help()

if __name__ == "__main__":
    chat()