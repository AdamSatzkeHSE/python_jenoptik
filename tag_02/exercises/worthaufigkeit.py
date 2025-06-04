
# Worthäufigkeiten

# Von den Textdokumenten sollen jeweils die Worthäufigkeiten ermittelt werden.
# Die Ergebnisse sollen sortierte Listen (absteigend nach Häufigkeit)
# von Tupeln der Form (wort, häufigkeit) sein.
# Dabei ist wort ein Wort, das im Text vorkommt
# und häufigkeit die Anzahl der Vorkommen dieses Wortes im Text.
"""
print(ermittleWorthaeufigkeitenAusDatei('Lorem Ipsum.txt'))
print(ermittleWorthaeufigkeitenAusDatei('Kafka.txt'))
print(ermittleWorthaeufigkeitenAusDatei('Werther.txt'))
"""
# Dateien in Python
# Stream: Text-Stream, Binary-Stream

file_stream = open("Kafka.txt", "r")
inhalt = file_stream.read()
# liste_inhalt = file_stream.readlines()

words = inhalt.split()
print(words)
# print("Inhalte: ")
# print(inhalt)
# print(type(inhalt))

# for i in liste_inhalt:
#     print(i)

# Aus der Wörter liste die Häufigkeit jedes Wort auszugeben und in einem Dictionary
# zu speichern.
# dictionary = {
#  "eines" : 6,
#  "Hund" : 2,
#  "sollte" : 8,
# }