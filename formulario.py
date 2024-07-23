import tkinter as tk
from tkinter import messagebox
import matplotlib
matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib.figure import Figure
from main_hospitales import main_aux
from main_hospitales import mostrar_grafico1
from main_hospitales import mostrar_flujo_max
from customtkinter import CTk, CTkFrame, CTkLabel, CTkEntry, CTkButton
from tkinter import PhotoImage

# Variables para el formulario del gráfico
formulario_grafico = None
lienzo_grafico = None
barra_herramientas = None

def Crear_ventana():
    # Función para mostrar el gráfico en el formulario
    def mostrar_grafico():
        global formulario_grafico, lienzo_grafico, barra_herramientas

        figura=mostrar_grafico1()

        # Si el formulario del gráfico ya existe, destruir la instancia anterior
        if formulario_grafico:
            formulario_grafico.destroy()

        # Crear el formulario del gráfico y el lienzo del gráfico
        formulario_grafico = tk.Frame(marco_izquierdo)
        formulario_grafico.pack(pady=10)

        lienzo_grafico = FigureCanvasTkAgg(figura, master=formulario_grafico)
        lienzo_grafico.draw()
        lienzo_grafico.get_tk_widget().pack()

        # Crear la barra de herramientas
        barra_herramientas = NavigationToolbar2Tk(lienzo_grafico, formulario_grafico)
        barra_herramientas.update()
        barra_herramientas.pack()


    # Función para filtrar pacientes por síntomas y mostrarlos en el formulario
    def filtrar_pacientes():
        sintoma1 = campo_sintoma1.get()
        sintoma2 = campo_sintoma2.get()

        # Lógica para filtrar pacientes según los síntomas
        # Aquí puedes utilizar tus propias funciones y datos
        pacientes_filtrados=main_aux(sintoma1,sintoma2)

        # Mostrar los pacientes filtrados en el formulario
        resultado_text.delete('1.0', tk.END)
        for paciente in pacientes_filtrados:
            resultado_text.insert(tk.END, paciente + '\n')
            
    def flujo_max():
        flujo_maximo = mostrar_flujo_max()
        result_max_text.insert()
        
        
        
    
   # Crear la ventana principal
    inicio.withdraw()
    ventana = tk.Toplevel()
    ventana.title('Hos-Friend')
    ventana.geometry('500x600+40+20')
    ventana.minsize(1600,800)
    ventana.config(bg = '#010101')
    inicio.call('wm','iconphoto',ventana._w,PhotoImage(file='images/LogoPrincipal.png'))

    # Crear el marco izquierdo para el gráfico
    marco_izquierdo = tk.Frame(ventana, bg= '#010101', width=400, height=400)
    marco_izquierdo.pack(side=tk.LEFT, padx=50)

    # Crear el marco derecho para los síntomas y pacientes filtrados
    marco_derecho = tk.Frame(ventana, bg= '#010101', width=300, height=300)
    marco_derecho.pack(side=tk.RIGHT,padx=50,pady=50)



    # Agregar etiquetas y campos de entrada para los síntomas en el marco derecho
    etiqueta_sintoma1 = tk.Label(marco_derecho, text='Síntoma 1:', fg= "#7abae6", bg= '#010101', font=('sans rerif',12))
    etiqueta_sintoma1.pack(pady=5)

    campo_sintoma1 = CTkEntry(marco_derecho, fg_color="#010101", text_color="#2cb67d",border_color="#2cb67d", font=('sans rerif',12), placeholder_text='Inserte sintomas:', placeholder_text_color="#aea5bb")
    campo_sintoma1.pack(pady=5)

    etiqueta_sintoma2 = tk.Label(marco_derecho, text='Síntoma 2:', fg= "#7abae6", bg= '#010101', font=('sans rerif',12))
    etiqueta_sintoma2.pack(pady=5)

    campo_sintoma2 = CTkEntry(marco_derecho, fg_color="#010101", text_color="#2cb67d",border_color="#2cb67d", font=('sans rerif',12), placeholder_text='Inserte sintomas:', placeholder_text_color="#aea5bb")
    campo_sintoma2.pack(pady=5)

    # Agregar botón para filtrar pacientes en el marco derecho
    filtrar_btn = CTkButton(marco_derecho, text='Filtrar Pacientes', command=filtrar_pacientes, corner_radius=12, fg_color="#010101", border_color="#e5afb4",border_width=1.2, hover_color="#89666a")
    filtrar_btn.pack(pady=10)

    # Agregar un widget de texto para mostrar los pacientes filtrados
    resultado_text = tk.Text(marco_derecho, height=20, width=80, bg="#010101", fg= "#7abae6", font=('sans rerif',12))
    resultado_text.pack(pady=10)

    # Agregar botón para Flujo maximo de personas en los hospitales
    flujo_btn = CTkButton(marco_derecho, text='Flujo máximo de pacientes', command=flujo_max, corner_radius=12, fg_color="#010101", border_color="#e5afb4",border_width=1.2, hover_color="#89666a")
    flujo_btn.pack(pady=10)
    
    # Agregar un widget de texto para mostrar Flujo maximo
    result_max_text = tk.Text(marco_derecho, height=4, width=80, bg="#010101", fg= "#7abae6", font=('sans rerif',12))
    result_max_text.pack(pady=10)

    # Mostrar el gráfico en el formulario del gráfico al presionar el botón correspondiente
    mostrar_grafico_btn = CTkButton(marco_izquierdo, text='Mostrar Gráfico', command=mostrar_grafico, corner_radius=12, fg_color="#010101", border_color="#d5afe5",border_width=1.2, hover_color="#7a6689")
    mostrar_grafico_btn.pack(pady=10) 
    ventana.mainloop()


def cerrarventana():
    inicio.destroy()

inicio = tk.Tk()
inicio.title('Hos-Friend')
inicio.geometry('500x600+40+20')
inicio.minsize(1600,800)
inicio.config(bg = '#010101')


frame = CTkFrame(inicio, fg_color='#010101')
frame.grid(column=0, row = 0, sticky='nsew', padx=100, pady=50)

inicio.columnconfigure(0, weight=1)
inicio.rowconfigure(0, weight=1)


Logo = CTkLabel(inicio, image=PhotoImage(file='images/LogoPrincipal.png', gamma=0.2), text='')
Logo.grid(columnspan = 2, row=0)

Name = tk.Label(frame, text='Hos-Friend', fg= "#7abae6", bg= '#010101', font=('sans rerif',60))
Name.pack(pady=10) 

Iniciar = CTkButton(frame, text='Inicio', command=Crear_ventana, corner_radius=12, fg_color="#010101", border_color="#2cb67d",border_width=1.2, hover_color="#80af86",width=400,
                    height=60, font=('sans rerif',40))
Iniciar.pack(side='bottom', pady=20)

inicio.call('wm','iconphoto',inicio._w,PhotoImage(file='images/LogoPrincipal.png'))
inicio.mainloop()