

class Bird:

    def __init__(self):
        print("Bird created")
    
    def WhoisThis(self):
        print("I am a bird")
    
    def swim(self):
        print("Swim faster")

class Penguin(Bird):
    
    def __init__(self):

        super().__init__()
        print("Penguin created")
    
    def WhoIsThis(self):
        print("I am a penguin")
    
    def run(self):
        print("Run faster")


p = Penguin()
p.WhoisThis()
p.swim()
p.run()