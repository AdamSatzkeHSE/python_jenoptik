# Exceptions
# else
# Für den Fall, dass im try kein Fehler geworfen wird.

try:
    print("Ergebnis")
    x = 1 / 0
except ValueError:
    print("ValueError")
except ZeroDivisionError:
    print("Durch 0 darf man nicht teilen.")
else:
    print("Keine Fehler.")

print("Hier gehts weiter.")