# Exceptions zusammenfassen

try:
    eingabe = input("Geben Sie eine Zahl ein: ")
    eingabe = int(eingabe)
    x = eingabe / 0
    
except (ZeroDivisionError, ValueError) as ex:
    print(ex)
