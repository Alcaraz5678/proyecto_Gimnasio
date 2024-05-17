from Usuario import Usuario
from Actividad import Actividad
from Reserva import Reserva


class AlmacenInformacion:

    def __init__(self):
        self.usuarios: [Usuario] = []
        self.actividades: [Actividad] = []
        self.reservas: [Reserva] = []

    def leer_usuario(self):
        # leer el archivo de los usuarios y crear los objetos, y almacenarlos
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
        # leer el archivo donde estan todas las actividades, crear los objetos y almacenar
        pass

    def leer_reserva(self):
        # leer el archivo de reservas, crear el objeto Reserva, buscar el usuario en self.usuarios
        # agregar reserva a ese usuario
        pass

# archivo usuaario: nombre, doc, contr
# reserva: id_reserva, id_actividad, doc_usuario
# actividad: nombre, id, hora_inicio, hora_fin, año, mes, dia