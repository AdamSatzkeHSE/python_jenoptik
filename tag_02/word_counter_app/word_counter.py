from modules import worthaufigkeit as wh
from modules import statistic as st

# Alle Inhalte mit Alis wh importieren.
# import modules.worthaufigkeit as wh
# Alle Inhalte nach Name importieren.
# from modules.worthaufigkeit import *
# Nur spezifische Inhalte importieren
# from modules.worthaufigkeit import word_counter

import os
# import sys

""" Main Program """
# file_list = ["./data/Kafka.txt", "./data/Lorem Ipsum.txt", "./data/Werther.txt"]
file_list = []

# print("Aktuelles Arbeitsverzeichnis: {}".format(os.getcwd()))
print("File list")
print("Inhalte CWD: ", os.listdir())
for file in os.listdir():
    print(file)

os.chdir("data")
print(os.getcwd())
content_list = []

for file in os.listdir():
    file_list.append(file)

# File Streams definieren:
for file in file_list:
    print("Filename: {}".format(file))
    content = wh.open_file(file)
    content_list.append(content)
    # print(content)

# Dictionary for output. Get words in lists.
words_list = wh.get_words_list(content_list)
# Count words and create a dictionary with an end result.
result = wh.count_words(words_list)
for dictionary in result:
    sorted_dictionary = dict(sorted(dictionary.items(), key= lambda x: x[1], reverse=True))
    print(sorted_dictionary)

