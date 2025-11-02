class Sucursal:
    def __init__(self, numeroId, direccion):
        self.numeroId = numeroId
        self.direccion = direccion
        self.venta = []

    #comandos
    def establecerNumeroId(self, numeroId):
        self.numeroId = numeroId
    
    def establecerDireccion(self, direccion):
        self.direccion = direccion

    def agregarVenta(self, venta):
        self.venta.append(venta)

    def removerVenta(self, venta):
        self.venta.remove(venta)
    
    #Consultas
    def obtenerNumeroId(self):
        return self.numeroId
    
    def obtenerDireccion(self):
        return self.direccion
    
    def obtenerVentas(self):
        return self.venta
        

    
