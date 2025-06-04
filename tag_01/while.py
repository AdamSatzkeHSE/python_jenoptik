# While - Schleife

i = 0
while i < 5:
    print(i, end=' ')
    i += 1

# Endloss Schleife (Vorsichtig...)
# while True:
#     pass

counter = 0
while counter < 5:

    if counter == 2:
        print("Counter ist gleich 2 Bedingung erfuellt.")
        counter += 1

    print("Fertig mit Schleife", counter)
    counter += 1

print("Jetzt bin ich raus. Counter = ", counter)