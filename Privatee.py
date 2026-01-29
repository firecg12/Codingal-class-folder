
class myClass:

    __private_var = 27;

    def __privMeth(self):
        print("I'm inside class myClass")
    

    def hello(self):
        print("Private Variable value: " ,myClass.__private_var)

foo = myClass()
foo.hello()
foo.__privMeth