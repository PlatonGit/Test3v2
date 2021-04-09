class Recipe:
    def __init__(self, id, recipe_name, number_of_ingredients):
        self.id = id
        self.recipe_name = recipe_name
        self.number_of_ingredients = number_of_ingredients


    @classmethod
    def from_dict(cls, data):
        return Recipe(**data)