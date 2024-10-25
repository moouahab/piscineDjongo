#!/usr/bin/python3

import random
import beverages

class CoffeeMachine:
    class EmptyCup(beverages.Beverage):
        def __init__(self, name="empty cup", price=0.90):
            super().__init__(name, price)
        
        def description(self):
            return "An empty cup?! Gimme my money back!"
    
    class BrokenMachineException(Exception):
        def __init__(self):
            super().__init__("This coffee machine has to be repaired")
    
    def __init__(self):
        self.capacity = 10
        self.count_cup = 0
    
    def repaire(self):
        self.count_cup = 0

    def server(self, cup):
        if self.count_cup >= self.capacity:
            raise self.BrokenMachineException()
        
        self.count_cup += 1
        # Utilisation de random.choices pour gérer les probabilités
        return random.choices(
            [self.EmptyCup(), cup()],
            weights=[0.2, 0.8],  # 20% de chance de servir une EmptyCup
            k=1
        )[0]
        

if __name__ == "__main__":
    coffee_machine = CoffeeMachine()
    for _ in range(12):
        try:
            cup = coffee_machine.server(random.choice([beverages.Coffee, beverages.Tea, beverages.Cappuccino]))
            print(cup, "\n---", sep="\n")
        except coffee_machine.BrokenMachineException as e:
            print(e, "Machine repaired", "---", sep="\n")
            coffee_machine.repaire()
