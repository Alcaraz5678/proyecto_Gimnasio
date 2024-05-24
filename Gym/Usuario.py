from Reserva_actividad import ReservaActividad

class Usuario:

    def __init__(self, nombre: str, ctr: str, documento: int):
        self.nombre: str = nombre
        self.ctr: str = ctr
        self.documento: int = documento
        self.reservas: [ReservaActividad] = []
