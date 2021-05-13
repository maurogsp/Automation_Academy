
f = open('mi_archivo.txt','w')

# f.write('Hola mundo')
#
# f.close()


milista = ['estoy \n', 'escribiendo \n', 'un archivo \n']

f.writelines(milista)

f.close()
