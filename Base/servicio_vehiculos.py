import servicio_concesionarias
#EJERCICIO 7:
class ServicioVehiculos:

    def obtener_vehiculos_por_sucursal_y_estado(self, concesionaria_id, sucursal_id, estado_id):
        
        servicio_concesionarias_instancia = servicio_concesionarias.ServicioConcesionarias()
        concesionaria = servicio_concesionarias_instancia.obtener_por_id(concesionaria_id)

        if concesionaria is None:
            return []

        vehiculos_filtrados = []
        for vehiculo in concesionaria.obtener_vehiculos():
            if (
                vehiculo.obtener_sucursal_id() == int(sucursal_id)
                and vehiculo.obtener_estado_id() == int(estado_id)
            ):
                vehiculos_filtrados.append(vehiculo)

        return vehiculos_filtrados
