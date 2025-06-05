# Roboter 2

# In dieser Aufgabe geht wieder um eine Roboterklasse.
# Uns interessiert nicht das Aussehen und die Beschaffenheit eines Roboters,
# sondern nur seine Position in einer imaginären „Landschaft”,
# die zweidimensional sein soll
# und durch ein Koordinatensystem beschrieben werden kann.
# Ein Roboter hat also zwei Attribute für die x- und die y-Koordinate.
# Es empfiehlt sich, diese Informationen in einer 2er-Liste zusammenzufassen,
# also beispielsweise position = [3, 4],
# wobei dann 3 der x-Position und 4 der y-Position entspricht.
# Der Roboter ist in eine der vier Richtungen „west”, „south”, „east”
# oder „north” orientiert, was wir in einem Attribut speichern wollen.
# Außerdem sollten unsere Roboter auch Namen haben.
# Allerdings dürfen die Namen nicht länger als 10 Zeichen sein.
# Sollte jemand versuchen,
# dem Roboter einen längeren Namen zuzuweisen,
# soll der Name auf 10 Zeichen abgeschnitten werden.
# Um die Roboter im Koordinatensystem bewegen zu können,
# benötigen wir eine move()-Methode.
# Die Methode erwartet einen Parameter „distance”,
# der angibt, um welchem Betrag sich der Roboter in Richtung
# der eingestellten Orientierung bewegen soll.
# Wird ein Roboter x beispielsweise mit x.move(10) aufgerufen
# und ist dieser Roboter östlich orientiert,
# also x.orientation == "east", und ist [3, 7] die aktuelle Position des
# Roboters, dann bewegt er sich 10 Felder östlich
# und befindet sich anschließend in Position [13, 7].

class Robot:
    """
    Roboter Klasse
    """
    # Klassenvariable *orientations*: liste mit erlaubten Orientations.
    # Gültig für alle Roboter Instanzen.
    orientations = ["west", "north", "south", "east"]

    def __init__(self, name, x, y, orientation):
        # Attribute
        self.x = x
        self.y = y
        if orientation not in Robot.orientations:
            raise Exception("Orientation {} nicht erlaubt".format(orientation))
        self.orientation = orientation
        self.position = [self.x, self.y]
        # Kurze Lösung mit String - Slicing.
        self.name = name[:10]   # Nehme immer nur die ersten 10 Buchstaben
        # Lange Lösung.
        # self.name = ''
        # if len(name) > 10:
        #     for i in range(10):
        #         self.name += name[i]

    def move(self, distance):
        """
        Erwartet ein Parameter distance, der angibt, um welchem Betrag
        sich der Roboter in Richtung der eingestellten Orientierung bewegen soll.
        Wird der Roboter bswp. mit move(10) aufgerufen, und ist er östlich orientiert,
        dann bewegt er sich östlich um 10 Felder. Position wird dementsprechend
        aktualisiert.
        """
        if self.orientation == "north":
            self.position[1] += distance
        elif self.orientation == "south":
            self.position[1] -= distance
        elif self.orientation == "west":
            self.position[0] -= distance
        elif self.orientation == "east":
            self.position[0] += distance
        else:
            raise ValueError("Orientierung nicht erkannt.")

if __name__ == '__main__':
    # Test main module here
    robot = Robot("Marvin123456790", 0, 0, "west")
    print(robot.orientation)
    print(robot.name)
    # Init: pos = [0,0], orientation = "west"
    # move(10)
    # output: pos = [-10, 0]
    print("Anfang: ", robot.position)
    robot.move(10)
    print("Ende: ", robot.position)
    robot.orientation = "south"
    robot.move(2)
    robot.orientation = "east"
    robot.move(4)
    print(robot.position)

