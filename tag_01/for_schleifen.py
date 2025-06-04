# Kontrollstrukturen 2
# for - Schleifen

# Iterables in Python
# Dictionaries, Sets, Generatoren, Iteratoren, Listen, Sequenzen, Tuples

variable = "Python"

for buchstabe in variable:
    print(buchstabe, end='')
    # if buchstabe == 'y':
    #     # print(buchstabe)
    #     # print("Buchstabe ist y")
    #     print(buchstabe, end='')
    # else:
    #     print("")
    #     # print(buchstabe)
    #     # print("Buchstabe ist nicht y")
print()
for i in 'abcdef':
    print(i, end='$')
print()
s= ""
for i in 'abcdef':
    s += i + "---"

print(s) 
