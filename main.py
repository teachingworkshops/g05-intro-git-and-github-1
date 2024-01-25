import room

r1 = room.Room("STARTING POINT", "you start in this room.")
r2 = room.Room("RUGGLES", "ruuggles street")

r1.setNorth(r2) 
r2.setSouth(r1) 

print(r1.title + ": \n" + r1.description + "\n")

print("North: {0}, East: {1}, South: {2}, West: {3}".format(r1.north,r1.east,r1.south,r1.west))


