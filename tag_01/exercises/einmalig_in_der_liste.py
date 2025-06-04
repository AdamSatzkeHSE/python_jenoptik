# Einmaliges in einer Liste

"""
Erstelle eine Liste mit neun zufälligen Zahlen 
Dabei sollen vier Zahlen doppelt vorkommen und eine Zahl nur einmal.

Dann mische die Liste per random.shuffle() und finde heraus, ob und welche Zahl nur
einmal vorkommt.
"""

import random

# Hier möchte ich später meine Werte speichern.
# random_liste = []
# for i in range(9):
#     # Zufallszahl in x speichern.
#     x = random.randint(0, 10)
#     random_liste.append(x)

# print(random_liste)
# print(len(random_liste))
# print(random_liste.count(10))
# # print(random_liste.index(10))
# random_liste.remove(4)
# print(random_liste)


erlaubte_werten = []
for i in range(10):
    zahl = random.randint(0, 100)
    if zahl < 50:
        erlaubte_werten.append(zahl)

    else:
        print("Error: zahl nicht erlaubt:", zahl)

print(erlaubte_werten)
erlaubte_werten.pop()
erlaubte_werten.pop()
erlaubte_werten.pop()

print(erlaubte_werten)


