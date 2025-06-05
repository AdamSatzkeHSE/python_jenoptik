# FileNotFoundError

try:
    filename = "test.txt"
    stream = open(filename, "r")
    inhalte = stream.read()
    stream.close()
except FileNotFoundError:
    print("Datei \"{}\" existiert nicht!".format(filename))

