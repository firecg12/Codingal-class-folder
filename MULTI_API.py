import requests

def get_data_from_api(url, category):
    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()

            if category == "General Knowledge":
                print(f"Did you know? {data['text']}")

            elif category == "Technology":
                print(f"Did you know? {data[0]['setup']}")
                print(f"Answer: {data[0]['punchline']}")

            elif category == "Science":
                print(f"Did you know? {data['fact']}")

            elif category == "History":
                print(f"Did you know? {data['text']}")

            elif category == "Sports":
                event = data["events"][0]
                print(f"Upcoming event: {event['strEvent']}")
                print(f"Date: {event['dateEvent']}")

            elif category == "Math":
                print(f"Did you know? {data['text']}")

        else:
            print("Failed to retrieve data")

    except Exception as e:
        print(f"An error occurred: {e}")


def main():

    print("Welcome to the random fact generator!")

    print("Please select a category for your random fact:")

    categories = {
        "1": "General Knowledge",
        "2": "Technology",
        "3": "Science",
        "4": "History",
        "5": "Sports",
        "6": "Math"
    }

    for key, value in categories.items():
        print(f"{key}. {value}")

    choice = input("Enter your choice (1-6): ")

    if choice == "1":
        get_data_from_api(
            "https://uselessfacts.jsph.pl/random.json?language=en",
            "General Knowledge"
        )

    elif choice == "2":
        get_data_from_api(
            "https://official-joke-api.appspot.com/jokes/programming/random",
            "Technology"
        )

    elif choice == "3":
        get_data_from_api(
            "https://api.chucknorris.io/jokes/random?category=science",
            "Science"
        )

    elif choice == "4":
        get_data_from_api(
            "https://history.muffinlabs.com/date",
            "History"
        )

    elif choice == "5":
        get_data_from_api(
            "https://www.thesportsdb.com/api/v1/json/123/eventsnextleague.php?id=4328",
            "Sports"
        )

    elif choice == "6":
        get_data_from_api(
            "http://numbersapi.com/random/math?json",
            "Math"
        )

    else:
        print("Invalid choice. Please select a valid category.")

if __name__ == "__main__":
    main()
