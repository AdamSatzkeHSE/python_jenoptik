# Fakultät

"""
Schreibe ein Skript, dass ermittelt,
welche Zahl möglichst groß ist,
ohne dass ihre Fakultät über 1.000.000.000 ist.

Hinweis:
Fakultät von 5 (Kurzschreibweise: 5!):
1 * 2 * 3 * 4 * 5 = 120
"""

zahl = 5
result = zahl
print("Factorial", zahl)
while zahl > 1:
    zahl -= 1
    result *= zahl
print(result)

