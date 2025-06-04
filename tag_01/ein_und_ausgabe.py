# Eingabe - Ausgabe

# print("Hello World")
# print("Hello", "World", sep='#', end="ENDE")

# print("Geben Sie Ihren Namen ein: ")

# username = input()

# print("Ihr Name ist: ", username)

# zahl = input("Geben Sie eine Zahl ein: ")

# zahl_umgewandelt = int(zahl)
# result = zahl_umgewandelt / 3
# print(result)

zahl: int

zahl = "nicht integer"
a = b = c = 4
d = 5
a = d
print(a, b, c, d)
name, vorname = "Daniel", "Kaiser"
print(name, vorname)

# Immutable
print(id("5"))
var = "5"
print(id(var))
var2 = 5
print(id(5))
print(id(var2))

# Mutable
meine_liste1 = [2, 3, 4]
meine_liste2 = [2, 3, 4]
print(id(meine_liste1), id(meine_liste2))

