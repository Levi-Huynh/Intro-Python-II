# Implement a class to hold room information. This should have name and
# description attributes.
# https://stackoverflow.com/questions/2328094/python-oop-class-relationships
# https://stackoverflow.com/questions/39453493/when-to-use-association-aggregation-composition-and-inheritance
# kwargs: https://stackoverflow.com/questions/8187082/how-can-you-set-class-attributes-from-variable-arguments-kwargs-in-python
# https://stackoverflow.com/questions/39390157/cant-pass-a-list-as-class-attribute

import argparse
from item import Item


class Room:
    #n_to = None
    #s_to = None
    #e_to = None
    #w_to = None

    def __init__(self, name, description, *itemnames, north=None, south=None, east=None, west=None):
        self.name = name
        self.description = description
        self.Item = Item(itemnames)
        self.n_to = north
        self.s_to = south
        self.e_to = east
        self.w_to = west

    def roomDirection(self, direction):
        if direction == "n":
            return self.n_to  # execute the room links in adv2.py if it exists
        if direction == "s":
            return self.s_to
        if direction == "w":
            return self.w_to
        else:
            return self.e_to

    def addItem(self, *item):
        self.Item = item

    def __str__(self):
        return f" {self.name} Items this room has are: {self.Item}  "


#itemnames = ["sheild", "hammer"]
#itemdescript = ["weapon", "tool"]
# myroom = Room("Outside Cave Entrance", "North of you, the cave mount beckons",
# 'foyer', 'outside', 'outside', 'outside', itemnames, itemdescript)
# print(myroom)
# print(myroom.Item.name)
"""
, n_to, s_to, e_to, w_to, exits
        self.n_to = n_to
        self.s_to = s_to
        self.e_to = e_to
        self.w_to = w_to
        self.exits = exits
"""

"""
    def move(self):        
        parser = argparse.ArgumentParser()
        parser.add_argument('--direct', type=str)
        arg = parser.parse_args()
        if arg.direct == 'n':
            print("You choose North. You are now in:" room[self.name]self.n_to )
"""
