# Beispiel mit Coffee Class

class Coffee:
    grenzen_dict = {
        "max_bohnen": 100,
        "max_wassermenge": 200
    }
    # Kontruktor
    def __init__(self, water, beans):
        if water > Coffee.grenzen_dict["max_bohnen"]:
            print("Dieses Objekt ist nicht erlaubt.")
            raise ValueError("Wassermenge überschritten.")
        else:
            self.water = water

        self.beans = beans

    def get_coffee(self):
        print("Kaffee wird zubereitet.")
        return self.water + self.beans

# Class Inheritance - Klassenvererbung
# MilkCoffee enthält alle Eigenschaften und Funktionalität einer Coffee Klasse.
class MilkCoffee(Coffee):
    # Konstruktor
    def __init__(self, water, beans, milk):
        # super() Funktion: Wird aufgerufen, um die Superklasse mit den
        # gewünschten Eigenschaften zu initialisieren.
        super().__init__(water, beans)
        self.milk = milk

    def get_milk_coffee(self):
        print("Milchkaffee wird zubereitet.")
        return self.get_coffee() + self.milk

class Capuccino(MilkCoffee):
    def __init__(self, water, beans, milk, espresso_shots):
        super().__init__(water, beans, milk)
        self.espresso_shots = espresso_shots

    def get_capuccino(self):
        print("Capuccino wird zubereitet.")
        return self.get_milk_coffee() + self.espresso_shots * 1.5

class Moccachino:
    pass

if __name__ == '__main__':
    wahl = input("Was möchten Sie haben? ")
    if wahl == "kaffee":
        coffee = Coffee(120, 10)
        print(coffee.get_coffee())
    elif wahl == "milchkaffee":
        milchkaffee = MilkCoffee(10, 20, 30)
        print(milchkaffee.get_milk_coffee())
    elif wahl == "capuccino":
        capuccino = Capuccino(40, 30, 20, 10)
        capuccino.get_capuccino()
    else:
        print("Die Wahl {} wurde noch nicht programmiert...".format(wahl))

