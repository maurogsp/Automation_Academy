#1-Tomar de base el ejercicio de la clase 2
#2-Si es menor de edad, vamos a venderle juguetes
# 2.1-Preguntar si es electronico, color, si camina o no
#3-Si es mayor de edad, vamos a venderle ropa
# 3.1-Preguntar si es camisa o pantalon, color y talle
#4-Si es jubilado vamos a venderle pasajes
# 4.1-Preguntar si quiere viajar a Federacion, Cataratas o Santa Teresita
#5-Mostrar por pantalla los datos de la persona y el producto seleccionado
#Tip: crear funciones y llamarlas dentro de mi programa


def calculaRangoEtario(edad):
    if edad < 18:
        condicion = 'menor'
    elif edad < 65:
        condicion = 'mayor'
    elif edad < 120:
        condicion = 'jubilado'
    return condicion

def ventaMenor(nombre,apellido,rango):
    electronico = 0
    while electronico == 0:
        print('¿Desea un juguete electronico? Indique el número segun corresponda:  \n 1- Si \n 2- No ')
        electronico = int(input('Indique aqui su opcion: '))
        if electronico == 1:
            electronico = 'Si'
        elif electronico == 2:
            electronico = 'No'
        else:
            electronico = 0
            print('Opcion incorrecta. Ingrese su opción nuevamente')
    color = input('Indique el color que desea: ')
    camina = 0
    while camina == 0:
        print('¿Desea que el juguete camine? Indique el número segun corresponda: \n 1- Si \n 2- No ')
        camina = int(input('Indique aqui su opcion: '))
        if camina == 1:
            camina = 'Si'
        elif camina == 2:
            camina = 'No'
        else:
            camina = 0
            print('Opcion incorrecta. Ingrese su opción nuevamente')
    print('Su nombre es:',nombre, apellido,'\nUsted es',rango,'\nJueguete Electronico: ',electronico,' Color: ',color, 'Camina: ',camina)

def ventaMayor(nombre,apellido,rango):
    prenda = 0
    while prenda == 0:
        print('¿Desea una camisa o un pantalon? Indique el número segun corresponda: \n 1- Camisa \n 2- Pantalon')
        prenda = int(input('Indique aqui su opcion: '))
        if prenda == 1:
            prenda = 'Camisa'
        elif prenda == 2:
            prenda = 'Pantalon'
        else:
            prenda = 0
            print('Opcion incorrecta. Ingrese su opción nuevamente')
    color = input('Indique el color que desea: ')
    talle = 0
    while talle ==0:
        print('Indique el talle que desea: Indique el número segun corresponda: \n 1- S \n 2- M \n 3- L \n 4- XL')
        talle = int(input('Indique aqui su opcion: '))
        if talle == 1:
            talle = 'S'
        elif talle == 2:
            talle = 'M'
        elif talle == 3:
            talle ='L'
        elif talle == 4:
            talle = 'XL'
        else:
            talle = 0
            print('Opcion incorrecta. Ingrese su opción nuevamente')
    print('Su nombre es:',nombre, apellido,'\nUsted es',rango,'\nPrenda: ',prenda,' Color: ',color, 'Talle: ',talle)

def ventaJubilado(nombre,apellido,rango):
    viaje = 0
    while viaje == 0:
        print('Indique el destino al que desea viajar: Indique el número segun corresponda: \n 1- Federacion \n 2- Cataratas \n 3- Santa Teresita')
        viaje = int(input('Indique aqui su opcion: '))
        if viaje == 1:
            viaje = 'Federacion'
        elif viaje == 2:
            viaje = 'Cataratas'
        elif viaje == 3:
            viaje ='Santa Teresita'
        else:
            viaje = 0
            print('Opcion incorrecta. Ingrese su opción nuevamente')
    print('Su nombre es:',nombre, apellido,'\nUsted es',rango,'\nDestino: ',viaje)

def ventaSegunRango(nombre,apellido,rango):
    if rango == 'menor':
        ventaMenor(nombre,apellido,rango)
    elif rango == 'mayor':
        ventaMayor(nombre,apellido,rango)
    else:
        ventaJubilado(nombre,apellido,rango)


personas = int(input('Ingrese la cantidad de personas que desea registrar: '))
for i in range (personas):
        nombre = input('Ingrese su nombre: ')
        apellido = input('Ingrese su apellido: ')
        edad = int(input('Ingrese su edad: '))
        while edad < 1  or edad >=120:
            edad = int(input('Su edad debe ser mayor a 0 y menor o igual a 120. Ingrese su edad nuevamente: '))
        rango = calculaRangoEtario(edad)
        ventaSegunRango(nombre, apellido, rango)


    #print('Su nombre es: '+ nombre+ " " +apellido + ' y usted es '+condicion)
