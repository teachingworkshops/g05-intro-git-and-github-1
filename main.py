import room_manager as rm #room module room.py containing Room class
import player_manager as pm
import os
import os.path
import sys,time
import msvcrt
from scenes import Scenes
from maps.map_structure import Map
from colorama import Fore, Style #library containing colored

highScore = 0
def getch():
    return msvcrt.getch()

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    reset = False

    #Code for setting up for exe assuming exe is in downloads inside dist folder
    #downloads = os.path.join(os.path.expanduser('~'), 'Downloads')
    #file_name = "dist\main.exe"
    #game_path = os.path.join(downloads, file_name)


    #reload scene after
    def draw_game(x,y):
        clear_screen()

        print(playerStatsMessage)

        print(messageLog)

        print(Fore.GREEN + Style.BRIGHT + currentRoom.title + ": \n" + Fore.WHITE + Style.RESET_ALL + currentRoom.description.replace('\\n','\n') + "\n") #replace the implicit \n's in txt with actual line breaks

        print(Fore.YELLOW + Style.BRIGHT + "North: {0}, East: {1}, South: {2}, West: {3}".format(str(currentRoom.north) + (' (blocked)' if currentRoom.northBlocked else ''),str(currentRoom.east) + (' (blocked)' if currentRoom.eastBlocked else ''),str(currentRoom.south) + (' (blocked)' if currentRoom.southBlocked else ''),str(currentRoom.west) + (' (blocked)' if currentRoom.westBlocked else '')))

        print(Fore.WHITE)
        
        print("\r"+("\n").join(background)) #separate each element with \n

    def clear_previous_position(tile): #replace previous position with the tile the player was on
        updated_row = list(background[player.y])
        updated_row[player.x] = tile
        background[player.y] = "".join(updated_row)

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
        return player.x, player.y

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
    #CREATE PLAYER
    player = pm.Player()
    currentRoom = rm.getRoomByName('STARTINGPOINT')
    currentRoom.visited = True

    background = currentRoom.background
    screen_width = len(background[0])
    screen_height = len(background)

    currentTile = ' '

    player.x = screen_width // 2
    player.y = screen_height // 2
    move_player(player.x,player.y,' ')
    won = False

    inputCmd = ''
    #GAME LOOP
    while inputCmd != 'QUIT' and inputCmd != 'RESET':
        background = currentRoom.background
        screen_width = len(background[0])
        screen_height = len(background)

        messageLog = ""
        #apply current room attributes
        if not currentRoom.visited:
            #add score for each unique room visited
            player.score += 100 
            #check attributes / events of the room if not yet visited
            if (currentRoom.hasMoney):
                messageLog = "You found $" + currentRoom.moneyAmount + " on the floor!"
                player.score += round(float(currentRoom.moneyAmount)) * 100
                player.money += float(currentRoom.moneyAmount)
            #win condition
            if currentRoom.title == 'HOME':
                messageLog = "YOU WIN!"
                player.score += 5000

                path = './scores.txt' #file with high scores path
                #if the file exists
                if os.path.isfile(path):
                    #open the file to read from it. and use readlines to create a list of strings
                    with open(path, 'r') as scores_file:
                        existing_scores = scores_file.readlines()
    
                #if the list is empty 
                    if not existing_scores:
                        #open the file to write to it, and write the player's current score
                        with open(path, 'w') as scores_file:
                            scores_file.write(str(player.score))
                #if the list is not empty   
                    else:
                        #always make the high_score the first line of the file aka. element 0 in the existing_scores list
                        high_score = int(existing_scores[0].strip())
                        #now if the current score of the player is bigger than the previous high score
                        if player.score > high_score:
                            #open the file, now to write to it, write the current score.
                            with open(path, 'w') as scores_file:
                                scores_file.write(str(player.score))
                        else:
                            pass
                else:
                    with open(path, 'w') as scores_file:
                        scores_file.write(str(player.score))
                
                won = True
                break


            if currentRoom.unlocksRoom:
                rm.getRoomByName(currentRoom.roomUnlocks).unlockAll()
                messageLog = currentRoom.roomUnlocksDesc.replace('\\n','\n') + "\n"
            currentRoom.visited = True
        
        playerStatsMessage = ("Score: {}    Money: ${:.2f}").format(player.score,player.money) 

        if entry_point == "left":
            player.x = 1
            player.y = screen_height // 2
        elif entry_point == "right":
            player.x = screen_width - 2
            player.y = screen_height // 2
        elif entry_point == "top":
            player.x = screen_width // 2
            player.y = 1
        elif entry_point == "bottom":
            player.x = screen_width // 2
            player.y = screen_height - 2
        else:
            player.x = screen_width // 2
            player.y = screen_height // 2
        
        player.x,player.y = move_player(player.x,player.y,currentTile) #update player pos
        #inner loop
        while True:
            draw_game(player.x,player.y)
            ch = getch()

            #remember this tile
            previousTile = currentTile
            if ch == b'a':         
                #update the tile
                currentTile = get_tile_after_move(player.x - 1, player.y)
                player.x, player.y = move_player(player.x - 1, player.y, previousTile)
            elif ch == b'd':
                currentTile = get_tile_after_move(player.x + 1, player.y)
                player.x, player.y = move_player(player.x + 1, player.y, previousTile)
            elif ch == b'w':
                currentTile = get_tile_after_move(player.x, player.y - 1)
                player.x, player.y = move_player(player.x, player.y - 1, previousTile)
            elif ch == b's':
                currentTile = get_tile_after_move(player.x, player.y + 1)
                player.x, player.y = move_player(player.x, player.y + 1, previousTile)
            else:
                print("Commands: QUIT to quit, MAP to open map, ENTER to continue, RESET to reset")
                inputCmd = input(Fore.RESET + Style.RESET_ALL + '>').upper()
                if inputCmd == 'QUIT':
                    break
                if inputCmd == 'RESET':           
                    reset = True
                    break

                if inputCmd =='MAP' or inputCmd == 'M':
                    print(Map.map)
                    second_user_input = input("Type place of interest to view the description\nOr press Enter to continue...\n")
                    if second_user_input.lower() == "ruggles":
                        print(Map.ruggles_description)
                    elif second_user_input.lower() == "boston common":
                        print(Map.boston_common_description)
                    elif second_user_input.lower() == "library":
                        print(Map.library_description)
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
            if player.x == 0: #x position relative to what's on the screen
                #WEST
                if currentRoom.westBlocked or currentRoom.west == 'NONE':
                    messageLog=("You can't go west!")
                    player.x, player.y = move_player(player.x + 1, player.y,previousTile)
                else:
                    entry_point = "right"
                    clear_previous_position(previousTile)
                    currentRoom = currentRoom.west
                    break
            elif player.x == screen_width - 1:
                #EAsT
                if currentRoom.eastBlocked or currentRoom.east == 'NONE':
                    messageLog=("You can't go east!")
                    player.x, player.y = move_player(player.x - 1, player.y,previousTile)
                else:
                    entry_point = "left"
                    clear_previous_position(previousTile)
                    currentRoom = currentRoom.east
                    break
            elif player.y == 0:
                #NORTH
                if currentRoom.northBlocked or currentRoom.north == 'NONE':
                    messageLog=("You can't go north!")
                    player.x, player.y = move_player(player.x, player.y + 1,previousTile)
                else:
                    entry_point = "bottom"
                    clear_previous_position(previousTile)
                    currentRoom = currentRoom.north
                    break
            elif player.y == screen_height - 1:
                #SOUTH
                if currentRoom.southBlocked or currentRoom.south == 'NONE':
                    messageLog=("You can't go south")
                    player.x, player.y = move_player(player.x, player.y - 1,previousTile)
                else:
                    entry_point = "top"
                    clear_previous_position(previousTile)
                    currentRoom = currentRoom.south
                    break

            
    #after quit
    if won:
        clear_screen()
        Scenes().ending_page()

        print("Final score: " + str(player.score) +"\n")
        print("Enter QUIT to quit or REPLAY to play again")
        inputCmd = input(Fore.RESET + Style.RESET_ALL + '>').upper()

        if inputCmd == 'QUIT':
            print("Thanks for playing!")
        elif inputCmd == 'REPLAY':
            reset = True

    #after reset
    if reset == True:
        clear_screen()
        os.system('python main.py')

        #code for exe setup
        #os.startfile(game_path)
    else:
        #after quit
        print ("goodbye.")

if (__name__) == '__main__':
    main() 