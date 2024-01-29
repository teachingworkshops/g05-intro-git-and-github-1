#DATA FORMATTING CONVENTION
[
NAME
DESC:DESCRIPTION
N:NAME E:NAME S:NAME W:NAME #Replace NAME with the name of the adjaecent location, or NONE if no location

#Any other room attributes below may be unordered


]



ENDDATA

#LIST OF POSSIBLE ROOM ATTRIBUTES
HASMONEY:[FLOAT AMOUNT] - this room has money lying around. when this room is visited for the first time, it will give an amount of money
HASITEM:[ITEM ID] - this room has a pickable item. when vistied for the first time, it will add the item to the player's inventory