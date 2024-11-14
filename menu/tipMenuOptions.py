import keyboard
def design():
    while True:
        try:
            keyboard.is_pressed('ctrl+c')
            print(f'''
            =============================================
                                Options
            =============================================
            1. Calculate tip
            2. Show all the tips storaged
            3. Search a tip
            4. Delete a tip
            5. Edit a tip
            6. Exit
            =============================================
            ''')
            options = int(input('Please choose an option (1-6): '))
            if (options >= 1 and options <= 6):
                return options
            else:
                raise ValueError()
            
        except ValueError as e:
            print('Please choose a valid option')
        except KeyboardInterrupt:
            print('Please choose a valid option')