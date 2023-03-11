import re


class Product:
    def __init__(self,name,price):
        self.name = name
        self.price = price
    
    def __str__(self):
        return f'{self.name} is {self.price}'

    def __add__(self,other):
        if isinstance(other,str):
            self.name += other

p1 = Product('DOG',10)
p2 = Product('CAT',30)
p1+' BIG '
print(p1)
