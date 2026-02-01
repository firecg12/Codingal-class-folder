class India():
    def capital(self):
        print(f"New Delhi is the capital of India.\n")

    
    def language(self):
        print(f"Hindi is the most widely spoken language of India.\n")
    
    def type(self):
        print(f"India is a developing country.\n")
class USA():
    def capital(self):
        print(f"Washington, D.C. is the capital of USA.\n")

    
    def language(self):
        print(f"English is the most widely spoken language of USA.\n")
    
    def type(self):
        print(f"USA is a developed country.\n")

obj_india = India()
obj_usa = USA()

for countries_on_earth in (obj_india, obj_usa):
    countries_on_earth.capital()
    countries_on_earth.language()
    countries_on_earth.type()