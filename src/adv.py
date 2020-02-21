from room import Room
from player import Player
import argparse

# Declare all the rooms
# https://www.futurelearn.com/courses/object-oriented-principles/0/steps/31490
# ADDING ITEM VERSUS LIST OF ITEMS TO LIST https://www.geeksforgeeks.org/append-extend-python/
itemnames = ["sheild", "hammer"]
itemdescript = ["weapon", "tool"]

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", 'foyer', 'outside', 'outside', 'outside', itemnames, itemdescript),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", 'overlook', 'outside', 'foyer', 'foyer', itemnames, itemdescript),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers
the distance, but theres no way across the chasm.""", 'overlook', 'foyer', 'overlook', 'overlook', itemnames, itemdescript),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", 'treasure', 'narrow', 'narrow', 'foyer', itemnames, itemdescript),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", 'treasure', 'narrow', 'treasure', 'treasure', itemnames, itemdescript),
}


# Link rooms together
"""
room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
"""

# print(type(room['foyer']))
# room['foyer'].move()
#
# Main
#
# https://thispointer.com/python-how-to-check-if-an-item-exists-in-list-search-by-value-or-condition/
# https://stackoverflow.com/questions/31924708/in-python-how-would-i-go-about-creating-a-save-system-for-a-text-adventure

parser = argparse.ArgumentParser(description='Move players around')
parser.add_argument('--direction', type=str, )
parser.add_argument('--get', type=str)
parser.add_argument('--drop', type=str)
parser.add_argument('-i', '--inventory', type=str)
arg = parser.parse_args()
dir = arg.direction
playeritems = ["rope", "hat"]
playeritemdes = ["tool", "clothes"]
cPlayer = Player("currPlayer", room["outside"], playeritems, playeritemdes)

print("cp current room item name", cPlayer.current_room.Item.name)


if arg.direction == 'n' and cPlayer.current_room.Item.name:
    print(arg.direction + " " + "PREVIOUS" + str(cPlayer.current_room) + " " + "Desription:" +
          str(cPlayer.current_room.description) + " " + "NEW ROOM: " + str(cPlayer.current_room.n_to))
    cPlayer.current_room = cPlayer.current_room.n_to
    print("in scope player:", cPlayer)
if arg.direction == 's':
    print(arg.direction + " " + "PREVIOUS" + str(cPlayer.current_room) + " " + "Desription:" +
          str(cPlayer.current_room.description) + " " + "NEW ROOM: " + str(cPlayer.current_room.s_to))
    cPlayer.current_room = cPlayer.current_room.s_to
    print("in scope player:", cPlayer)
if arg.direction == 'e':
    print(arg.direction + " " + "PREVIOUS" + str(cPlayer.current_room) + " " + "Desription:" +
          str(cPlayer.current_room.description) + " " + "NEW ROOM: " + str(cPlayer.current_room.s_to))
    cPlayer.current_room = cPlayer.current_room.e_to
    print("in scope player: ", cPlayer)
if arg.direction == 'w':
    print(arg.direction + " " + "PREVIOUS" + str(cPlayer.current_room) + " " + "Desription:" +
          str(cPlayer.current_room.description) + " " + "NEW ROOM: " + str(cPlayer.current_room.w_to))
    cPlayer.current_room = cPlayer.current_room.w_to
    print("nin scope player:", cPlayer)
if arg.direction == 'q':
    print("you've quit the game!", type(cPlayer.current_room.Item.name))
if arg.get and cPlayer.current_room.Item.name.count(arg.get) > 0:
    cPlayer.current_room.Item.name.remove(arg.get)
    cPlayer.Item.name.append(arg.get)
    print("item picked!", cPlayer.Item.name,
          cPlayer.current_room.Item.name)
if arg.get and cPlayer.Item.name.count(arg.get) == 0:
    print("item is not in room")
if arg.drop and cPlayer.Item.name.count(arg.drop) > 0:
    cPlayer.Item.name.remove(arg.drop)
    print("player has dropped item!", "Player carrying:", cPlayer.Item.name)
if arg.inventory:
    print("Player inventory:", cPlayer.Item.name)
else:
    print("please enter a command using `python adv.py --direction` followed by `n, s, w, or e` to choose a direction. Use command --i or --inventory player to get player's current items. Or `q` to quit game")

""""
def move(cPlayer):
    #parser = argparse.ArgumentParser(description='Move players around')
    #parser.add_argument('--direction', type=str, )
    #arg = parser.parse_args()

    if arg.direction == 'n':
        print(arg.direction + " " + "PREVIOUS" + str(cPlayer.current_room) + " " + "Desription:" +
              str(cPlayer.current_room.description) + " " + "NEW ROOM: " + str(cPlayer.current_room.n_to))
        cPlayer.current_room = cPlayer.current_room.n_to
        print("in scope player:", cPlayer)
        return cPlayer 
    if arg.direction == 's':
        print(arg.direction + " " + "PREVIOUS" + str(cPlayer.current_room) + " " + "Desription:" +
              str(cPlayer.current_room.description) + " " + "NEW ROOM: " + str(cPlayer.current_room.s_to))
        cPlayer.current_room = cPlayer.current_room.s_to
        print("in scope player:", cPlayer)
        return cPlayer 
    if arg.direction == 'e':
        print(arg.direction + " " + "PREVIOUS" + str(cPlayer.current_room) + " " + "Desription:" +
              str(cPlayer.current_room.description) + " " + "NEW ROOM: " + str(cPlayer.current_room.s_to))
        cPlayer.current_room = cPlayer.current_room.e_to
        print("in scope player: ", cPlayer)
        return cPlayer 
    if arg.direction == 'w':
        print(arg.direction + " " + "PREVIOUS" + str(cPlayer.current_room) + " " + "Desription:" +
              str(cPlayer.current_room.description) + " " + "NEW ROOM: " + str(cPlayer.current_room.w_to))
        cPlayer.current_room = cPlayer.current_room.w_to
        print("nin scope player:", cPlayer)
        return cPlayer 
    if arg.direction == 'q':
        print("you've quit the game!")
        return cPlayer 
    if arg.get in cPlayer.current_room.Item.name:
        cPlayer.current_room.Item.name.remove(arg.get)
        cPlayer.Item.name.append(arg.get)
        print("item picked!", cPlayer.Item.name,
              cPlayer.current_room.Item.name)
        return cPlayer 
    if arg.get and arg.get not in cPlayer.current_room.Item.name and arg.get not in cPlayer.Item.name:
        print("item is not in room")
        return cPlayer 
    if arg.drop and arg.drop in cPlayer.Item.name:
        cPlayer.Item.name.remove(arg.drop)
        print("player has dropped item!")
        return cPlayer 
    if arg.drop and arg.drop not in cPlayer.current_room.Item.name and arg.drop not in cPlayer.Item.name:
        print("player not carrying item")
        return cPlayer 
    else:
        print("please enter a command using `python adv.py --direction` followed by `n, s, w, or e` to choose a direction. Or `q` to quit game")
"""

# move(cPlayer)
print("OUTSIDE SCOPE:", cPlayer)
#print("name", cPlayer.Item.name)
# move(cPlayer)
# print(cPlayer.current_room.n_to)


# print(currPlayer.current_room)

# print(room["foyer"])


"""
Add a REPL parser to adv.py that accepts directional commands to move the player

After each move, the REPL should print the name and description of the player's current room
Valid commands are n, s, e and w which move the player North, South, East or West
The parser should print an error if the player tries to move where there is no room.
"""
# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# https://gamedev.stackexchange.com/questions/143523/movement-in-a-text-based-game-using-room-class-python
# https://www.futurelearn.com/courses/object-oriented-principles/0/steps/31490
