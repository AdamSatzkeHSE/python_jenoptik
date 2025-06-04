
# Worthäufigkeiten
# Aufgabenstellung:
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


# Aus der Wörter liste die Häufigkeit jedes Wort auszugeben und in einem Dictionary
# zu speichern.
# dictionary = {
#  "eines" : 6,
#  "Hund" : 2,
#  "sollte" : 8,
# }

# PSEUDOCODE
# 1. Text einlesen X
# 2. Leeres Dictionary vorbereiten
# 3. Wörter separieren
# 4. Worthäufigkeit zählen.
# 5 Dictionary mit Worthäufigkeiten ausgeben

""" Funktionen """
def open_file(filename):
    """ open_file(): Öffnet die gegebene Text-Datei (filename)
    Öffnet einen Stream zur gegebenen Datei im Read-Modus
    Speichert dann die Inhalten in einem Buffer
    return: Buffer mit Inhalten"""
    # Datei im Read Modus öffnen
    file_stream = open(filename, "r")
    # Inhalte lesen und speichern.
    contents = file_stream.read()
    # Wenn ich fertig bin, Stream schließen.
    file_stream.close()
    return contents

def define_filestreams():
    pass

def get_words():
    pass

def count_words():
    pass

""" Main Program """
file_list = ["Kafka.txt", "Lorem Ipsum.txt", "Werther.txt"]
content_list = []
# File Streams definieren:
for file in file_list:
    print("Filename: {}".format(file))
    content = open_file(file)
    content_list.append(content)
    # print(content)

# Dictionary for output. Get words in lists.
result = {}
words_list = []
for content in content_list:
    words = content.split()
    words_list.append(words)
for i in words_list:
    print(i)

# Count words
output = []
for liste in words_list:
    result = {}
    for word in liste:
        result[word] = liste.count(word)
    output.append(result)

for ergebnis in output:
    print(ergebnis)