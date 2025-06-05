# finally
# Wird in jedem Fall ausgeführt.

try:
    eingabe = '0'
    # eingabe = '1'
    eingabe = int(eingabe)
    print("Division: {}".format(10 / eingabe))
except ZeroDivisionError:
    print("Durch 0 darf man nicht teilen.")
finally:
    print("Fertig mit dem try-except Block")

print("Hier gehts weiter.")