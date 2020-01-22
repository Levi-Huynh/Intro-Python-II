
class Item:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __repr__(self):
        return f"Items are: {self.name}, Item descriptions are: {self.description}"

    def on_take(self):
        print(f"You've picked up {self.name} ")
    
    def on_drop(self):
        print(f"You've dropped {self.name} ")

#my_item = Item("sword", "weapon")

# print(my_item)
