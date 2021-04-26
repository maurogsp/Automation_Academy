
# nombre = 'pepe'
# oportunidades = 5
# adivino = input('Tiene'+ str(oportunidades) + 'oportunidades. Ingrese un nombre: ')
# while  adivino != nombre:
#     oportunidades-= 1

# nombre = input('Nombre: ')
# adivinar = ''
# oportunidades = 6
# while nombre != adivinar:
#     oportunidades -= 1
#     print('Oportunidades: '+str(oportunidades))
#     adivinar = input('Adivine el nombre: ')
#     if oportunidades == 0:
#         print('Perdiste')
#         break
# else:
#     print('Adivinó!')
#


nombre = input('Ingrese el nombre a adivinar: ')
oportunidades = 6
resultado = 0
while (oportunidades >0 and resultado !=1):
    print('Tiene ' + str(oportunidades) + ' oportunidades')
    adivinar = input('Adivine el nombre: ')
    if adivinar == nombre:
        resultado = 1
    oportunidades -= 1
if resultado == 1:
    print('Usted adivino')
else:
    print('Usted perdio')
