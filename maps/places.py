from enum import Enum  
from maps.map_structure import Map
class place_object:
    def __init__(self, number_x, number_y,  background):
        self.x = number_x
        self.y = number_y
        self.background = background
        
class Places(Enum):

    #1st row
    DEFAULT_0_EDGE_LEFT_UP = place_object(0,0, Map.zero_0)
    RUGGLES = place_object(1,0, Map.ruggles_background)
    DEFAULT_0_EDGE_TOP_BOTTOM = place_object(2,0, Map.zero_2)
    DEFAULT_0_TOP = place_object(3,0, Map.zero_3)
    HARVARD_UNIVERSITY = place_object(4,0, Map.harvard)

    #2nd row 
    DEFAULT_1_EDGE_LEFT_0 = place_object(0,1, Map.first_0)
    #default box 
    DEFAULT_1 = place_object(1,1, Map.first_1)
    BLOCKER_1 = place_object(2,1, Map.first_2)
    DEFAULT_1_EDGE_LEFT_1 = place_object(3,1, Map.first_3)
    BOSTON_PUBLIC_LIBRARY = place_object(4,1, Map.boston_public_library)

    #middle row/starting point
    STARTING_POINT = place_object(0,2, Map.second_0)
    BOSTON_COMMON = place_object(1,2, Map.boston_common)
    #dead center of screen when you go into this room you just have to go back
    BLOCKER_2 = place_object(2,2, Map.second_2)
    FANEUIL_HALL = place_object(3,2, Map.faneuil_hall)
    END_POINT = place_object(4,2, Map.end_point_background)

    #3rd row
    DEFAULT_3_EDGE_LEFT_0 = place_object(0,3, Map.third_0)
    MUSEUM_OF_FINE_ARTS = place_object(1,3, Map.mfa)
    DEFAULT_3_EDGE_RIGHT_UP = place_object(2,3, Map.third_2)
    DEFAULT_3_EDGE_LEFT_1 = place_object(3,3, Map.third_3)
    DEFAULT_3_EDGE_RIGHT_0 = place_object(4,3, Map.third_4)

    #4TH row/bottom row
    DEFAULT_4_EDGE_LEFT_BOTTOM_0 = place_object(0,4, Map.fourth_0)
    MIKES_PASTRIES = place_object(1,4, Map.mikes_pastries)
    DEFUALT_4_BOTTOM_0 = place_object(2,4, Map.fourth_2)
    FENWAY_PARK = place_object(3,4, Map.fenway_park)
    NEW_ENGLAND_AQUARIUM = place_object(4,4, Map.new_england_aquarium)
    

def find_background(x,y):
    for place in Places:
        if place.value.x == x and place.value.y == y:
            return place.value.background
    return None



    

