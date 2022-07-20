class Computer:
    '''Program to demonstrate Encapsulation'''
    def __init__(self):
        self.__maxprice=900
    def sell(self):
        print("Selling price is:",self.__maxprice)
    def setmaxprice(self,price):
        self.__maxprice=price
c1=Computer( )
c1.sell( )
c1.__maxprice=1000
c1.sell( )
c1.setmaxprice(1000)
c1.sell( )
