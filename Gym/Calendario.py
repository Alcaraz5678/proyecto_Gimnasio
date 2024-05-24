import tkinter as tk
from tkcalendar import Calendar


class CalendarioActividades(tk.Tk):
    def __init__(self, actividades_por_fecha):
        super().__init__()
        self.title("Calendario de Actividades")
        self.geometry("600x400")

        self.calendario = Calendar(self, selectmode="day", date_pattern="y-mm-dd")
        self.calendario.pack(pady=20)

        self.actividades_por_fecha = actividades_por_fecha

        self.calendario.bind("<<CalendarSelected>>", self.seleccionar_fecha)

        self.lista_actividades = tk.Listbox(self, width=50, height=10)
        self.lista_actividades.pack(pady=5)

        self.mostrar_actividades(self.calendario.get_date())

    def seleccionar_fecha(self, event=None):
        fecha_seleccionada = self.calendario.get_date()
        self.mostrar_actividades(fecha_seleccionada)

    def mostrar_actividades(self, fecha):
        self.lista_actividades.delete(0, tk.END)
        print(self.actividades_por_fecha)
        if fecha in self.actividades_por_fecha:
            actividades = self.actividades_por_fecha[fecha]
            for actividad in actividades:
                self.lista_actividades.insert(tk.END, actividad)
