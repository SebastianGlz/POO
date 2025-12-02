from tkinter import *
from tkinter import messagebox
from model import cochesBD

class View:
    def __init__(self,ventana):
        self.ventana=ventana
        ventana.title("..: Coches System :..")
        ventana.geometry("800x600")
        ventana.resizable(False,False)
        self.menu_principal(ventana)

    @staticmethod
    def borrarPantalla(ventana):
        for widget in ventana.winfo_children():
            widget.destroy()

    @staticmethod
    def menu_principal(ventana):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text="..:: Menú Principal ::..",justify="center",font=("Arial",24))
        lbl_titulo.pack()

        btn_autos=Button(ventana,text="Autos",font=("Arial",12),command=lambda:View.menu_acciones(ventana, "Autos"))
        btn_autos.pack(pady=30)

        btn_camionetas=Button(ventana,text="Camionetas",font=("Arial",12),command=lambda:View.menu_acciones(ventana, "Camionetas"))
        btn_camionetas.pack(pady=30)

        btn_camiones=Button(ventana,text="Camiones",font=("Arial",12),command=lambda:View.menu_acciones(ventana, "Camiones"))
        btn_camiones.pack(pady=30)

        btn_salir=Button(ventana,text="Salir",font=("Arial",12),command=ventana.quit)
        btn_salir.pack(pady=30)
    
    @staticmethod
    def menu_acciones(ventana, categoria=None):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text="..:: Menú de Acciones ::..",justify="center",font=("Arial",24))
        lbl_titulo.pack()

        lbl_categoria=Label(ventana, text=f"Sección: {categoria}" if categoria else "Sección: --", font=("Arial",14))
        lbl_categoria.pack(pady=10)

        btn_insertar=Button(ventana,text="Insertar",font=("Arial",12),command=lambda:View.insertar_vehiculo(ventana, categoria))
        btn_insertar.pack(pady=20)

        btn_consultar=Button(ventana,text="Consultar",font=("Arial",12),command=lambda:"")
        btn_consultar.pack(pady=20)

        btn_actualizar=Button(ventana,text="Actualizar",font=("Arial",12),command=lambda:"")
        btn_actualizar.pack(pady=20)

        btn_eliminar=Button(ventana,text="Eliminar",font=("Arial",12),command=lambda:"")
        btn_eliminar.pack(pady=20)

        btn_regresar=Button(ventana,text="Regresar",font=("Arial",12),command=lambda:View.menu_principal(ventana))
        btn_regresar.pack(pady=20)

    @staticmethod
    def insertar_vehiculo(ventana, categoria):
        View.borrarPantalla(ventana)
        lbl_titulo=Label(ventana,text=f"..:: Insertar {categoria} ::..",justify="center",font=("Arial",24))
        lbl_titulo.pack()

        lbl_marca=Label(ventana,text="Marca:",font=("Arial",12))
        lbl_marca.pack(pady=10)
        Entry_marca=Entry(ventana)
        Entry_marca.pack(pady=10)

        lbl_color=Label(ventana,text="Color:",font=("Arial",12))
        lbl_color.pack(pady=10)
        Entry_color=Entry(ventana)
        Entry_color.pack(pady=10)

        lbl_modelo=Label(ventana,text="Modelo:",font=("Arial",12))
        lbl_modelo.pack(pady=10)
        Entry_modelo=Entry(ventana)
        Entry_modelo.pack(pady=10)

        lbl_velocidad=Label(ventana,text="Velocidad:",font=("Arial",12))
        lbl_velocidad.pack(pady=10)
        Entry_velocidad=Entry(ventana)
        Entry_velocidad.pack(pady=10)

        lbl_caballaje=Label(ventana,text="Caballaje:",font=("Arial",12))
        lbl_caballaje.pack(pady=10)
        Entry_caballaje=Entry(ventana)
        Entry_caballaje.pack(pady=10)

        lbl_plazas=Label(ventana,text="Plazas:",font=("Arial",12))
        lbl_plazas.pack(pady=10)
        Entry_plazas=Entry(ventana)
        Entry_plazas.pack(pady=10)

        btn_guardar=Button(ventana,text="Guardar",font=("Arial",12),command=lambda:"")
        btn_guardar.pack(pady=20)


        btn_regresar=Button(ventana,text="Regresar",font=("Arial",12),command=lambda:View.menu_acciones(ventana, categoria))
        btn_regresar.pack(pady=20)