from menus import MainMenu


def main():
    main_menu = MainMenu()
    main_menu.display()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Goodbye!\n')

