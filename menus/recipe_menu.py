from menus import BaseMenu
from db import ConnectionConfig
from db import IngredientsController


class RecipeMenu(BaseMenu):  
    tabulation = '\t'
    heading = '\nRecipes:'
    options = f'{tabulation}[1] Add a recipy\n{tabulation}[2] Delete a recipe\n{tabulation}[3] Back'
    next_menus = {
        1 : RecipeAddMenu,
        2 : None,
        3 : lambda *_: None
    }


    def display(self):
        def get_input():
            print(self.heading)
            print(self.options)
            
            input_num = int(input('\nEnter action\'s number: '))
            if input_num not in self.next_menus.keys():
                raise KeyError('\n>>> Wrong action number <<<')
            return input_num

        while True:
            selected_option = self.input_secure_wrap(get_input)
            
            next_menu = self.next_menus[selected_option]()
            if next_menu is not None:
                next_menu.display()
            else:
                return


class RecipeAddMenu(RecipeMenu):
    tabulation = '\t\t'
    heading = '\n\tAdding recipy:'


    def display(self):
        def confirmation():
            user_input = input('Continue? (y/n): ')
            
            if user_input == 'y':
                return True
            elif user_input == 'n':
                return False
            else:
                raise ValueError('\n>>> You can only enter \'y\' for yes and \'n\' for no <<<')
        
        recipy_name = self.input_secure_wrap(input('Enter recipy\'s name: '))
        ingredient_num = self.input_secure_wrap(int(input('Enter number of ingredients required: ')))
        
        if self.input_secure_wrap(confirmation):
            recipy_ingredient_select_menu = RecipyIngredientSelectMenu()
            recipy_ingredient_select_menu.display()
        else:
            return

    
class RecipyIngredientSelectMenu(RecipeAddMenu):
    tabulation = '\t\t\t'
    heading = '\n\t\tAdding required ingredients to a recipe:'
    db_connection = ConnectionConfig()
    ingredients_controller = IngredientsController(db_connection)


    def display(self):
        ingredient_list = self.ingredients_controller.select_all_ingredients()
        chosen_ingr = []

        def show_ingredients():
            print(self.heading)
            for i, ing in enumerate(ingredient_list):
                print(f'[{i}] {ing.name}')
        
        show_ingredients()
            # selected_id = int(input('Enter the number of an ingredient you want to add: '))
            # if selected_id not in range(len(ingredient_list)) and selected_id != len(ingredients_list) and selected_id != len(ingredient_list) + 1:
            #     raise ValueError('>>> Wrong ingredient number <<<')
            