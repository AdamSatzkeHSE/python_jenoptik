
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

def get_words_list(content_list):
    """
    Get the words of each list with split.
    Return a new list. Each Element in the list is a new list with words as elements.
    """
    words_list = []
    for content in content_list:
        words = content.split()
        words_list.append(words)
    return words_list

def count_words(words_list):
    output = []
    for liste in words_list:
        result = {}
        for word in liste:
            result[word] = liste.count(word)
        output.append(result)
    return output

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
words_list = get_words_list(content_list)
# Count words and create dictionary with end result.
result = count_words(words_list)
for dictionary in result:
    sorted_dictionary = dict(sorted(dictionary.items(), key= lambda x: x[1], reverse=True))
    print(sorted_dictionary)

