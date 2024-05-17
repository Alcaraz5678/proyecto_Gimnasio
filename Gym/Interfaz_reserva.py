from Usuario import Usuario
import tkinter as tk
from tkinter import messagebox,ttk
from Almacen_informacion import AlmacenInformacion
from Actividad import Actividad
from Calendario import CalendarioActividades


class InterfazReserva:
    def __init__(self, usuario: Usuario, almacen: AlmacenInformacion):
        self.usuario: Usuario = usuario
        self.ventana_reserva = tk.Tk()
        self.ventana_reserva.title("Interfaz Reserva")
        self.centrar_ventana(self.ventana_reserva, 300, 200)
        self.crear_ventana_principal()
        self.almacen: AlmacenInformacion = almacen

    def centrar_ventana(self, ventana, ancho_, alto_):
        ancho = ventana.winfo_screenwidth()
        alto = ventana.winfo_screenheight()

        x = (ancho - ancho_) // 2
        y = (alto - alto_) // 2
        ventana.geometry(f"{ancho_}x{alto_}+{x}+{y}")

    def crear_ventana_principal(self):
        mostrar_reservas_boton = tk.Button(self.ventana_reserva, text="Mostrar Mi Calendario", command=self.mostrar_mis_reservas)
        mostrar_reservas_boton.pack(pady=20)
        reservar_act_boton = tk.Button(self.ventana_reserva, text="Reservar Actividad", command=self.interfaz_reservar_actividad)
        reservar_act_boton.pack(pady=20)
        cancelar_reserva_boton = tk.Button(self.ventana_reserva, text="Cancelar Reserva", command=self.interfaz_cancelar_reserva)
        cancelar_reserva_boton.pack(pady=20)

    def buscar_actividad(self, id_actividad):
        # con el id de la actividad mostrar la información de la misma
        for act in self.almacen.actividades:
            if act.id == id_actividad:
                return act.nombre, act.horario

    def formato_fecha(self, dia_mes):
        if len(dia_mes) == 1:
            return "0"+dia_mes
    def mostrar_mis_reservas(self):
        reservas_usuario = [reserva for reserva in self.almacen.reservas if reserva.documento_usuario == self.usuario.documento]
        self.ventana_reserva.destroy()
        if reservas_usuario:
            reservas_por_fecha = {}

            for reserva in reservas_usuario:
                fecha = f"{reserva.fecha.ano}-{self.formato_fecha(reserva.fecha.mes)}-{self.formato_fecha(reserva.fecha.dia)}"
                actividad = (f"{self.buscar_actividad(reserva.id_actividad)[0]}, Horario: "
                             f"{self.buscar_actividad(reserva.id_actividad)[1].hora_inicio} - "
                             f"{self.buscar_actividad(reserva.id_actividad)[1].hora_fin}")

                if fecha in reservas_por_fecha:
                    reservas_por_fecha[fecha].append(actividad)
                else:
                    reservas_por_fecha[fecha] = [actividad]
            # enviar a la interfaz de calendario
            calendario = CalendarioActividades(reservas_por_fecha)
            calendario.mainloop()

        else:
            messagebox.showinfo("Mis Reservas", "No tienes reservas.")

    def interfaz_reservar_actividad(self):
        self.ventana_actividad = tk.Toplevel(self.ventana_reserva)
        self.ventana_actividad.title("Actividades")
        self.centrar_ventana(self.ventana_actividad, 400, 450)

        self.actividades_lista = tk.Listbox(self.ventana_actividad)
        for actividad in self.almacen.actividades:
            self.actividades_lista.insert(tk.END, f"{actividad.id}: {actividad.nombre} -> {actividad.horario.hora_inicio}-{actividad.horario.hora_fin}")
        self.actividades_lista.pack()

        tk.Label(self.ventana_actividad, text="Ingrese el ID de la actividad a reservar:").pack(pady=5)
        self.id_entry = tk.Entry(self.ventana_actividad)
        self.id_entry.pack(pady=5)

        seleccionar_fecha_boton = tk.Button(self.ventana_actividad, text="Seleccionar fecha",
                                           command=self.interfaz_fecha)
        seleccionar_fecha_boton.pack(pady=5)

        reservas_boton = tk.Button(self.ventana_actividad, text="Reservar", command=self.reservar_actividad)
        reservas_boton.pack(pady=20)

    def mostrar_actividades(self, i: Actividad):
        messagebox.showinfo("Reserva", f"La reserva número {i.id} fue añadida con éxito!")

    def interfaz_fecha(self):
        self.ventana_fecha = tk.Toplevel(self.ventana_reserva)
        self.ventana_fecha.title("Fecha")
        self.centrar_ventana(self.ventana_fecha, 400, 450)

        self.dia_var = tk.StringVar()
        self.mes_var = tk.StringVar()
        self.ano_var = tk.StringVar()

        dias = [str(i) for i in range(1, 33)]
        meses = [str(i) for i in range(1, 13)]
        anos = [str(i) for i in range(2020, 2030)]

        dia_label = ttk.Label(self.ventana_fecha, text="Día:")
        mes_label = ttk.Label(self.ventana_fecha, text="Mes:")
        ano_label = ttk.Label(self.ventana_fecha, text="Año:")

        self.dia_cb = ttk.Combobox(self.ventana_fecha, textvariable=self.dia_var, values=dias, state="readonly")
        self.mes_cb = ttk.Combobox(self.ventana_fecha, textvariable=self.mes_var, values=meses, state="readonly")
        self.ano_cb = ttk.Combobox(self.ventana_fecha, textvariable=self.ano_var, values=anos, state="readonly")

        dia_label.grid(row=0, column=0, padx=5, pady=5)
        self.dia_cb.grid(row=0, column=1, padx=5, pady=5)
        mes_label.grid(row=1, column=0, padx=5, pady=5)
        self.mes_cb.grid(row=1, column=1, padx=5, pady=5)
        ano_label.grid(row=2, column=0, padx=5, pady=5)
        self.ano_cb.grid(row=2, column=1, padx=5, pady=5)

        fecha_ok = tk.Button(self.ventana_fecha, text="Guardar fecha", command=self.obtener_fecha)
        fecha_ok.grid(pady=20)

    def obtener_fecha(self):
        dia = self.dia_cb.get()
        mes = self.mes_cb.get()
        ano = self.ano_cb.get()
        self.ventana_fecha.withdraw()
        return dia, mes, ano

    def reservar_actividad(self):
        id_actividad = int(self.id_entry.get())
        dia, mes, ano = self.obtener_fecha()
        try:
            actividad = False
            for i in self.almacen.actividades:
                if i.id == id_actividad:
                    actividad = True
                    self.ventana_actividad.destroy()
                    self.ventana_reserva.destroy()
                    self.mostrar_actividades(i)
                    self.almacen.id_reserva_actual += 1
                    # escribir archivo de las reservas
                    with open("/home/lia/PycharmProjects/Gimnasio_POO/Documentos/reservas.txt", "a") as file:
                        file.write(f"Id_reserva: {self.almacen.id_reserva_actual}, Id_actividad: {id_actividad}, "
                                   f"Documento: {self.usuario.documento}, Dia: {dia}, Mes: {mes}, Año: {ano}\n")
                    break
            if not actividad:
                raise ValueError("Id no encontrado!.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def interfaz_cancelar_reserva(self):
        self.ventana_cancelar = tk.Toplevel(self.ventana_reserva)
        self.ventana_cancelar.title("Cancelar Reserva")
        self.centrar_ventana(self.ventana_cancelar, 400, 200)

        tk.Label(self.ventana_cancelar, text="Ingrese el ID de la reserva a cancelar:").pack(pady=5)
        self.cancelar_entry = tk.Entry(self.ventana_cancelar)
        self.cancelar_entry.pack(pady=5)

        cancelar_boton = tk.Button(self.ventana_cancelar, text="Cancelar Reserva", command=self.cancelar_reserva)
        cancelar_boton.pack(pady=20)

    def cancelar_reserva(self):
        id_reserva = int(self.cancelar_entry.get())
        self.ventana_reserva.destroy()
        try:
            reserva_a_cancelar = None
            for reserva in self.almacen.reservas:
                if reserva.id_reserva == id_reserva and reserva.documento_usuario == self.usuario.documento:
                    reserva_a_cancelar = reserva
                    break
            if reserva_a_cancelar:
                self.almacen.reservas.remove(reserva_a_cancelar)
                messagebox.showinfo("Cancelar Reserva", f"La reserva número {id_reserva} fue cancelada con éxito!")

                with open("/home/lia/PycharmProjects/Gimnasio_POO/Documentos/reservas.txt", "r") as file:
                    lineas = file.readlines()

                # reescribir el archivo sin la línea de la reserva cancelada
                with open("/home/lia/PycharmProjects/Gimnasio_POO/Documentos/reservas.txt", "w") as file:
                    for linea in lineas:
                        if not linea.startswith(
                                f"Id_reserva: {reserva_a_cancelar.id_reserva}, Id_actividad: {reserva_a_cancelar.id_actividad}, Documento: {reserva_a_cancelar.documento_usuario}"):
                            file.write(linea)
            else:
                raise ValueError("Reserva no encontrada o no pertenece al usuario.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
