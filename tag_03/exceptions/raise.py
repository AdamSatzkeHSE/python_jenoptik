# raise
# Schlüßelwort
# Zum Werfen von Exceptions

import traceback
import sys

def func(zahl):
    if type(zahl) != int:
        raise TypeError("Die Zahl muss vom Type Integer sein!")
    if zahl <= 0:
        raise ValueError("Die Zahl muss positiv sein!")
    print("Alles in Ordnung. Sie haben eine {} eingeben.".format(zahl))

try:
    func(-7)
except (TypeError, ValueError) as error:
    print("Fehler wurde abgefangen.")
    print(error)
    traceback.print_exc(file=sys.stdout)

print("Hier gehts weiter.")