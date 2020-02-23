

class Category:
    def __init__(self, name, description, location):
        self.name = name
        self.description = description
        self.location = location
    def __str__(self):
        output = f'{self.name}: {self.description} \n'
        output += f'Find me on: {self.location}'
        return output

thing = Category("cool", "clothing", "home")
print(str(thing))