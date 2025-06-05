# assert
# Nach dem assert muss ein Ausfruck stehen, der zu einem Boolean evaluiert

# assert 1 == 1
# assert 1 == 0

try:
    limit = input("Setzen Sie eine Grenze: ")
    limit = int(limit)
    assert limit < 100
except AssertionError:
    print("Geben Sie eine Grenze unterhalb von 100 bitte.")
else:
    print("Grenze {} wurde eingestellt".format(limit))
finally:
    print("Finally")