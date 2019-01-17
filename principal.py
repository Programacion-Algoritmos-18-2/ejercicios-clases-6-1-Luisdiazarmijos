#Importamos los paquetes paquete_archivos  de la clase Miarchivo
from paquete_archivos.Miarchivos import MiArchivo
from busqueda.ArregloBinario import *# Importamos el paquete busqueda de la clase ArregloBinario
#Creamos un objeto MiArchivo
m = MiArchivo()
#Obtenemos informacion y del archivo y almacenarla en lista
lista = m.obtener_informacion()
#Creamos un split para separar con comas(,)
lista = [l.split(",") for l in lista]
#Creamos una lista vacia
lista2 = []
#Recorremos  la lista
for l in lista:
	
	for m in l:
		#transformar en enteros
		lista2.append(int(m))
# Ordenar la lista con sort
lista2.sort()
#Imprimimos la lista ordenada
print(lista2)
#Creamos un objeto de ArregloBinario
operacion = ArregloBinario(lista2)
#Llamas e imprimimos en pantalla
num=int(input("Ingrese elemento a buscar\n"))
#Imprimimos en pantalla
print("El elemento esta en la posicion")
print(operacion.busquedaBinaria(num))

