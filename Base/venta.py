#EJERCICIO 4:
class Venta:
    # Constructor
       def __init__(self, numeroId, fecha, clienteId, vehiculoId, monto):
        self.__numeroId = numeroId
        self.__fecha = fecha
        self.__clienteId = clienteId
        self.__vehiculoId = vehiculoId
        self.__monto = monto

    # ---------- COMANDOS ----------
       def establecerNumeroId(self, numeroId):
        self.__numeroId = numeroId

       def establecerFecha(self, fecha):
        self.__fecha = fecha

       def establecerClienteId(self, clienteId):
        self.__clienteId = clienteId

       def establecerVehiculoId(self, vehiculoId):
        self.__vehiculoId = vehiculoId

       def establecerMonto(self, monto):
        self.__monto = monto

    # ---------- CONSULTAS  ------
       def obtenerNumeroId(self):
        return self.__numeroId

       def obtenerFecha(self):
        return self.__fecha

       def obtenerClienteId(self):
        return self.__clienteId

       def obtenerVehiculoId(self):
        return self.__vehiculoId

       def obtenerMonto(self):
        return self.__monto
      #EJERCICIO 5: 
       def __eq__(self, otro):
         if not isinstance(otro, Venta):
           return False
         return self.obtenerNumeroId() == otro.obtenerNumeroId()

       def __str__(self):
           return f"Venta {self.__numeroId} - Fecha: {self.__fecha} - Cliente ID: {self.__clienteId} - Vehículo ID: {self.__vehiculoId} - Monto: ${self.__monto}"