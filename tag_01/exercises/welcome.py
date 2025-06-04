# Welcome Exercise

# Es soll eine Begrüßung in Abhängigkeit zur Uhrzeit ausgegeben werden.

"""
Zwischen 22 Uhr und 5 Uhr: Gute Nacht
Vor 11 Uhr: Guten Morgen
Vor 15 Uhr: Mahlzeit
Vor 18 Uhr: Guten Nachmittag
Vor 22 Uhr: Guten Abend
"""

# Benutze zum Testen die Funktion "randint(a, b)" vom Modul random
# um eine Zufallszahl von 0 bis 23 zu erzeugen.

# import random

# time = random.randint(0, 23)
# print(time)

time = input()
time = int(time)

if time <= 5 or time >= 23:
    print('Gute Nacht')
elif time < 11:
    print('Guten Morgen')
elif time < 15:
    print('Mahlzeit')
elif time < 18:
    print('Guten Nachmittag')
else:
    print('Guten Abend')
