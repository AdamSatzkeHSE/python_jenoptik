# if elif else
# Kontrollstrukturen
# Verzweigung

# importierte Module
import random
import math
import sys

# Eigene Funktionsdefinitionen
def func1():
    pass

def func2(x, y):
    pass

def func3(a, b, c):
    return a + b + c

# Globale Variablen
global1 = 4
global2 = "Python Schulung"

# Skript
# 1. Benutzereingabe

x = 10

if x == 10:
    print("x ist die", x)
else:
    print("x ist nicht gleich 10, sondern ", x)

x = 11
x = 2.0
x = "Python"

# # Nicht zulässig.
# if x == "Python":
#     x += 2
#     y = x * 6
#     result = y - 1

# Mehrere elif
# x = 3
x = -1
if x == 0:
    print("x ist 0")
elif x == 3:
    print("x ist eine 3")
elif x == 5:
    print("5")
elif x > 5:
    print("x ist > 5")
else:
    print("Alles andere")

vorname = input("Wie ist ihr Name? ")

# if vorname == "Adam" or vorname == "Daniel":
#     print("Kursteilnehmer erkannt. Zugang erhalten.")
# else:
#     print("Nicht erlaubt")

def teste_grenze(x):
    if x == "Daniel" or x == "Adam":
        return True
    else:
        return False

result = teste_grenze(vorname)
print("Das ergebnis ist", result)
