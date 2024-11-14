import keyboard
def design():
    while True:
        try:
            keyboard.is_pressed('ctrl+c')
            print(f'''
            =============================================
                            Tip simulation
            =============================================
            1. Calculate the tip and the total ammount
            2. Calculate the total ammount divided with your party
            3. Exit
            =============================================
            ''')
            options = int(input('Please choose an option (1-3): '))
            if (options >= 1 and options <= 3):
                return options
            else:
                raise ValueError()
            
        except ValueError as e:
            print('Please choose a valid option')
        except KeyboardInterrupt:
            print('Please choose a valid option')