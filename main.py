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

r1 = Room("STARTING POINT", "you start in this room.")
r2 = Room("RUGGLES", "ruuggles street")

r1.setNorth(r2) 
r2.setSouth(r1) 

print(r1.title + ": \n" + r1.description + "\n")

print("North: {0}, East: {1}, South: {2}, West: {3}".format(r1.north,r1.east,r1.south,r1.west))


