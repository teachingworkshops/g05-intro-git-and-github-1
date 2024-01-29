import room #room module room.py containing Room class
from colorama import Fore, Style #library containing colored

roomList = []

#return a room obj, given its title
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

        newRoom = room.Room(title,desc) #construct a new obj
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
            line = next(dataFile).strip() #continue moving down data file

        #done constructing the room
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

currentRoom = roomDict['STARTINGPOINT']
currentRoom.visited = True

print(Fore.GREEN + Style.BRIGHT + currentRoom.title + ": \n" + Fore.WHITE + Style.RESET_ALL + currentRoom.description + "\n")

print(Fore.YELLOW + Style.BRIGHT + "North: {0}, East: {1}, South: {2}, West: {3}".format(currentRoom.north,currentRoom.east,currentRoom.south,currentRoom.west))

input1 = input(Fore.RESET + Style.RESET_ALL + '>').upper()

while input1 != 'QUIT':
    print(Fore.YELLOW + "=======================================================================" + Fore.RESET)
    previousRoom = currentRoom
    match input1:
        case 'NORTH':
            currentRoom = currentRoom.north
        case 'EAST':
            currentRoom = currentRoom.east
        case 'SOUTH':
            currentRoom = currentRoom.south
        case 'WEST':
            currentRoom = currentRoom.west
        case 'QUIT':
            print ("goodbye.")
        case _: 
            print("Unable to read command")
    if currentRoom == 'NONE':
        print("You can't go that way!")
        currentRoom = previousRoom
    else:
        if not currentRoom.visited:
            #check attributes / events of the room if not yet visited
            if (currentRoom.hasMoney):
                print("You found $" + currentRoom.moneyAmount + " on the floor!")
                #still need to implement player class
            currentRoom.visited = True

    print(Fore.GREEN + Style.BRIGHT + "\n" + currentRoom.title + ": \n" + Fore.WHITE + Style.RESET_ALL + currentRoom.description + "\n")

    print(Fore.YELLOW + Style.BRIGHT + "North: {0}, East: {1}, South: {2}, West: {3}".format(currentRoom.north,currentRoom.east,currentRoom.south,currentRoom.west))
    
    input1 = input(Fore.RESET + Style.RESET_ALL + '>').upper()
            

