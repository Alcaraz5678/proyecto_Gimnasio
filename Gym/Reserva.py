from Fecha import Fecha

class Reserva:
    def __init__(self, id_reserva: int, id_actividad: int, doc_usuario: int, fecha: Fecha):
        self.id_reserva: int = id_reserva
        self.id_actividad: int = id_actividad
        self.documento_usuario: int = doc_usuario
        self.fecha: Fecha = fecha

