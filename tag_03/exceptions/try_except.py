# Exceptions in Python

# Error handling - Fehlerbehandlung

try:
    eingabe = input("Bitte eine Ganzzahl eingeben: ")
    zahl = eingabe / 3
# Nicht schön.
except:
    print("Die Eingabe war keine Ganzzahl!")

# Programm wird nicht unterbrochen und Code wird nach der Fehlerbehandlung
# weiter ausgeführt.
print("Hier gehts weiter.")
