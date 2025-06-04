# continue & break. Für Schleifen.

# for i in range(1, 11):
#     if i == 3:
#         x = 4
#         print(x)
#         continue
#     print(i, end=' ')

for i in range(1, 11):
    if i == 3:
        x = 4
        print(x)
        break
    print(i, end=' ')

# Hier mach ich weiter
c = 0
while True:
    c += 1
    print(c)
    if c == 10:
        break
    else:
        print("Andere Operation")
        continue