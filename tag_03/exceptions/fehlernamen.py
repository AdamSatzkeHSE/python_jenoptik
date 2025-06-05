# Fehlernamen im except

try:
    eingabe = input("Bitte geben Sie eine natürliche Ganzahl: ")
    eingabe = int(eingabe)
    eingabe = float(eingabe)

    print("Das Ergebnis der Division ist: {}".format(100 / eingabe))
except TypeError:
    print("Sie haben die Datenumwandlung vergessen!")
except ValueError:
    print("Die Eingabe war keine Ganzzahl.")
# except ArithmeticError:
#     print("Das wird zuerst abgefangen.")
except ZeroDivisionError:
    print("Die Eingabe war 0! Das ist nicht erlaubt")

# Hier gehts weiter
print("Programm weiter ausführen.")
