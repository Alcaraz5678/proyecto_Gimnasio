from Interfaz_principal import InterfazInicial
from Almacen_informacion import AlmacenInformacion

if __name__ == "__main__":
    datos = AlmacenInformacion()
    datos.leer_usuario()
    app = InterfazInicial(datos)
    app.visualizar()
