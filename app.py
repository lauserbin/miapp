import tkinter as tk
import json
from tkintermapview import TkinterMapView

ventana = tk.Tk()
ventana.title("tour de musica")
ventana.geometry("500x500+500+50")
ventana.resizable(width=False, height=False)

usuario = tk.StringVar()
password = tk.StringVar()
surname = tk.StringVar()

etiqueta1 = tk.Label(ventana, text="escribe tu nombre")
etiqueta1.place(x=100, y=100)
etiqueta2 = tk.Label(ventana, text="escribe tu contraseña")
etiqueta2.place(x=100, y=300)
etiqueta3 = tk.Label(ventana, text="escribe tu apellido")
etiqueta3.place(x=100,y=200)

entrada = tk.Entry(ventana, textvar=usuario, width=22, relief="flat")
entrada.place(x=255, y=100)

entrada2 = tk.Entry(ventana, textvar=password, width=22, relief="flat")
entrada2.place(x=255, y=300)

entrada3 = tk.Entry(ventana, textvar=surname,width=22,relief="flat")
entrada3.place(x=255,y=200)

def login():
    nombre = usuario.get()
    contraseña = password.get()
    apellido = surname.get()

    if nombre == "lautaro" and contraseña == "2023" and apellido== "serbin":
        correcta()
    else:
        incorrecta()

def correcta():
    ventana.withdraw()
    window = tk.Toplevel()
    window.title("tour de musica(bienvenido)")
    window.geometry("500x500+500+50")
    window.resizable(width=False, height=False)
    informacion_eventos= tk.Label(window, text="presiona eventos para conseguir informacion",font=("comic Sans MS", 12, "bold"))
    informacion_eventos.place(x=20, y=100)

    informacion_eventos1= tk.Label(window, text="presiona ubicacion para ver las ciudades",font=("comic Sans MS", 12, "bold"))
    informacion_eventos1.place(x=20, y=200)
    
    informacion_eventos2= tk.Label(window, text=" donde se llevan a cabo eventos",font=("comic Sans MS", 12, "bold"))
    informacion_eventos2.place(x=20, y=250)

    def regresar():
        window.withdraw()
        ventana.deiconify()

    def eventos():
        ventana.withdraw()
        ventana2 = tk.Toplevel()
        ventana2.title("eventos disponibles")
        ventana2.geometry("500x500+500+50")
        ventana2.resizable(width=False, height=False)

        lista_eventos = ["evento 1", "evento 2", "evento 3", "evento 4", "evento 5"]
        

        listbox = tk.Listbox(ventana2)
        listbox.pack(padx=20, pady=20)

        for evento in lista_eventos:
            listbox.insert(tk.END, evento)

            listbox.bind("<Double-Button-1>", mostrar_descripcion)

    def mostrar_descripcion(event):
        listbox = event.widget
        seleccion = listbox.get(listbox.curselection())
        descripcion = obtener_descripcion_objeto(seleccion)

        if descripcion:
            ventana_descripcion = tk.Toplevel()
            ventana_descripcion.title("Descripción del evento")
            ventana_descripcion.geometry("700x450")
            ventana_descripcion.resizable(width=False, height=False)

            etiquetas = []
            for palabra, informacion in descripcion.items():
                etiqueta = tk.Label(ventana_descripcion, text=f"{palabra}: {informacion}")
                etiqueta.pack(padx=10, pady=5)
                etiquetas.append(etiqueta)

    def mostrar_ubicacion():
        ventana.withdraw()
        ventana_ubicacion = tk.Toplevel()
        ventana_ubicacion.title("Ubicación")
        ventana_ubicacion.geometry("500x500+500+50")
        ventana_ubicacion.resizable(width=False, height=False)

        map_widget = TkinterMapView(ventana_ubicacion,width=600,height=400,corner_radius=0)

        map_widget.pack(fill="both",expand=True)



        map_widget.set_address("Resistencia Chaco Argentina",marker=True)
        map_widget.set_address("Cordoba Argentina",marker=True)
        map_widget.set_address("Bariloche Rio Negro Argentina",marker=True)
        map_widget.set_address("General Acha La Pampa Argentina",marker=True)
        map_widget.set_address("San Antonio de los Cobres Salta Argentina",marker=True)
        map_widget.set_address("Argentina")




    boton_ubicacion = tk.Button(window, text="Ubicación", command=mostrar_ubicacion, cursor="hand2", width=13, relief="flat", font=("Comic Sans MS", 12, "bold"))
    boton_ubicacion.place(x=300, y=400)

    boton_eventos = tk.Button(window, text="eventos", command=eventos, cursor="hand2", width=13, relief="flat", font=("Comic Sans MS", 12, "bold"))
    boton_eventos.place(x=60, y=400)

    boton_regresar = tk.Button(window, text="regresar", command=regresar, cursor="hand2", width=13, relief="flat", font=("Comic Sans MS", 12, "bold"))
    boton_regresar.place(x=180, y=400)


def obtener_descripcion_objeto(nombre_objeto):
    with open('data.json') as json_file:
        data = json.load(json_file)
        eventos = data["eventos"]
        for evento in eventos:
            if evento["nombre"] == nombre_objeto:
                return evento["descripcion"]
        return None
    

def incorrecta():
    ventana.withdraw()
    root = tk.Toplevel()
    root.title("tour de musica(bienvenido)")
    root.geometry("500x500+500+50")
    root.resizable(width=False, height=False)

    def regresar():
        root.withdraw()
        ventana.deiconify()

    boton4 = tk.Button(root, text="intentar de nuevo", command=regresar, cursor="hand2", width=19, relief="flat", font=("Comic Sans MS", 12, "bold"))
    boton4.place(x=148, y=400)

def salir():
    ventana.destroy()

boton = tk.Button(ventana, text="entrar", command=login, cursor="hand2", width=12, relief="flat", font=("comic Sans MS", 12, "bold"))
boton.place(x=60, y=405)

boton1 = tk.Button(ventana, text="salir", command=salir, cursor="hand2", width=12, relief="flat", font=("Comic Sans MS", 12, "bold"))
boton1.place(x=310, y=405)

ventana.mainloop()