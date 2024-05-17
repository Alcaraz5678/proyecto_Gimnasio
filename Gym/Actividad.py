from Horario import Horario


class Actividad:
    def __init__(self, id: int, nombre: str, horario: Horario):
        self.id: int = id
        self.nombre: str = nombre
        self.horario: Horario = horario
