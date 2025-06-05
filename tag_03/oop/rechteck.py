# OOP - Objekt Orientierte Programmierung

# Klasse - Class
# Schlüßelwort zum Erzeugen einer Klasse

class Rechteck:
    # Konstruktor. Setzen von Eigenschaften.
    # self: Bezeichner für die eigene Instanz der Klasse.
    def __init__(self, breite, hoehe):
        self.breite = breite
        self.hoehe = hoehe
    
    # Methoden
    def flaeche(self):
        return self.breite * self.hoehe

if __name__ == '__main__':
    form_1 = Rechteck(10, 10)
    form_2 = Rechteck(3, 5)
    form_3 = Rechteck(9, 7)

    print("Form_1 hat eine Flaeche von: ", form_1.flaeche())
    print("Form_2 hat eine Hoehe von: ", form_2.hoehe)
    print("Form_3 hat eine Breite von: ", form_3.breite)
    # print(form_1)
    # print(form_2)
    # print(form_3)

    # print(type(form_1))