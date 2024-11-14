from formula.logic import calcular_propina, calcular_total_con_propina, dividir_total
import os
import keyboard

def design():
    opcion = 1
    while opcion:
        print('''
        =============================================
                Divided cost with the party
        =============================================''')
        try:
            keyboard.is_pressed('ctrl+c')
            total = int(input('\tType the total ammount on the receipt: $'))
            if total < 0:
                raise ValueError()
            percentage = int(input('\tType the tip percentage (por ejemplo: 10, 15, 20):  % '))
            if percentage < 0:
                raise ValueError
            people = int(input('\tType the number of the party: '))
            if people < 0:
                raise ValueError
            propina = calcular_propina(total, percentage)
            totalMasPropina = calcular_total_con_propina(total, propina)

            print(f'''
            =============================================
            The tip is: ${propina}
            The total with the tip is: ${totalMasPropina}
            What each one have to pay: ${dividir_total(total, people)}
            =============================================

            ''')

            opcion = int(input('\tDo you wish to calculate it again? (1 - S/0 - N): '))
            os.system('clear')
        except ValueError as e:
            print('''\n Dear user, what you entered was a letter or a negative number. Please correct it''')
        except KeyboardInterrupt:
            print('''\n Dear user, please don't press ctrl + c''')