import requests
import tabulate
import keyboard
from menu.mainMenu import design as mainDesign
from menu.calculateTipMenu import design as designOption1
from menu.divideAmountMenu import design as designOption2
from menu.tipMenuOptions import design as designTipOption
from menu.updateTipMenu import design as updateDesign
from server.findAllTip import firstTipOption
from server.findByIdTip import thirdTipOption
from server.deleteByIdTip import fourthTipOption
from server.updateByIdTip import getId

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
    match mainDesign():
        case 1: 
            while True:
              option = designTipOption()
              if(option == 1): designOption1()
              elif(option == 2): print(tabulate(firstTipOption(), headers="keys"))
              elif(option == 3): 
                try:
                  keyboard.is_pressed('ctrl+c')
                  id = int(input("Ingrese el id de la propina que desea consultar: "))
                  if(id < 0):
                      raise ValueError()
                  print(tabulate([thirdTipOption(id)], headers="keys"))
                except ValueError as e:
                    print("\tUsuario los datos solicitados no son válidos, ingrese datos de tipo entero")
                except KeyboardInterrupt:
                    print("`\n\tSeñor usuario no presionó Ctrl+C, termine la ejecución del programa y selecione una de las opciones disponibles")
              elif(option == 4): 
                try:
                  keyboard.is_pressed('ctrl+c')
                  id = int(input("Ingrese el id de la propina que desea consultar: "))
                  if(id < 0):
                      raise ValueError()
                  fourthTipOption(id)
                  print("Propina eliminada con éxito")
                except ValueError as e:
                    print("\tUsuario los datos solicitados no son válidos, ingrese datos de tipo entero")
                except KeyboardInterrupt:
                    print("`\n\tSeñor usuario no presionó Ctrl+C, termine la ejecución del programa y selecione una de las opciones disponibles")
              elif(option == 5):
                try:
                    keyboard.is_pressed('ctrl+c')
                    id = int(input('Please type the id of the tip to search it: '))
                    if (id <= 0):
                        raise ValueError()
                except ValueError as e:
                    print('Dear user, what you entered was a letter or a negative number. Please correct it')
                except KeyboardInterrupt:
                    print('''\n Dear user, please don't press ctrl + c''')

                    print(tabulate([getId(id)], headers="keys"))

                try:
                    decission = input('Is this the tip you want to edit? (y/n): ').lower
                    keyboard.is_pressed('ctrl+c')
                    if decission == 'y': updateDesign()
                    elif decission == 'n': break
                except KeyboardInterrupt:
                    print('''\n Dear user, please don't press ctrl + c''')
              elif(option == 6): break
        case 2: designOption2()
        case 3:
            print("""
            =============================================
              ¡Gracias por usar el Simulador de Propina!
            =============================================
            """)
            exit()
         