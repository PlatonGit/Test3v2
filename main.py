from conf import ConnectionConfig
from controllers import RecipeController





def main():
    db_connection = ConnectionConfig()
    recipe_controller = RecipeController(db_connection)

    recipe_controller.delete_recipe()


if __name__ == '__main__':
    main()

