import vehiculo


class Auto(vehiculo.Vehiculo):

    def __init__(self, numero_id, marca, modelo, anio,
                 sucursal_id, estado_id,
                 airbags, frenos_abs, caballos_fuerza):
        # Llamamos al constructor de la clase padre Vehiculo
        super().__init__(numero_id, marca, modelo, anio, sucursal_id, estado_id)
        
        # Atributos propios de Auto
        self.__airbags = airbags
        self.__frenos_abs = frenos_abs
        self.__caballos_fuerza = caballos_fuerza

    # --- Comandos ---
    def establecerAirbags(self, airbags):
        self.__airbags = airbags

    def establecerFrenosAbs(self, frenos_abs):
        self.__frenos_abs = frenos_abs

    def establecerCaballosFuerza(self, caballos_fuerza):
        self.__caballos_fuerza = caballos_fuerza

    # --- Consultas ---
    def obtenerAirbags(self):
        return self.__airbags

    def obtenerFrenosAbs(self):
        return self.__frenos_abs

    def obtenerCaballosFuerza(self):
        return self.__caballos_fuerza

    def __str__(self):
        return (f"Auto [ID: {self.obtener_numero_id()}] {self.obtener_marca()} {self.obtener_modelo()} ({self.obtener_anio()}) - "
                f"Sucursal: {self.obtener_sucursal_id()}, Estado: {self.obtener_estado_id()}, "
                f"Airbags: {self.obtenerAirbags()}, Frenos ABS: {self.obtenerFrenosAbs()}, Caballos: {self.obtenerCaballosFuerza()}")