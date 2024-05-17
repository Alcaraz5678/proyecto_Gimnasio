from Usuario import Usuario
import tkinter as tk
from tkinter import messagebox


class InterfazReserva:
    def __init__(self, usuario: Usuario):
        self.usuario: Usuario = usuario
        self.ventana_reserva = tk.Tk()
        self.ventana_reserva.title("Interfaz Reserva")
        self.centrar_ventana(self.ventana_reserva, 300, 200)
        self.crear_ventana_principal()

    def centrar_ventana(self, ventana, ancho_, alto_):
        ancho = ventana.winfo_screenwidth()
        alto = ventana.winfo_screenheight()

        x = (ancho - ancho_) // 2
        y = (alto - alto_) // 2
        ventana.geometry(f"{ancho_}x{alto_}+{x}+{y}")

    def crear_ventana_principal(self):
        mostrar_reservas_boton = tk.Button(self.ventana_reserva, text="Mostrar Mis Reservas",
                                                  command=self.mostrar_mis_reservas)
        mostrar_reservas_boton.pack(pady=20)

        reservar_act_boton = tk.Button(self.ventana_reserva, text="Reservar Actividad",
                                              command=self.reservar_actividad)
        reservar_act_boton.pack(pady=20)

        cancelar_reserva_boton = tk.Button(self.ventana_reserva, text="Cancelar Reserva",
                                                   command=self.cancelar_reserva)
        cancelar_reserva_boton.pack(pady=20)

    def mostrar_mis_reservas(self):
        messagebox.showinfo("Mis Reservas", "Funcionalidad para mostrar reservas.")

    def reservar_actividad(self):
        messagebox.showinfo("Reservar Actividad", "Funcionalidad para reservar una actividad.")

    def cancelar_reserva(self):
        messagebox.showinfo("Cancelar Reserva", "Funcionalidad para cancelar una reserva.")
