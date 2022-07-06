import pandas as pd
class Arch:
    def __init__(self):
        ar=open("Clientes.txt","r")
        contenido=ar.read()
        print('lectura del archivo')
        print(contenido)
        ar.close()
Arch=Arch()
'''
lectura de un archivo de texto
'''

read_file = pd.read_csv (r'Clientes.txt')
read_file.to_csv (r'Clientes.csv', index=None)
print('Creacion del archivo csv exitoso ')
'''
conversion de un archivo de texto a un
archivo tipo csv
'''





