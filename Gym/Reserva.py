from Fecha import Fecha


class Reserva:
    def __init__(self, id_reserva: int, doc_usuario: int, fecha: Fecha):
        self.id_reserva: int = id_reserva
        self.documento_usuario: int = doc_usuario
        self.fecha: Fecha = fecha
