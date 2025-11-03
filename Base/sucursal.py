#EJERCICIO 1:
class Sucursal:              
    def __init__(self, numeroId, direccion):
        self.__numeroId = numeroId
        self.__direccion = direccion
        self.__ventas = []  # lista vacía de objetos Venta para guardar las ventas

    # Comandos
    def establecerNumeroId(self, numeroId):
        self.__numeroId = numeroId

    def establecerDireccion(self, direccion):
        self.__direccion = direccion

    def agregarVenta(self, venta):
        self.__ventas.append(venta)   #agrega una venta, a la lista de Ventas

    def removerVenta(self, venta):
        if venta in self.__ventas:     #Elimina una venta de la lista solo si esta presente y evita error si no existe
            self.__ventas.remove(venta)

    #  Consultas
    def obtenerNumeroId(self):
        return self.__numeroId

    def obtenerDireccion(self):
        return self.__direccion

    def obtenerVentas(self):
        return self.__ventas
    #EJERCICIO 5
    def __eq__(self, otro):
        if not isinstance(otro, Sucursal):
            return False
        return self.obtenerNumeroId() == otro.obtenerNumeroId()
    
    def __str__(self):
        texto = f'Sucursal [ID: {self.__numeroId}] - Direccion: {self.__direccion}\n'
        if not self.obtenerVentas():
            texto += " Sin ventas registradas \n"
        else:
            texto += " Ventas \n"
            for i in self.obtenerVentas():
                texto += "    " + str(i) + "\n"
        return texto