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
BLOCKED:[NORTH/EAST/SOUTH/WEST] - blocks another room

#HOW TO BUILD USING PYINSTALLER

make sure to pip install pyinstaller first

run this command in the VsCode terminal: python -m PyInstaller --onefile --add-data="data.txt;." --add-data="background_data.txt;." main.py

The -m flag is, at its simplest, a means to execute python scripts
from the command line by using modulenames rather than filenames.
--onefile includes all related modules in the exe 
--add-data includes the data text files in the exe