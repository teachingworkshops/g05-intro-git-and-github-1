import os
import msvcrt

def play_game(background, position):


    screen_width = len(background[0])
    screen_height = len(background)
    player_x = screen_width // 2
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
        if x < 0 or x >= screen_width or y < 0 or y >= screen_height:
            return False
        return background[y][x] == " "

    def move_player(x, y):
        if is_valid_move(x, y):
            clear_previous_position()
            background[y] = background[y][:x] + "." + background[y][x + 1:]
            return x, y
        return player_x, player_y

    print("Use WASD keys to move, 'q' to quit")

    while True:
        draw_game()
        ch = getch()

        if ch == b'q':
            print("Thanks for playing!")
            break

        if ch == b'a':
            player_x, player_y = move_player(player_x - 1, player_y)
        elif ch == b'd':
            player_x, player_y = move_player(player_x + 1, player_y)
        elif ch == b'w':
            player_x, player_y = move_player(player_x, player_y - 1)
        elif ch == b's':
            player_x, player_y = move_player(player_x, player_y + 1)

        if player_x == 0:
            print("You hit the left of the screen")
            x = position[0] - 1
            position = (x,position[1])
            print(f"Your position {position} decreased by one in the x direction ")
            break
        elif player_x == screen_width - 1:
            print("You hit the right of the screen")
            x =position[0] + 1 
            position = (x,position[1])
            print(f"Your position {position} increased by one in the x direction ")
            break
        elif player_y == 0:
            print("You hit the top of the screen")
            y = position[1] - 1
            position = (position[0],y)
            print(f"Your position {position} decreased by one in the y direction ")
            break
        elif player_y == screen_height - 1:
            print("You hit the bottom of the screen!")
            y = position[1] + 1
            position = (position[0],y)
            print(f"Your position {position} increased by one in the y direction ")
            break
    
    
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

play_game(background, (2,2))