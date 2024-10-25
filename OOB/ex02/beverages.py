#!/usr/bin/python3

class Beverage:
    def __init__(self, name = "hot beverage", price=None):
        self.name = name
        self.price = price if price is not None else 0.30

    def description(self):
        return "Just some hot water in a cup."
    
    def __str__(self):
        return f"""nom : {self.name}
price : {self.price}
description : {self.description()}"""

class Coffee(Beverage):
    def __init__(self, name = "coffee", price = 0.40):
        super().__init__(name, price)

    def description(self):
        return "A coffee, to stay awake"

class Tea(Beverage):
    def __init__(self, name = "tea"):
        super().__init__(name)

class Chocolat(Beverage):
    def __init__(self, name = "chocolate", price = 0.50):
        super().__init__(name, price)
    
    def description(self):
        return "Chocolate, sweet chocolate..."

class Cappuccino(Beverage):
    def __init__(self, name="cappuccino", price= 0.45):
        super().__init__(name, price)
    
    def description(self):
        return "Un po’ di Italia nella sua tazza!"

if __name__ == "__main__":
    beverage = Beverage()
    print(beverage)
    
    coffee = Coffee()
    print(coffee)
    
    tea = Tea()
    print(tea)
    
    chocolate = Chocolat()
    print(chocolate)
    
    cappuccino = Cappuccino()
    print(cappuccino)
    