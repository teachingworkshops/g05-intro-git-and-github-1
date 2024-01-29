from enum import Enum  
from map_structure import Map
class place_object:
    def __init__(self, name,  background):
        self.name = name
        self.background = background
        
class Places:
    RUGGLES = place_object(1, Map.ruggles_background)
    FENWAY_PARK = place_object(2, Map.fenway_park)
    BOSTON_COMMON = place_object(3, Map.boston_common)
    FANEUIL_HALL = place_object(4, Map.faneuil_hall)
    NEW_ENGLAND_AQUARIUM = place_object(5, Map.new_england_aquarium)
    MUSEUM_OF_FINE_ARTS = place_object(6, Map.mfa)
    HARVARD_UNIVERSITY = place_object(7, Map.harvard)
    BOSTON_PUBLIC_LIBRARY = place_object(8, "Boston Public Library")

def find_place_by_number(number):
    for place in Places:
        if place.value == number:
            return place
    return None


    

