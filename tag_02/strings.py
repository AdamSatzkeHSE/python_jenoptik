# String formating in Python

# print("Hallo Welt", "mein Name ist Adam", sep='*', end='')

# .format()
import random
import math

def func(x, y):
    return random.randint(x, y)

# x = random.randint(0, 10)
# y = random.randint(5, 50)
# print("x = {} und y = {}".format(x, y))

random_result = func(4, 17)
print("Mein Ergebnis ist {}".format(random_result))

for i in range(100):
    random_result = func(0, i)
    print("{}: Ergebnis ist {}".format(i, random_result))

# f-Strings
for i in range(100):
    random_result = func(0, i)
    print(f"{i}: Ergebnis ist {math.sqrt(random_result):.2f}")

# Format String mit Tupel
print('%-7s: %10.6f' % ('Cord', 177.44))