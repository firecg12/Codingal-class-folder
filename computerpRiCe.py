
class ComputerPrice:

    def __init__(self):
        self.__maxprice = 900

    def sell(self):
        print("seling Price: {}".format(self.__maxprice))
    
    def setMaxPrice(self, price):
        self.__maxprice = price 

c = ComputerPrice()
c.sell()

c.__maxprice = 1000
c.sell()

c.setMaxPrice(1000)
c.sell()
