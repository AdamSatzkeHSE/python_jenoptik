# sys_exc
import sys

try:
    eingabe = input("Geben Sie eine Zahl ein: ")
    x = int(eingabe) / 0
except ZeroDivisionError as error:
    print(error)
    print(error.args)
    print(sys.exc_info())
    print(sys.exc_info()[0])
    print(sys.exc_info()[0].__name__)