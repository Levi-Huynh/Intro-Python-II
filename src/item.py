
class Item:

    def __init__(self, *name):
        self.name = name

    def __repr__(self):
        return f"{self.name}"

    def on_take(self):
        print(f"You've picked up {self.name} ")

    def on_drop(self):
        print(f"You've dropped {self.name} ")
