import room_manager as rm #room module room.py containing Room class
from colorama import Fore, Style #library containing colored

def printTitle():
    #image to braille source - https://505e06b2.github.io/Image-to-Braille/
    print(Fore.CYAN + Style.BRIGHT + "     MBTA SIMULATOR 2K24\n")
    print(('⠄⠄⠄⠄⠄⠄⠄⠄⣀⣤⣤⠶⠖⠛⠛⠛⠛⠲⠶⣤⣤⣀⠄⠄⠄⠄⠄⠄⠄⠄\n⠄⠄⠄⠄⠄⣠⣤⠟⠛⠉⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠛⠻⣦⣄⠄⠄⠄⠄⠄\n⠄⠄⠄⣠⣴⠛⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠛⣦⣄⠄⠄⠄\n⠄⠄⣤⠟⠁⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠈⠛⣦⠄⠄\n⠄⣼⡟⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠻⣧⠄\n⢠⡟⠄⠄⠄⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠄⠄⠄⢹⡄\n⣼⠁⠄⠄⠄⠉⠉⠉⠉⠉⠉⠉⢹⣿⣿⣿⣿⡏⠉⠉⠉⠉⠉⠉⠉⠄⠄⠄⠈⣷\n⣿⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣿\n⢻⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⡿\n⠘⣧⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣸⠃\n⠄⢻⣦⠄⠄⠄⠄⠄⠄⠄⠄⠄⢸⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⠄⠄⣴⡿⠄\n⠄⠄⠻⣦⡀⠄⠄⠄⠄⠄⠄⠄⢸⣿⣿⣿⣿⡇⠄⠄⠄⠄⠄⠄⠄⢀⣤⠟⠁⠄\n⠄⠄⠄⠙⠻⣄⡀⠄⠄⠄⠄⠄⠈⠉⠉⠉⠉⠁⠄⠄⠄⠄⠄⠄⣠⡾⠛⠄⠄⠄\n⠄⠄⠄⠄⠄⠙⠻⣤⣤⡀⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⣠⣤⠟⠛⠄⠄⠄⠄⠄\n⠄⠄⠄⠄⠄⠄⠄⠈⠙⠛⠳⠦⣤⣤⣤⣤⣤⣤⠶⠞⠛⠋⠁⠄⠄⠄⠄⠄⠄⠄').replace('⠄',' '))
    print(Fore.RESET + Style.RESET_ALL + "\n")

#was player able to move?
moved = False

printTitle()

currentRoom = rm.getRoomByName('STARTINGPOINT')
currentRoom.visited = True

print(Fore.GREEN + Style.BRIGHT + currentRoom.title + ": \n" + Fore.WHITE + Style.RESET_ALL + currentRoom.description.replace('\\n','\n') + "\n") #replace the implicit \n's in txt with actual line breaks

print(Fore.YELLOW + Style.BRIGHT + "North: {0}, East: {1}, South: {2}, West: {3}".format(str(currentRoom.north) + (' (blocked)' if currentRoom.northBlocked else ''),str(currentRoom.east) + (' (blocked)' if currentRoom.eastBlocked else ''),str(currentRoom.south) + (' (blocked)' if currentRoom.southBlocked else ''),str(currentRoom.west) + (' (blocked)' if currentRoom.westBlocked else '')))

input1 = input(Fore.RESET + Style.RESET_ALL + '>').upper()

while input1 != 'QUIT':
    print(Fore.YELLOW + "=======================================================================" + Fore.RESET)
    previousRoom = currentRoom
    moved = False
    match input1:
        case 'NORTH':
            if (currentRoom.northBlocked):
               currentRoom == 'BLOCKED' #currentRoom will act as an error code string
            else:
                currentRoom = currentRoom.north
                moved = True
        case 'EAST':
            if (currentRoom.eastBlocked):
                currentRoom == 'BLOCKED'
            else:
                currentRoom = currentRoom.east
                moved = True
        case 'SOUTH':
            if (currentRoom.southBlocked):
                currentRoom == 'BLOCKED'
            else:
                currentRoom = currentRoom.south
                moved = True
        case 'WEST':
            if (currentRoom.westBlocked):
                currentRoom == 'BLOCKED'
            else:
                currentRoom = currentRoom.west
                moved = True
        case _: 
            currentRoom = 'UNKNOWN' #currentRoom will act as an error code string
    if currentRoom == 'NONE':
        print("You can't go that way!")
        currentRoom = previousRoom
        moved = False
    elif currentRoom == 'UNKNOWN':
        print("Unable to read command")
        currentRoom = previousRoom
        moved = False
    elif currentRoom =='BLOCKED':
         print("That way is blocked!")
         currentRoom = previousRoom
         moved = False
    if moved:
        print("You head " + input1.lower())
        if not currentRoom.visited:
            #check attributes / events of the room if not yet visited
            if (currentRoom.hasMoney):
                print("You found $" + currentRoom.moneyAmount + " on the floor!")
                #still need to implement player class
            currentRoom.visited = True
    
    print(Fore.GREEN + Style.BRIGHT + currentRoom.title + ": \n" + Fore.WHITE + Style.RESET_ALL + currentRoom.description.replace('\\n','\n') + "\n") #replace the implicit \n's in txt with actual line breaks

    print(Fore.YELLOW + Style.BRIGHT + "North: {0}, East: {1}, South: {2}, West: {3}".format(str(currentRoom.north) + (' (blocked)' if currentRoom.northBlocked else ''),str(currentRoom.east) + (' (blocked)' if currentRoom.eastBlocked else ''),str(currentRoom.south) + (' (blocked)' if currentRoom.southBlocked else ''),str(currentRoom.west) + (' (blocked)' if currentRoom.westBlocked else '')))
    
    input1 = input(Fore.RESET + Style.RESET_ALL + '>').upper()
            
#after quit
print ("goodbye.")

