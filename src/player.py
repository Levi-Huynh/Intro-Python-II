# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
from item import Item

import argparse
# https://linuxhint.com/python_command_line_parsing_tutorial/


class IterRegistry(type):
    def __iter__(cls):
        return iter(cls._registry)


class Player:
    __metaclass__ = IterRegistry
    _registry = []

    def __init__(self, name, current_room, *itemname):
        self._registry.append(self)
        self.name = name
        self.current_room = current_room
        self.Item = Item(itemname)

    def move1(self, room):
        self.current_room = room

    def getitem(self, *item):
        self.Item = Item(item)

    # update the self item list in adv2 then pass in the list below
    def removeitem(self, *item):
        self.Item = Item(item)

    def __repr__(self):
        return f"Current player name is: {self.name}. & {self.current_room} Player carrying: {self.Item.name}. "


thing = Player("jack", "kitchen", ("spoon", "pencil"))
thing.getitem("thing", "thing1")
thing2 = thing.Item
print(thing2)
