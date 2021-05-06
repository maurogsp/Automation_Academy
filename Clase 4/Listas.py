colores = ['azul','verde','rojo']
#print(colores)
#print(colores[1])
print('Solucion 1')
for i in range (0, len(colores)):
    print(colores[i])

print('Solucion 2')
for color in colores:
    print(color)

colores.append('amarillo')
print(colores)
colores.insert(2,'violeta')
print(colores)
colores.pop()
print(colores)
colores.pop(2)
print(colores)
colores.reverse()
print(colores)
colores.sort()
print(colores)
colores_dos = ['naranja','violeta','marron']
colores.extend(colores_dos)
print(colores)

colores_tres = colores #esto asigna la lista colores a la lista colores_tres, las dos variables apuntan al mismo lugar de memoria, es decir, son la misma lista
colores_tres[1] = 'Negro'
print(colores_tres[1])
print(colores[1])
print(colores)
colores_cuatro = colores.copy()
colores_cuatro[1] = 'Blanco'
print('Lista colores_cuatro: ',colores_cuatro)
print('Lista colores: ',colores)

colores.clear()
print(colores)
