# Listen - Methoden
# append() -> Element hinzufügen.
liste = [1, 2, 3, 4]
liste.append(5)
print(liste)

# insert() -> Element hinzufügen in geg. Stelle
liste.insert(0, 9)
print(liste)

# Indexing: Werte lesen oder überschreiben / ersetzen
print(liste[4])
liste[4] = 10
print(liste)

# Count
print(liste.count(10))
print(liste.count(4))
print(liste.count(5))

if liste.count(5) == 1:
    print("Die 5 kommt einmal vor")
    # In diesem Fall soll diese Grenze geprueft werden.
    # Code, Funktionen, etc.

# pop(): Entfernt das letzte Element aus der Liste
# liste.pop()
# liste.pop()
# wert = liste.pop(1)
# print(wert)

# remove(): Entfernt das gew. Element (erster Auftritt)
liste.remove(10)
print(liste)

# sort()
liste.sort()
print(liste)

# clear()
liste.clear()
print(liste)
