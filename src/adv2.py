from room import Room
from player import Player
from item import Item
import argparse
import re

# Declare all the rooms
# https://www.futurelearn.com/courses/object-oriented-principles/0/steps/31490
# ADDING ITEM VERSUS LIST OF ITEMS TO LIST https://www.geeksforgeeks.org/append-extend-python/
itemnames = ["sheild", "hammer"]
itemdescript = ["weapon", "tool"]

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", itemnames),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""",  itemnames),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""",  itemnames),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""",  itemnames),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""",  itemnames),
}

playeritems = ["rope", "hat"]
playeritemdes = ["tool", "clothes"]

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# set player attributes here
player = Player(input("Enter your player name: "),
                room['outside'], playeritems)

# print(player.current_room.Item.name[0][0])

"""
get = input(
    "choose an item by typing [take] [itemname] or choose [q]: ")
# \s stands for white chars and + for reps of \s char
ans = get.split()

print(ans)
"""

"""
def check():
    get = input(
        "choose an item by typing [take] [itemname] or choose [q]: ")
    # if get in player.current_room.Item.name[0][0] and "take" in get:
    ran = get.split()
    if "take" in ran:
        print("yep")
    if get == "q":
        print("no items chosen from room")
    elif ran[1] in player.current_room.Item.name[0][0]:
        player.getitem(player, ran[1], ran[2])
        thing1 = [i for i in player.Item.name[0]]
        thing1.remove(ran[1])
        thing2 = []
        thing2.append(thing1[1])
        # print("here", thing2)
"""


def check():
    # rlist = [i for sub in player.current_room.Item[1] for i in sub]
    rlist = ["hammer", "gloves"]
    rlist.append(player.current_room.Item)
    thing4 = player.current_room.addItem(player, rlist)
    # print("rlist", rlist)
    print("room items: ", thing4)
    # print("thing4", thing4)


def getDirection():  # decouple function to take care of getting direction input
    direction = input("which direction? [n/s/w/e]: ")
    if direction == "n" or direction == "s" or direction == "w" or direction == "e":
        return direction
    else:
        print("Invalid direction")
        return getDirection()  # regression


def moveRoom(player, direction):
    # direction passed here is result of getDirection() function input
    newRoom = player.current_room.roomDirection(direction)
    if newRoom:
        player.move1(newRoom)
    else:
        print("Oops can't go in that direction, retry!")
        newDirection = getDirection()
        moveRoom(player, newDirection)  # regression


def takeItem(player, room):
    get = input(
        "choose an item by typing [take] [itemname] or choose [no] [item]: ")
    spltInput = get.split()
    if "no" in spltInput:
        print("no items chosen from room")
    elif spltInput[1] in player.current_room.Item.name[0][0] and "take" in spltInput:
        spltInput.pop(0)
        # print("here", player.Item.name)
        mlist = [i for i in player.Item.name[0]]
        mlist.append(spltInput)
        player.getitem(player, mlist)
        print("You have picked up: ", spltInput)


def dropItem(player, room):
    get = input(
        "Drop an item by typing [drop] [itemname] or choose [dont] [drop]: ")
    spltInput = get.split()
    ilist = [i for i in player.Item.name[0]]
    rlist = []
    rlist.append(player.current_room.Item.name)
    #print("YO", player.Item.name[0])
    if "dont" in spltInput:
        print("no items dropped")
        return
    if len(spltInput) > 1:
        if any(spltInput[1] in x for x in ilist[1]) and "drop" in spltInput:
            print('you have dropped', spltInput[1])
            flat = [i for sub in ilist[1] for i in sub]
            flat.remove(spltInput[1])
            mytup = []
            for i in rlist[0][0][0]:
                mytup.append(i)
            #print("MYTUP", mytup)
            mytup.append(spltInput[1])
            #print("MYTUP2", mytup)
            #flat1 = [i for sub in r2list for i in sub]
            #print("YO HERE FLAT", flat1)
            # print("item dropped,now carrying: ", ilist[1])
            #player.removeitem(player, flat)

            remove = player.removeitem(player, flat)
            newItem = Item(mytup)
            player.current_room.addItem(player, newItem)
            #print("ROOM ITEMS: ", player.current_room.Item)
            return remove
    else:
        print("try again")
        dropItem(player, room)


def inventory(player):
    inv = input(
        "To check items carried by player type [i] or [inventory] else type [continue]: ")
    spltInv = inv.split()
    if "i" in spltInv or "inventory" in spltInv:
        print("player currently carrying: ", player.Item.name[0][1])
        return
    if "continue" in spltInv:
        print("game continue")
    else:
        print("invalid command")
        inventory(player)


def loopGame():
    global player
    print(
        f'\n{player.name} entered the {player.current_room}.')
    direction = getDirection()
    moveRoom(player, direction)
    takeItem(player, room)
    dropItem(player, room)
    inventory(player)
    # check()


def main():
    while True:
        loopGame()


main()
"""
check()
"""
