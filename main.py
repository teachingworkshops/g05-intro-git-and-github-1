import room_manager as rm #room module room.py containing Room class
import os
import msvcrt
from scenes import Scenes
from maps.map_structure import Map
from colorama import Fore, Style #library containing colored

def getch():
    return msvcrt.getch()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

#reload scene after
def draw_game(x,y):
    clear_screen()

    #print(x)
    #print(y)
    print(messageLog)

    print(Fore.GREEN + Style.BRIGHT + currentRoom.title + ": \n" + Fore.WHITE + Style.RESET_ALL + currentRoom.description.replace('\\n','\n') + "\n") #replace the implicit \n's in txt with actual line breaks

    print(Fore.YELLOW + Style.BRIGHT + "North: {0}, East: {1}, South: {2}, West: {3}".format(str(currentRoom.north) + (' (blocked)' if currentRoom.northBlocked else ''),str(currentRoom.east) + (' (blocked)' if currentRoom.eastBlocked else ''),str(currentRoom.south) + (' (blocked)' if currentRoom.southBlocked else ''),str(currentRoom.west) + (' (blocked)' if currentRoom.westBlocked else '')))

    print(Fore.WHITE)
    
    for row in background:
        print(row)

def clear_previous_position(tile): #replace previous position with the tile the player was on
    updated_row = list(background[player_y])
    updated_row[player_x] = tile
    background[player_y] = "".join(updated_row)

def is_valid_move(x, y):
    # Check if x and y are within the valid range
    if 0 <= y < len(background) and 0 <= x < len(background[y]):
        return background[y][x] != "#" #return true if the tile is an open space and not a wall (denoted by # symbol)
    else:
        return False

def move_player(x, y, tile): #tile is a variable to remember the tile that the player moved from
    if is_valid_move(x, y):
        clear_previous_position(tile)
        background[y] = background[y][:x] + "@" + background[y][x + 1:]
        return x, y
    return player_x, player_y

#gets the tile player lands on after moving
def get_tile_after_move(x,y):
    if is_valid_move(x, y):
        return background[y][x]
    #else
    return currentTile

#TITLE
Scenes().title_page()
#need to add description of the game
input("Press Enter to start the game...")

#INITIALIZATION
entry_point = ""

currentRoom = rm.getRoomByName('STARTINGPOINT')
currentRoom.visited = True

background = currentRoom.background
screen_width = len(background[0])
screen_height = len(background)

currentTile = ' '

player_x = screen_width // 2
player_y = screen_height // 2
move_player(player_x,player_y,' ')



inputCmd = ''
#GAME LOOP
while inputCmd != 'QUIT':
    background = currentRoom.background
    tempBackground = background
    
    screen_width = len(background[0])
    screen_height = len(background)

    messageLog = ""
    #apply room attributes
    if not currentRoom.visited:
        #check attributes / events of the room if not yet visited
        if (currentRoom.hasMoney):
            messageLog = "You found $" + currentRoom.moneyAmount + " on the floor!"
            #still need to implement player class
        #win condition
        if currentRoom.title == 'HOME':
            messageLog = "YOU WIN!"
        currentRoom.visited = True
     
    if entry_point == "left":
        player_x = 1
        player_y = screen_height // 2
    elif entry_point == "right":
        player_x = screen_width - 2
        player_y = screen_height // 2
    elif entry_point == "top":
        player_x = screen_width // 2
        player_y = 1
    elif entry_point == "bottom":
        player_x = screen_width // 2
        player_y = screen_height - 2
    else:
        player_x = screen_width // 2
        player_y = screen_height // 2
    
    player_x,player_y = move_player(player_x,player_y,currentTile) #update player pos
    #inner loop
    while True:
        draw_game(player_x,player_y)
        ch = getch()

        #remember this tile
        previousTile = currentTile
        if ch == b'a':         
            #update the tile
            currentTile = get_tile_after_move(player_x - 1, player_y)
            player_x, player_y = move_player(player_x - 1, player_y, previousTile)
        elif ch == b'd':
            currentTile = get_tile_after_move(player_x + 1, player_y)
            player_x, player_y = move_player(player_x + 1, player_y, previousTile)
        elif ch == b'w':
            currentTile = get_tile_after_move(player_x, player_y - 1)
            player_x, player_y = move_player(player_x, player_y - 1, previousTile)
        elif ch == b's':
            currentTile = get_tile_after_move(player_x, player_y + 1)
            player_x, player_y = move_player(player_x, player_y + 1, previousTile)
        else:
            print("Commands: QUIT to quit, MAP to open map")
            inputCmd = input(Fore.RESET + Style.RESET_ALL + '>').upper()
            if inputCmd == 'QUIT':
                break
            if inputCmd =='MAP' or inputCmd == 'M':
                print(Map.map)
                second_user_input = input("Type place of interest to view the description\nOr press Enter to continue...\n")
                if second_user_input.lower() == "ruggles":
                    print(Map.ruggles_description)
                elif second_user_input.lower() == "boston common":
                    print(Map.boston_common_description)
                elif second_user_input.lower() == "library":
                    print(Map.boston_public_library_description)
                elif second_user_input.lower() == "faneuil hall":
                    print(Map.faneuil_hall_description)
                elif second_user_input.lower() == "mfa":
                    print(Map.mfa_description)
                elif second_user_input.lower() == "mikes pastries":
                    print(Map.mikes_pastries_description)
                elif second_user_input.lower() == "fenway park":
                    print(Map.fenway_park_description)
                elif second_user_input.lower() == "aquarium":
                    print(Map.new_england_aquarium_description)
                elif second_user_input.lower() == "harvard":
                    print(Map.harvard_description)
                else:
                    pass
                input("Press Enter to continue...")
            clear_screen()
            continue  
        if player_x == 0: #x position relative to what's on the screen
            #WEST
            if currentRoom.westBlocked or currentRoom.west == 'NONE':
                messageLog=("You can't go west!")
                player_x, player_y = move_player(player_x + 1, player_y,previousTile)
            else:
                entry_point = "right"
                clear_previous_position(previousTile)
                currentRoom = currentRoom.west
                break
        elif player_x == screen_width - 1:
            #EAsT
            if currentRoom.eastBlocked or currentRoom.east == 'NONE':
                messageLog=("You can't go east!")
                player_x, player_y = move_player(player_x - 1, player_y,previousTile)
            else:
                entry_point = "left"
                clear_previous_position(previousTile)
                currentRoom = currentRoom.east
                break
        elif player_y == 0:
            #NORTH
            if currentRoom.northBlocked or currentRoom.north == 'NONE':
                messageLog=("You can't go north!")
                player_x, player_y = move_player(player_x, player_y + 1,previousTile)
            else:
                entry_point = "bottom"
                clear_previous_position(previousTile)
                currentRoom = currentRoom.north
                break
        elif player_y == screen_height - 1:
            #SOUTH
            if currentRoom.southBlocked or currentRoom.south == 'NONE':
                messageLog=("You can't go south")
                player_x, player_y = move_player(player_x, player_y - 1,previousTile)
            else:
                entry_point = "top"
                clear_previous_position(previousTile)
                currentRoom = currentRoom.south
                break
        
        
#after quit
print ("goodbye.")

