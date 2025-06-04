# Fibonacci

"""
Schreibe ein Programm, das per for-Schleife die ersten 10 Zahlen der
Fibonacci-Folge ausgibt: 0 1 1 2 3 5 8 13 21 34
Die ersten beiden Zahlen dürfen hard-codiert ausgegeben werden:
print(0, 1)
Alle folgenden Zahlen müssen dann in der for-Schleife ausgegeben werden.
Die Fibonacci-Folge beginnt mit 0 und 1.
Ab dann entsteht die folgende Zahl,
indem man jeweils die beiden vorherigen Zahlen addiert.

Zusatz: Gib alle Fibonacci Zahlen unter 500 aus
"""

print(0, 1)
# range function: Werte von 0 bis n - 1 generieren.
# for i in range(500):
#     a, b = b, a + b

grenze = 500
a = 0
b = 1
counter = 1
next_number = b

while next_number <= grenze:
    print(next_number, end=' ')
    counter += 1
    a, b = b, next_number
    next_number = a + b  


