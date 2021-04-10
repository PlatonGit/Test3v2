class BaseMenu:
    tabulation = None
    heading = None
    options = None
    next_menus = None


    @staticmethod
    def input_secure_wrap(input_func, *args, **kwargs):
        while True:
            try:
                return input_func(*args, **kwargs)
            except (KeyError, ValueError):
                pass
            except KeyboardInterrupt:
                raise KeyboardInterrupt
            except Exception as ex:
                print('>>> Error:', ex, '<<<')


    def display(self):
        raise NotImplementedError
        
