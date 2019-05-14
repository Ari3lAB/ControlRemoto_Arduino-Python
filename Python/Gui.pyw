from tkinter import *
from tkinter import messagebox
import Conexion

def enviaDato():
    messagebox.showinfo('Envío de información', 'Enviaste algo')
    grados.config(text=Conexion.envia()+'°')
    

def recibirDato():
    messagebox.showinfo('Recepción de información', 'Recibiste algo')
    grados.config(text=Conexion.recibe()+'°')    
    

root = Tk()

# Configuración de ventana
root.resizable(False,False)
root.config(width=1024, height=768)
root.title("Control de clima")
root.config(bg="grey")

root.iconbitmap('C:/Users/Ariel AB/Documents/ProyectoEmpotrados/Imgs/fan.ico')

# Centra la ventana creada
windowWidth = root.winfo_reqwidth()
windowHeight = root.winfo_reqheight()
print("Width",windowWidth,"Height",windowHeight)
positionRight = int(root.winfo_screenwidth()/2 - windowWidth/2)
positionDown = int(root.winfo_screenheight()/2 - windowHeight/2)
root.geometry("+{}+{}".format(positionRight, positionDown))

#Set frame de opciones
opciones= Frame(root)
opciones.config(width=300, height=300)
opciones.grid(column=0, row = 0)

#Set label de opciones
lbl = Label(opciones, text="Selecciona la opcion:")
lbl.pack()

#Set boton de recepción
recibe = Button(opciones, text="Recibir Info", command=recibirDato)
recibe.pack()

#Set boton de envío
enviar = Button(opciones, text="Enviar info", command=enviaDato)
enviar.pack()

#Set frame de temperatura
temperatura = Frame(root)
temperatura.config(width=300, height=300)
temperatura.grid(column=1, row = 0)


#Set label de opciones
tempAcual = Label(temperatura, text="Temperatura actual:")
tempAcual.pack()
#Set label de grados
grados = Label(temperatura, text="0°", font =("Tahoma", 50))
grados.pack()


root.mainloop()