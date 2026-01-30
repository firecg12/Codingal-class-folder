
class ReversClassName:
    def __init__(self, word):
        self.word = word
    
    def __reverse_word(self):
        return self.word[::-1]
    
    def get_reversed(self):
        return self.__reverse_word()

UserInput = str(input("Enter a word: "))
Word = ReversClassName(UserInput)
print("Reversed word:", Word.get_reversed())



