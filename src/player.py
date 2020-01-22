# Write a class to hold player information, e.g. what room they are in
# currently.
from room import Room
from item import Item

import argparse
# https://linuxhint.com/python_command_line_parsing_tutorial/


class Player:
    def __init__(self, name, current_room, itemname, itemdes):
        self.name = name
        self.current_room = current_room
        self.Item = Item(itemname, itemdes)

    def move1(self):
        parser = argparse.ArgumentParser(
            description='Input a command to choose direciton (n for north, s for south, e for east, w for west)')
        parser.add_argument('--direction', type=str)
        arg = parser.parse_args()
        if arg.direction == 'n':
            print("You choose north")
        if arg.direction == 's':
            print("you choose south")
        if arg.direction == 'w':
            print("you choose west")

    def __repr__(self):
        return f"Current player name is: {self.name}. & {self.current_room} Player carrying: {self.Item.name}. "


#thing = Player("myroom", "kitchen")
