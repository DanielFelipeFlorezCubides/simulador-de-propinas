import requests
from menu.mainMenu import design as mainDesign
from menu.calculateTipMenu import design as optionDesign1
from menu.divideAmountMenu import design as optionDesign2

### Errors
# Try and except. Try is the first sequence that the program execute and if everythings's good that's nice,
# otherwise if there's an error on x line, except will catch it and will execute another code that will
# inform to the user what's the problem and what to do to not make it happen again.

# try:
#   opcion = int(input('Type a number: '))
#    print('The number is: ', opcion)
#    exit()
# except ValueError as e:
#    print('User, please type a number. The programm cannot accept more than that')

while True:
    option = mainDesign()
    match option:
        case 1:
            optionDesign1()
        case 2:
            optionDesign2()
        case _:
             print('''
            =============================================
                Thanks for using tip simulation!
            =============================================
            ''')
             exit()