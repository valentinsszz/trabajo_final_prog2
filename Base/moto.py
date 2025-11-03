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

    def __str__(self):
        return (f"Moto [ID: {self.obtener_numero_id()}] {self.obtener_marca()} {self.obtener_modelo()} ({self.obtener_anio()}) - "
                f"Sucursal: {self.obtener_sucursal_id()}, Estado: {self.obtener_estado_id()}, Cilindrada: {self.obtener_cilindrada()}cc")