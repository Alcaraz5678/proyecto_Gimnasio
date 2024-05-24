from Reserva import Reserva
from Fecha import Fecha


class ReservaBloque(Reserva):
    def __init__(self, id_bloque: int, hora_inicio: str, hora_fin: str, doc_usuario: int, fecha: Fecha):
        super().__init__(id_bloque, doc_usuario, fecha)
        self.hora_inicio: str = hora_inicio
        self.hora_fin: str = hora_fin
