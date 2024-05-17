from Usuario import Usuario
from Actividad import Actividad
from Reserva import Reserva
from Horario import Horario
from Fecha import Fecha


class AlmacenInformacion:

    def __init__(self):
        self.usuarios: [Usuario] = []
        self.actividades: [Actividad] = []
        self.reservas: [Reserva] = []
        self.id_reserva_actual: int = 0

    def leer_usuario(self):
        try:
            with open("/home/lia/PycharmProjects/Gimnasio_POO/Documentos/usuarios.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(", ")
                    if len(parts) == 3:
                        nombre = parts[0].split(": ")[1]
                        documento = parts[1].split(": ")[1]
                        ctr = parts[2].split(": ")[1]
                        usuario = Usuario(nombre, ctr, int(documento))
                        self.usuarios.append(usuario)
        except FileNotFoundError:
            print("El archivo usuarios.txt no existe.")

    def leer_actividades(self):
        try:
            with open("/home/lia/PycharmProjects/Gimnasio_POO/Documentos/actividades.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(", ")
                    if len(parts) == 7:
                        nombre = parts[0].split(": ")[1]
                        id = int(parts[1].split(": ")[1])
                        hora_inicio = int(parts[2].split(": ")[1].split(":")[0])
                        hora_fin = int(parts[3].split(": ")[1].split(":")[0])
                        horario = Horario(hora_inicio, hora_fin)
                        actividad = Actividad(id, nombre, horario)
                        self.actividades.append(actividad)
        except FileNotFoundError:
            print("El archivo actividades.txt no existe.")

    def leer_reserva(self):
        try:
            with open("/home/lia/PycharmProjects/Gimnasio_POO/Documentos/reservas.txt", "r") as file:
                for line in file:
                    parts = line.strip().split(", ")
                    id_reserva = int(parts[0].split(": ")[1])
                    id_actividad = int(parts[1].split(": ")[1])
                    documento = int(parts[2].split(": ")[1])
                    dia = parts[3].split(": ")[1]
                    mes = parts[4].split(": ")[1]
                    ano = parts[5].split(": ")[1]

                    fecha = Fecha(dia, mes, ano)
                    reserva = Reserva(id_reserva, id_actividad, documento, fecha)
                    self.reservas.append(reserva)
                    # añadir a ese usuario el objeto de Reserva
                    for u in self.usuarios:
                        if u.documento == int(documento):
                            u.reservas.append(reserva)
        except FileNotFoundError:
            print("El archivo de reservas no existe.")
        except Exception as e:
            print(f"Error al leer el archivo de reservas: {e}")
