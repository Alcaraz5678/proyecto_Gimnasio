from Interfaz_principal import InterfazInicial
from Gimnasio import Gimnasio

if __name__ == "__main__":
    datos = Gimnasio()
    datos.leer_usuario()
    datos.leer_actividades()
    datos.leer_reserva_act()
    datos.leer_reserva_bloque()
    app = InterfazInicial(datos)
    app.visualizar()
