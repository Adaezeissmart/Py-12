class Computer:
    def __init__(self):
        self.__maxprice = 1000

    def sell(self):
        print("Selling Prive: {}".format(self.__maxprice))


    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()
c.sell
c.__maxprice = 1200
c.sell

c.setMaxPrice(1200)
c.sell()