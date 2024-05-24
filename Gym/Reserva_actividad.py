from Reserva import Reserva
from Fecha import Fecha


class ReservaActividad(Reserva):
    def __init__(self, id_reserva: int, id_actividad: int, doc_usuario: int, fecha: Fecha):
        super().__init__(id_reserva, doc_usuario, fecha)
        self.id_actividad: int = id_actividad
