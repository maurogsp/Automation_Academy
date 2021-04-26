# 1. Crear un nuevo repositorio
# 2. Tomar de base el programa de la clase pasada
# 3. Vamos a modificar el programa para que solo tome como válidos números entre 1 y 120
#  (si pone un número entre -inf y 0 o 121 a inf debe volver a preguntar)
# 3. Al inicio del programa preguntar cuantas personas registrar
# 4. Hacer que el programa que se hizo se ejecute esas n veces que se pusieron en el punto 3
# 5. Subir el programa al repositorio creado.

personas = int(input('Ingrese la cantidad de personas que desea registrar: '))
for i in range (personas):
    nombre = input('Ingrese su nombre: ')
    apellido = input('Ingrese su apellido: ')
    edad = int(input('Ingrese su edad: '))
    while edad < 1  or edad >120:
        edad = int(input('Su edad debe ser mayor a 0 y menor o igual a 120. Ingrese su edad nuevamente: '))
    if edad < 18:
        condicion = 'menor'
    elif edad < 65:
        condicion = 'mayor'
    elif edad < 120:
        condicion = 'jubilado'
    else:
        condicion = 'cadaver'
    #print('Su nombre es: '+ nombre+ " " +apellido + ' y usted es '+condicion)
    print('Su nombre es:',nombre, apellido,'y usted es',condicion)
