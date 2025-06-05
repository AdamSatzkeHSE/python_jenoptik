
# Roboter

# Wir haben folgende Roboterklasse geschrieben:

class RobotError(Exception):
    def __init__(self, message):
        self.message = message

class Robot:
    def __init__(self, name):
        if name == "Hugo":
            # print("Hugo ist deprecated.")
            # raise RobotError("Error Message Roboter Name nicht erlaubt.")
            name = "Marvin"

        self.name = name

# Letzte drei Zeilen:
try:
    x = Robot("Marvin")
    y = Robot("Hugo")
    print(x.name, y.name)  # Marvin Hugo
except RobotError as rb:
    print(rb)

# Hier programmiere ich mein Roboter weiter
print("Weitergehts")
# Diese Klasse erfreut sich nun auf einmal weltweit großer Beliebtheit.
# Wir haben allerdings ein Problem:
# Die internationale Robotergewerkschaft konnte ein weltweites Verbot durchsetzen,
# dass Roboter nicht mehr „Hugo” genannt werden dürfen.
# Schreibe nun die Klasse so um,
# dass Roboter automatisch „Marvin” genannt werden,
# wenn jemand versucht, sie „Hugo” zu taufen
# oder versucht den Roboter in „Hugo” umzubenennen.
# Für die Benutzer der Klasse darf sich natürlich nichts ändern,
# d.h. die letzten drei Zeilen müssen unverändert bleiben können
# (nur muss jetzt zweimal "Marvin" ausgegeben werden).

# Bitte auch das Umbenennen testen:
# Nach dem Versuch, einen Roboter in „Hugo” umzubenennen,
# muss dieser Roboter „Marvin” heissen.