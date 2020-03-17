
class Item:

    def __init__(self, name):
        self.Iname = name

    def on_take(self):
        print(f"You've picked up {self.Iname} ")

    def on_drop(self):
        print(f"You've dropped {self.Iname} ")

    def __str__(self):
        return f"{self.Iname}"
