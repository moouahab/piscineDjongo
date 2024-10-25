#!/usr/bin/python3

#une methode en python a besoin obiligatoirement 
# du parametre self pour l'instance courente

class Inter:
    def __init__(self, name="My name? I’m nobody, an intern, I have no name."):
        self.name = name

    def __str__(self):
        return self.name

    class Coffee:
        def __str__(self):
            return "This is the worst coffee you ever tasted."

    def work(self):
        raise Exception("I’m just an intern, I can’t do that...")

    def make_coffee(self):
        return Inter.Coffee()


if __name__ == '__main__':
    # Création d'un objet Inter
    intern = Inter()
    print(intern)

    # Création d'un objet Inter avec nom
    intern2 = Inter("Mark")
    print(f"Bonjour je m'appelle {intern2} je suis ravie de vous aide")

    # Création d'un objet Coffee via l'instance de Inter
    coffee = intern.make_coffee()
    print(coffee)

    # Test de la fonction work() qui lance une exception
    try: 
        intern2.work()
    except Exception as e:
        print(e)
    