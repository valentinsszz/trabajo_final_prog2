import servicio_concesionarias
#EJERCICIO 6:
class ServicioClientes:

    def obtener_total_ventas_por_cliente(self, concesionaria_id, cliente_id):
        # Obtenemos la concesionaria por ID
        servicio_conc = servicio_concesionarias.ServicioConcesionarias()
        concesionaria = servicio_conc.obtener_por_id(concesionaria_id)

        if concesionaria is None:
            return 0  # Concesionaria no existe

        # Verificamos si el cliente existe 
        cliente_id_int = int(cliente_id)
        cliente_existe = any(
            c.obtenerNumeroId() == int(cliente_id_int) 
            for c in concesionaria.obtener_clientes()
        )
        if not cliente_existe:
            return 0  # Cliente no existe 

        # Recorremos todas las sucursales y sus ventas para sumar las del cliente
        total = 0
        for sucursal in concesionaria.obtener_sucursales():
            for venta in sucursal.obtenerVentas():
                if venta.obtenerClienteId() == int(cliente_id):
                    total += venta.obtenerMonto()

        return total