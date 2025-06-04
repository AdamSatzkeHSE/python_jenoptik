# Module worthaufigkeit
# Function for word counter
# Autor: Adam Satzke
# Date: 04.06.2025

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

