from menus import BaseMenu
from menus.recipe_menu import RecipeMenu


class MainMenu(BaseMenu):
    @staticmethod
    def raise_exception():
        raise KeyboardInterrupt
    
    heading = '\nMain menu:'
    options = f'[1] Recipes\n[2] Ingredients\n[3] Exit'
    next_menus = {
        1 : RecipeMenu,
        2 : None,
        3 : lambda *_: MainMenu.raise_exception()
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
            next_menu.display()
            