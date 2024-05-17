from Interfaz_principal import InterfazInicial
from Almacen_informacion import AlmacenInformacion

if __name__ == "__main__":
    datos = AlmacenInformacion()
    datos.leer_usuario()
    datos.leer_actividades()
    datos.leer_reserva()
    app = InterfazInicial(datos)
    app.visualizar()
