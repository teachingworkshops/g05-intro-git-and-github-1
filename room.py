class Room:
    #CONSTRUCTOR
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.north = None #type Room
        self.east = None
        self.south = None
        self.west = None
    #TO STRING
    def __str__(self):
        return self.title

    def setNorth(self, room):
        self.north = room
    def setSouth(self, room):
        self.south = room

    #need to implement setEast, south and west

#end Room class    