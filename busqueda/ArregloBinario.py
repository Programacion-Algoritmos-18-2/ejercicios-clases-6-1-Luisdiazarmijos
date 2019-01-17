class ArregloBinario(object):
    """docstring for ArregloBinario"""
    def __init__(self, datos):
        self.datos = datos
        #agregamos los agregar y obtener de datos
    def agregar_datos(self, datos):
        self.datos = datos
    def obtener_datos(self):
        return self.datos

    #Creamops el metodo busquedad binaria  que recibe un parametro 
    def busquedaBinaria(self, elem):
        elementobusqueda = elem
        inferior = 0 # extremo inferior del area de busqueda
        superior = len(self.datos) -1 # extremo superior del area de busqueda
        medio = int((inferior + superior + 1) / 2) #elemento medio
        ubicacion = -1 #devuelve el valor; -1 si no lo encontra
        #Agregamos un while con la siguiente condicion
        while ((inferior <= superior) and (ubicacion == -1)):
            #condicional if  si el elemento se encuentra en medio
            if (elementobusqueda == self.datos[medio]):
                ubicacion = medio #la ubicacion es el elemento medio actual
                #el elemento medio es demasiado alto
            elif(elementobusqueda < self.datos[medio]):
                superior = medio - 1 # elimina la mitad superio
            else:
                inferior = medio + 1 #elimina la mitad inferior
            medio = int((inferior + superior + 1) / 2) #recalcula el elemento medio
            # retornamos ubicacion
        return ubicacion


