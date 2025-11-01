import vehiculo


class Moto(vehiculo.Vehiculo):

    def __init__(
        self, numero_id, marca, modelo, anio, sucursal_id, estado_id, cilindrada
    ):
        super().__init__(numero_id, marca, modelo, anio, sucursal_id, estado_id)
        self.__cilindrada = cilindrada

    def establecer_cilindrada(self, cilindrada):
        self.__cilindrada = cilindrada

    def obtener_cilindrada(self):
        return self.__cilindrada
