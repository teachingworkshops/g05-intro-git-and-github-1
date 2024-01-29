from enum import Enum  
class place_object:
    def __init__(self, name,  background):
        self.name = name
        self.background = background
        
class Places:
    RUGGLES = place_object(1, "Ruggles")
    FENWAY_PARK = place_object(2, "Fenway")
    BOSTON_COMMON = place_object(3, "Boston Common")
    FANEUIL_HALL = place_object(4, "Faneuil Hall")
    NEW_ENGLAND_AQUARIUM = place_object(5, "Aquarium")
    MUSEUM_OF_FINE_ARTS = place_object(6, "MFA")
    HARVARD_UNIVERSITY = place_object(7, "Harvard")
    BOSTON_PUBLIC_LIBRARY = place_object(8, "Boston Public Library")

def find_place_by_number(number):
    for place in Places:
        if place.value == number:
            return place
    return None


    

