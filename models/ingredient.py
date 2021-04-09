class Ingredient:
    def __init__(self, id, name):
        self.id = id
        self.name = name


    @classmethod
    def from_dict(cls, data):
        return Ingredient(**data)