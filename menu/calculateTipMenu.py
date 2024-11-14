from formula.logic import calcular_propina, calcular_total_con_propina
import os
import keyboard
import requests

def design():
    opcion = 1
    while opcion:
        print('''
        =============================================
                    Tip calculation
        =============================================
        ''')
        try:
            keyboard.is_pressed('ctrl+c')
            total = float(input('Type the total ammount on the receipt: $'))
            if total < 0:
                raise ValueError()
            percentage = int(input('Type the tip percentage (por ejemplo: 10, 15, 20):  % '))
            propina = calcular_propina(total, percentage)
            totalPagar = calcular_total_con_propina(total, propina)
            print(f'''
            =============================================
            The tip is: $ {propina}
            The total with the tip is: $ {totalPagar}
            =============================================
            ''')
            
            headers = {'Content-Type': 'application/json'}
            data = {'monto': total, 'propina': propina, 'montoTotalPagar': totalPagar, 'porcetaje': percentage}
            response = requests.post('https://6734e17b5995834c8a913808.mockapi.io/propina', headers=headers, json=data)
            print(response)

            opcion = int(input('Do you wish to calculate it again? (1 - S/0 - N): '))
            os.system('clear')
        except ValueError as e:
            print('Dear user, what you entered was a letter or a negative number. Please correct it')
        except KeyboardInterrupt:
            print('''\n Dear user, please don't press ctrl + c''')