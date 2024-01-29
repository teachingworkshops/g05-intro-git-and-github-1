from scenes import Scenes
class Main_Controller:
    def __init__(self) -> None:
        scenes = Scenes()
        scenes.title_page()
        input("Press Enter to start the game...")
x = Main_Controller()