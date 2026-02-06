# Flash Cards
class flashCard:
    def __init__(self, word, meaning):
        self.word = word
        self.meaning = meaning
    def __str__(self):

        return self.word+'( ' +self.meaning+' )'

flash = []
print("Welcome to Flashcard application!")


while (True):
    word = input("Enter the name you want to add to the flashcard : ")
    meaning = input("Enter the meaning of the word : ")

    flash.append(flashCard(word, meaning))
    choice = input("Do you want to add more flashcards? (y/n) : ")
    if choice.lower() != 'y':
        break

print("\nYour Flashcards are : ")
for f in flash:
    print(">", f)