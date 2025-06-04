""" Autor: Adam Satzke
Datum: 04.06.2025
functions.py: Testen von Funktionen in Python.
"""
# Built-In Functions
import random
import math
# random_wert = random.randint(0, 10)
# print("Random Wert = ", random_wert)
# result = math.sqrt(random_wert)
# print("Result: ", result)

""" Funktionsdefinitionen """
# Eigene Funktionen definieren.
def meine_erste_funktion():
    print("Python Funktion.")

# Positionelle Argumente: Reihenfolge und Anzahl wird vordefiniert.
def funktion_mit_argumenten(a, b, c, d):
    print("Vorher: ", a, b, c, d)
    a += 1
    b += 2
    c += 3
    d += 4
    print("Nachher: ", a, b, c, d)

def optional_args(a, b, c=None):
    print(a, b, c)

def return_value_function(x):
    liste = []
    for i in range(x):
        liste.append(math.sqrt(random.randint(0, x)))
    return liste

""" Main Code Here """
# meine_erste_funktion()
# meine_erste_funktion()
# meine_erste_funktion()
# meine_erste_funktion()

for i in range(10):
    meine_erste_funktion()

funktion_mit_argumenten(1, 2, 3, 4)
optional_args(2, 4)
optional_args(2, 4, 5)
# optional_args(2, 4, 5, 8)

# Wenn man einen Rückgabewert erwartet, muss man den irgendwo im Hauptprogramm
# speichern.
liste_7 = return_value_function(7)
liste_2 = return_value_function(2)
liste_10 = return_value_function(10)

print(liste_7)
print(liste_2)
print(liste_10)