# alias
import traceback
import sys

try:
    eingabe = input()
    eingabe = int(eingabe)
    x = eingabe / 0
except ZeroDivisionError as ex:
    print("Man darf durch 0 nicht teilen")
    print(ex)
    print(ex.args)
    print(type(ex))
    traceback.print_exc(file=sys.stdout)

