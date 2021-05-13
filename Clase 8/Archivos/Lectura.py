#MODO

lorem = open('lorem.txt','r')

print('1')
#print(lorem.read())
print('2')
#print(lorem.read(12))
print('3')

#Leer linea a linea
#linea = lorem.readline()
#print(linea)
#
# linea = lorem.readline()
# while linea !='':
#     print(linea)
#     linea = lorem.readline()
#
# for linea in lorem:
#     print(linea, end='')
#
# texto = lorem.readlines()
# print(texto)

texto = list(lorem)
print(texto)
