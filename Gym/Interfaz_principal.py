import tkinter as tk
from tkinter import messagebox
from Almacen_informacion import AlmacenInformacion
from Interfaz_reserva import InterfazReserva


class InterfazInicial:
    def __init__(self, almacen: AlmacenInformacion):
        self.ventana_principal = tk.Tk()
        self.ventana_principal.title("Interfaz Inicial")
        self.centrar_ventana(self.ventana_principal,300, 200)
        self.crear_ventana_principal()
        self.almacen = almacen

    def centrar_ventana(self, ventana, ancho_, alto_):
        ancho = ventana.winfo_screenwidth()
        alto = ventana.winfo_screenheight()

        # con el tamaño de la ventana, calcular el centro y ubicar la ventana
        x = (ancho - ancho_) // 2
        y = (alto - alto_) // 2
        ventana.geometry(f"{ancho_}x{alto_}+{x}+{y}")

    def crear_ventana_principal(self):
        iniciar = tk.Button(self.ventana_principal, text="Iniciar Sesión", command=self.interfaz_iniciar_sesion)
        iniciar.pack(pady=20)

        registrarse = tk.Button(self.ventana_principal, text="Registrarse", command=self.interfaz_registrar_usuario)
        registrarse.pack(pady=20)

    def interfaz_iniciar_sesion(self):
        self.ventana_ingreso = tk.Toplevel(self.ventana_principal)
        self.ventana_ingreso.title("Iniciar sesión")
        self.centrar_ventana(self.ventana_ingreso, 300, 250)

        tk.Label(self.ventana_ingreso, text="Documento:").pack(pady=5)
        self.documento_usuario_IS = tk.Entry(self.ventana_ingreso)
        self.documento_usuario_IS.pack(pady=5)

        tk.Label(self.ventana_ingreso, text="Contraseña:").pack(pady=5)
        self.contr_IS = tk.Entry(self.ventana_ingreso, show='*')
        self.contr_IS.pack(pady=5)

        tk.Button(self.ventana_ingreso, text="Iniciar sesión", command=self.iniciar_sesion_usuario).pack(pady=20)

    def interfaz_registrar_usuario(self):
        self.ventana_registro = tk.Toplevel(self.ventana_principal)
        self.ventana_registro.title("Registro")
        self.centrar_ventana(self.ventana_registro, 300, 250)

        tk.Label(self.ventana_registro, text="Nombre:").pack(pady=5)
        self.nombre_usuario = tk.Entry(self.ventana_registro)
        self.nombre_usuario.pack(pady=5)

        tk.Label(self.ventana_registro, text="Documento:").pack(pady=5)
        self.documento_usuario = tk.Entry(self.ventana_registro)
        self.documento_usuario.pack(pady=5)

        tk.Label(self.ventana_registro, text="Contraseña:").pack(pady=5)
        self.contr = tk.Entry(self.ventana_registro, show='*') # contraseña del usuario
        self.contr.pack(pady=5)

        tk.Button(self.ventana_registro, text="Registrar", command=self.registrar_usuario).pack(pady=20)

    def iniciar_sesion_usuario(self):
        documento_usuario_IS = int(self.documento_usuario_IS.get())
        contr_IS = self.contr_IS.get()
        try:
            usuario_encontrado = False
            for i in self.almacen.usuarios:
                if i.documento == documento_usuario_IS and i.ctr == contr_IS:
                    usuario_encontrado = True
                    self.ventana_ingreso.destroy()
                    messagebox.showinfo("Iniciar Sesión", f"Bienvenido {i.nombre}!")
                    interfaz_reserva = InterfazReserva(i, self.almacen)
                    break
            if not usuario_encontrado:
                raise ValueError("Usuario o contraseña incorrectos.")
        except ValueError as e:
            self.ventana_ingreso.destroy()
            messagebox.showerror("Error", str(e))

    def registrar_usuario(self):
        # obtener los datos y almacenarlos
        nombre = self.nombre_usuario.get()
        documento = self.documento_usuario.get()
        contr = self.contr.get()

        if not nombre or not documento or not contr:
            messagebox.showerror("Error", "Todos los campos son obligatorios!")
            return

        with open("/home/lia/PycharmProjects/Gimnasio_POO/Documentos/usuarios.txt", "a") as file:
            file.write(f"Nombre: {nombre}, Documento: {documento}, Contraseña: {contr}\n")

        self.ventana_registro.destroy()
        messagebox.showinfo("Usuario registrado", "Registro exitoso!")

    def visualizar(self):
        self.ventana_principal.mainloop()
