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

#initialize rooms
roomList = []

#dictionary to return a room obj, given its name
roomDict = {}

dataFile = open('data.txt','r') #read mode
line = next(dataFile).strip() #datafile is an iter
#initialize rooms
while line != 'ENDDATA':
    if line == '[': #Detected a new room to be created
        title = next(dataFile).strip() #important to strip those new lines
        desc = next(dataFile).strip()[5:] #remove DESC: part

        compass =  next(dataFile).strip()
        directions = compass.split() #split spaces

        newRoom = Room(title,desc) #construct a new obj
        newRoom.setNorth(directions[0][2:]) # [2:] removes first two characters, the N: E: S: W: parts
        newRoom.setEast(directions[1][2:])
        newRoom.setSouth(directions[2][2:])
        newRoom.setWest(directions[3][2:])
        
        line = next(dataFile).strip()

        #start reading attributes of a room
        while line != ']': #while not at the end of room definition
            splitLine = line.split(':')
            #splitLine[0] is the attribute keyword
            if splitLine[0] == 'HASMONEY':
                #print("THIS ROOM IS LOADED")
                newRoom.moneyAmount = splitLine[1]
                newRoom.hasMoney = True
            if splitLine[0] == 'BLOCKED':
                match splitLine[1].upper():
                    case 'NORTH':
                        newRoom.northBlocked = True
                    case 'EAST':
                        newRoom.eastBlocked = True
                    case 'SOUTH':
                        newRoom.southBlocked = True
                    case 'WEST':
                        newRoom.westBlocked = True
            line = next(dataFile).strip() #continue moving down data file until reached end of room def

        #done constructing the room, add it to the list
        roomList.append(newRoom)
        roomDict[title.upper()] = newRoom
    line = next(dataFile).strip()
        
dataFile.close()

#update room pointers, converting from string to room obj
for r in roomList:
    if r.north != 'NONE':
        r.setNorth(roomDict[r.north])
    if r.east != 'NONE':
        r.setEast(roomDict[r.east])
    if r.south != 'NONE':
        r.setSouth(roomDict[r.south])
    if r.west != 'NONE':
        r.setWest(roomDict[r.west])

def getRoomByName (id):
    return roomDict[id]

def getRoomList():
    return roomList
