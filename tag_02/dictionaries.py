# Dictionary in Python
# Mutable Datenstruktur -> Zwei - Dimensional

d1 = {"vorname" : "Daniel"}

print(d1)
print(type(d1))

d1 = {
    "vorname" : "Daniel",
    "nachname" : "Kaiser",
    "alter" : 45,
    "ort" : "Jena"
      }
print(d1)

# Auf items im Dictionary zugreifen
for key, value in d1.items():
    # print("{}: {}".format(key, value))
    print("The value of '{}' is '{}'".format(key, value))

# Auf keys zugreifen
for key in d1.keys():
    print(key)

for value in d1.values():
    print(value)

print(d1["alter"])
d1["alter"] = 46
print(d1["alter"])
d1["auto"] = "Mokka"
print(d1["auto"])
print(d1)