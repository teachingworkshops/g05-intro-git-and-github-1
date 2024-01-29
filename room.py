class Room:
    #CONSTRUCTOR
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.north = None #type String, this is a 
        self.east = None
        self.south = None
        self.west = None

        self.visited = False

        self.northBlocked = False
        self.eastBlocked = False
        self.southBlocked = False
        self.westBlocked = False

        self.hasMoney = False
        self.moneyAmount = 0.00

        self.hasItem = False
        self.itemID = "" #type string
    #TO STRING
    def __str__(self):
        return self.title

    def setNorth(self, room):
        self.north = room
    def setSouth(self, room):
        self.south = room
    def setEast(self, room):
        self.east = room
    def setWest(self, room):
        self.west = room

#end Room class    