import os
import msvcrt
from maps.map_structure import Map
from maps.places import find_backround

def play_game(position, entry_point) -> tuple[(int, int), bool, str]:

    #taking the position of the player and finding the background for each one 
    background = find_backround.find_backround(position[0], position[1])

    screen_width = len(background[0])
    screen_height = len(background)
    # To change players starting postion change the player_x and player_y
    #a bunch of if statments is silly but it works for now
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
        player_x = 1
        player_y = screen_height // 2

    def getch():
        return msvcrt.getch()

    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')

    def draw_game():
        clear_screen()

        for row in background:
            print(row)

    def clear_previous_position():
        updated_row = list(background[player_y])
        updated_row[player_x] = " "
        background[player_y] = "".join(updated_row)

    def is_valid_move(x, y):
        # Check if x and y are within the valid range
        if 0 <= y < len(background) and 0 <= x < len(background[y]):
            return background[y][x] == " "
        else:
            return False

    def move_player(x, y):
        if is_valid_move(x, y):
            clear_previous_position()
            background[y] = background[y][:x] + "." + background[y][x + 1:]
            return x, y
        return player_x, player_y


    while True:
        draw_game()
        ch = getch()

        # if ch == b'q':
        #     print("Thanks for playing!")
        #     print(position)

        if ch == b'a':
            player_x, player_y = move_player(player_x - 1, player_y)
        elif ch == b'd':
            player_x, player_y = move_player(player_x + 1, player_y)
        elif ch == b'w':
            player_x, player_y = move_player(player_x, player_y - 1)
        elif ch == b's':
            player_x, player_y = move_player(player_x, player_y + 1)

        if player_x == 0:
            x = position[0] - 1
            position = (x,position[1])
            entry_point = "right"
            break
        elif player_x == screen_width - 1:
            x = position[0] + 1 
            position = (x,position[1])
            entry_point = "left"
            break
        elif player_y == 0:
            y = position[1] - 1
            position = (position[0],y)
            entry_point = "bottom"
            break
        elif player_y == screen_height - 1:
            y = position[1] + 1
            position = (position[0],y)
            entry_point = "top"
            break
    #will change this to return if they won or not 
    if position == (4,2):
        return position, True, entry_point
    return position, False, entry_point
    
    
background = [
        "###############               ###############",
        "#                                           #",
        "#                                           #",
        "#                                           #",
        "#                                           #",
        "                                             ",
        "                                             ",
        "                                             ",
        "                                             ",
        "#                                           #",
        "#                                           #",
        "#                                           #",
        "#                                           #",
        "###############               ###############"
    ]


# play_game(Map.ruggles_background, (2,2))