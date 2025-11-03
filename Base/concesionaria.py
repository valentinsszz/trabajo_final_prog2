class Concesionaria:

    def __init__(self, numero_id, nombre):
        self.__numero_id = numero_id
        self.__nombre = nombre
        self.__clientes = []
        self.__sucursales = []
        self.__vehiculos = []

    def establecer_numero_id(self, numero_id):
        self.__numero_id = numero_id

    def establecer_nombre(self, nombre):
        self.__nombre = nombre

    def agregar_cliente(self, cliente):
        self.__clientes.append(cliente)

    def remover_cliente(self, cliente):
        self.__clientes.remove(cliente)

    def agregar_sucursal(self, sucursal):
        self.__sucursales.append(sucursal)

    def remover_sucursal(self, sucursal):
        self.__sucursales.remove(sucursal)

    def agregar_vehiculo(self, vehiculo):
        self.__vehiculos.append(vehiculo)

    def remover_vehiculo(self, vehiculo):
        self.__vehiculos.remove(vehiculo)

    def obtener_numero_id(self):
        return self.__numero_id

    def obtener_nombre(self):
        return self.__nombre

    def obtener_clientes(self):
        return self.__clientes

    def obtener_sucursales(self):
        return self.__sucursales

    def obtener_vehiculos(self):
        return self.__vehiculos
    #EJERCICIO 5:
    def __eq__(self, otro):
        if not isinstance(otro, Concesionaria):
            return False
        return self.obtener_numero_id() == otro.obtener_numero_id()
    

    def __str__(self):
        texto = f"Concesionaria [ID: {self.__numero_id}, Nombre: {self.__nombre}]\n"
        texto += "\nClientes:\n"

        if not self.obtener_clientes():
            texto += "No se encontraron clientes.\n"
        else: 
            for c in self.obtener_clientes():
                texto += "    " + str(c) + "\n"
        
        if not self.obtener_sucursales():
            texto += "No se encontraron sucursales.\n"
        else: 
            for s in self.obtener_sucursales():
                texto += "    " + str(s) + "\n"

        if not self.obtener_vehiculos():
            texto += "No se encontraron vehículos.\n"
        else: 
            for v in self.obtener_vehiculos():
                texto += "    " + str(v) + "\n"
        
        return texto
        