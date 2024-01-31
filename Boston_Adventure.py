from scenes import Scenes
import movement
from maps.map_structure import Map
class Main_Controller:
    def __init__(self) -> None:
        scenes = Scenes()
        scenes.title_page()
        #need to add description of the game
        input("Press Enter to start the game...")
        #defining the player's starting position and if they won or not
        conditions = ((0,2), False, "left")
        while conditions[1] == False:
            conditions = movement.play_game(conditions[0], conditions[2])
            user_input = input("Press Enter to continue...\nPress m to view the map...\nPress q to quit the game...\n")
            if user_input == "m":
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
            if user_input == "q":
                print("Thanks for playing!")
                break
            else:
                pass
x = Main_Controller()