from models import Recipe, Ingredient


class RecipeController:
    def __init__(self, db_connection):
        self.__db_connnection = db_connection


    def create_recipe(self):      
        print('Creating the recipe:')
        
        query = "SELECT * FROM Ingredients"
        self.__db_connnection.execute(query)
        ingredients_exist = self.__db_connnection.cursor.rowcount
        
        recipe_name = input('\tEnter recipe\'s name: ')
        while True:          
            ingredients_num = int(input('\tHow many ingredients are required: '))
            if ingredients_num > ingredients_exist:
                raise ValueError(f'>>> User\'s input states that {ingredients_num} ingredients are required, but only {ingredients_exist} exist <<<')
            else:
                break

        query = f"INSERT INTO Recipe (recipe_name, number_of_ingredients) VALUES ('{recipe_name}', {ingredients_num})"
        self.__db_connnection.execute(query)
            

    def add_ingredient_list(self, recipe_id):
        print('Adding an ingredient list:')

        query = "SELECT * FROM Ingredients"
        self.__db_connnection.execute(query)
        num_ingredients = self.__db_connnection.cursor.rowcount
        ingredients_left = []

        if num_ingredients > 0:
            for i in range(num_ingredients):
                cur_ingredient = Ingredient.from_dict(self.__db_connnection.cursor.fetchone())               
                print(f'\t[{cur_ingredient.id}] - {cur_ingredient.name}')
        else:
            print('\t>>> There are no ingredients <<<')
            return            

        while ingredients_left != []:
            ingredient_id = int(input('\tEnter ingredient\'s id to add it to the list: '))


    def delete_recipe(self):
        print('Deleting the recipe:')
        
        query = "SELECT * FROM Recipe"
        self.__db_connnection.execute(query)
        num_recipes = self.__db_connnection.cursor.rowcount

        if num_recipes > 0:
            for i in range(num_recipes):
                cur_recipe = Recipe.from_dict(self.__db_connnection.cursor.fetchone())
                print(f'\t[{cur_recipe.id}] - {cur_recipe.recipe_name}, ingredients - {cur_recipe.number_of_ingredients}')
        else:
            print('\t>>> There are no recipes <<<')
            return
        
        recipe_id = int(input('\tEnter id of the recipy you want to delete: '))
        
        query = f"DELETE FROM IngredientList WHERE recipe_id = {recipe_id}"
        self.__db_connnection.execute(query)
        
        query = f"DELETE FROM Recipe WHERE id = {recipe_id}"
        self.__db_connnection.execute(query)
