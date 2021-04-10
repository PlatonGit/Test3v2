from models import Ingredient
from db import ConnectionConfig


class IngredientsController:
    def __init__(self, db_connection):
        self.db_connection = db_connection


    def select_all_ingredients(self):
        query = "SELECT * FROM Ingredients"
        self.db_connection.execute(query)
        rows = self.db_connection.cursor.rowcount >= 1
        ingredient_list = []

        if self.db_connection.cursor.rowcount >= 1:
            for i in range(rows):
                cur_ingredient = Ingredient.from_dict(self.db_connection.cursor.fetchone())
                ingredient_list.append(cur_ingredient)
            return ingredient_list




