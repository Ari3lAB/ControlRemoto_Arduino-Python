from tkinter import *
from tkinter import messagebox
import Conexion
import tkinter.ttk as ttk
import datetime
import threading
import time
import Database


root = Tk()
maxTemp = 25
autoStatus = "OFF"
temp = 0


win = Toplevel(root)
win.title("Config")
l = Label(win, text="Temperatura máxima:")
l.grid(row=0, column=0)
i = Entry(win, bd=2)
i.grid(row=0, column=1)


def setMaxTemp():
    global maxTemp
    maxTemp = i.get()
    lbl_maxTemp.config(text="Temp. máxima:" + str(maxTemp)+"°")
    win.withdraw()


b = Button(win, text="Okay", command=setMaxTemp)
b.grid(row=1, column=0)
win.withdraw()


# Salir del programa
def exit():
    if messagebox.askokcancel("Salir", "Salir de la aplicación?"):
        root.destroy()

# Controla el estado del Abanico (ON/OFF)


def controLed():
    ledStat = Conexion.setLed()
    abanico.config(text=ledStat)


# Revisa el estado del led (Sin modificarlo)
def statusLed():
    ledStat = Conexion.checkLed()


def configTemp():
    win.wm_deiconify()


# Configura la pantalla principal
root.iconbitmap('fan.ico')
root.geometry("589x457+508+214")
root.resizable(False, False)
root.title("Control de temperatura")
root.configure(background="#3f51b5")
root.configure(highlightbackground="#f0f0f0")
root.configure(highlightcolor="#5c6bc0")


# Labels hora
lbl_Hora = Label(root)
lbl_Hora.place(relx=0.017, rely=0.022, height=21, width=54)
lbl_Hora.configure(activebackground="#f9f9f9")
lbl_Hora.configure(activeforeground="black")
lbl_Hora.configure(background="#3f51b5")
lbl_Hora.configure(disabledforeground="#a3a3a3")
lbl_Hora.configure(font="-family {Consolas} -size 14")
lbl_Hora.configure(foreground="#ffffff")
lbl_Hora.configure(highlightbackground="#d9d9d9")
lbl_Hora.configure(highlightcolor="black")
lbl_Hora.configure(text="Hora:")
lbl_Hora.configure(width=54)

hora = Label(root)
hora.place(relx=0.0, rely=0.066, height=61, width=294)
hora.configure(activebackground="#f9f9f9")
hora.configure(activeforeground="black")
hora.configure(background="#3f51b5")
hora.configure(disabledforeground="#a3a3a3")
hora.configure(font="-family {Consolas} -size 48")
hora.configure(foreground="#ffffff")
hora.configure(highlightbackground="#d9d9d9")
hora.configure(highlightcolor="black")
hora.configure(text="00:00:00")
hora.configure(width=294)


# Labels temperatura
lbl_temperatura = Label(root)
lbl_temperatura.place(relx=0.017, rely=0.241, height=21, width=214)
lbl_temperatura.configure(activebackground="#f9f9f9")
lbl_temperatura.configure(activeforeground="black")
lbl_temperatura.configure(background="#3f51b5")
lbl_temperatura.configure(disabledforeground="#a3a3a3")
lbl_temperatura.configure(font="-family {Consolas} -size 14")
lbl_temperatura.configure(foreground="#ffffff")
lbl_temperatura.configure(highlightbackground="#d9d9d9")
lbl_temperatura.configure(highlightcolor="black")
lbl_temperatura.configure(text="Temperatura ambiente:")
lbl_temperatura.configure(width=214)

temperatura = Label(root)
temperatura.place(relx=0.017, rely=0.306, height=61, width=144)
temperatura.configure(background="#3f51b5")
temperatura.configure(disabledforeground="#a3a3a3")
temperatura.configure(font="-family {Consolas} -size 48")
temperatura.configure(foreground="#ffffff")
temperatura.configure(text="0°")
temperatura.configure(width=144)


# Labels humedad
lbl_humedad = Label(root)
lbl_humedad.place(relx=0.017, rely=0.503, height=21, width=184)
lbl_humedad.configure(activebackground="#f9f9f9")
lbl_humedad.configure(activeforeground="black")
lbl_humedad.configure(background="#3f51b5")
lbl_humedad.configure(disabledforeground="#a3a3a3")
lbl_humedad.configure(font="-family {Consolas} -size 14")
lbl_humedad.configure(foreground="#ffffff")
lbl_humedad.configure(highlightbackground="#d9d9d9")
lbl_humedad.configure(highlightcolor="black")
lbl_humedad.configure(text="índice de humedad:")
lbl_humedad.configure(width=184)

humedad = Label(root)
humedad.place(relx=0.017, rely=0.569, height=61, width=144)
humedad.configure(activebackground="#f9f9f9")
humedad.configure(activeforeground="black")
humedad.configure(background="#3f51b5")
humedad.configure(disabledforeground="#a3a3a3")
humedad.configure(font="-family {Consolas} -size 48")
humedad.configure(foreground="#ffffff")
humedad.configure(highlightbackground="#d9d9d9")
humedad.configure(highlightcolor="black")
humedad.configure(text="0%")


# Labels abanico
lbl_abanico = Label(root)
lbl_abanico.place(relx=0.017, rely=0.766, height=21, width=194)
lbl_abanico.configure(activebackground="#f9f9f9")
lbl_abanico.configure(activeforeground="black")
lbl_abanico.configure(background="#3f51b5")
lbl_abanico.configure(disabledforeground="#a3a3a3")
lbl_abanico.configure(font="-family {Consolas} -size 14")
lbl_abanico.configure(foreground="#ffffff")
lbl_abanico.configure(highlightbackground="#d9d9d9")
lbl_abanico.configure(highlightcolor="black")
lbl_abanico.configure(text="Estado del abanico:")
lbl_abanico.configure(width=194)

abanico = Label(root)
abanico.place(relx=0.017, rely=0.832, height=61, width=144)
abanico.configure(activebackground="#f9f9f9")
abanico.configure(activeforeground="black")
abanico.configure(background="#3f51b5")
abanico.configure(disabledforeground="#a3a3a3")
abanico.configure(font="-family {Consolas} -size 48")
abanico.configure(foreground="#ffffff")
abanico.configure(highlightbackground="#d9d9d9")
abanico.configure(highlightcolor="black")
abanico.configure(text="OFF")


# Separadores
TSeparator1 = ttk.Separator(root)
TSeparator1.place(relx=0.017, rely=0.46, relwidth=0.34)

TSeparator1_4 = ttk.Separator(root)
TSeparator1_4.place(relx=0.017, rely=0.219, relwidth=0.34)

TSeparator1_5 = ttk.Separator(root)
TSeparator1_5.place(relx=0.017, rely=0.722, relwidth=0.34)


# Botones
controlAbanico = Button(root)
controlAbanico.place(relx=0.747, rely=0.022, height=94, width=117)
controlAbanico.configure(activebackground="#757de8")
controlAbanico.configure(activeforeground="#ffffff")
controlAbanico.configure(background="#002984")
controlAbanico.configure(cursor="hand2")
controlAbanico.configure(disabledforeground="#a3a3a3")
controlAbanico.configure(font="-family {Consolas} -size 24")
controlAbanico.configure(foreground="#ffffff")
controlAbanico.configure(highlightbackground="#d9d9d9")
controlAbanico.configure(highlightcolor="#757de8")
controlAbanico.configure(overrelief="flat")
controlAbanico.configure(pady="0")
controlAbanico.configure(relief="flat")
controlAbanico.configure(text="ON/OFF")
controlAbanico.configure(width=117)
controlAbanico.config(command=controLed)

lbl_AutoStatus = Label(root)
lbl_AutoStatus.place(relx=0.39, rely=0.372, height=21, width=144)
lbl_AutoStatus.configure(activebackground="#f9f9f9")
lbl_AutoStatus.configure(activeforeground="black")
lbl_AutoStatus.configure(background="#3f51b5")
lbl_AutoStatus.configure(disabledforeground="#a3a3a3")
lbl_AutoStatus.configure(font="-family {Consolas} -size 12")
lbl_AutoStatus.configure(foreground="#ffffff")
lbl_AutoStatus.configure(highlightbackground="#d9d9d9")
lbl_AutoStatus.configure(highlightcolor="black")
lbl_AutoStatus.configure(text="Auto: OFF")


def autoControl():
    global autoStatus
    if (autoStatus == "OFF"):
        autoStatus = "ON"
        lbl_AutoStatus.config(text="Arduino: ON")
        controlAbanico.config(state="disabled")
    else:
        autoStatus = "OFF"
        lbl_AutoStatus.config(text="Arduino: OFF")
        controlAbanico.config(state="normal")


auto = Button(root)
auto.place(relx=0.747, rely=0.241, height=44, width=117)
auto.configure(activebackground="#757de8")
auto.configure(activeforeground="#ffffff")
auto.configure(background="#002984")
auto.configure(cursor="hand2")
auto.configure(disabledforeground="#a3a3a3")
auto.configure(font="-family {Consolas} -size 24")
auto.configure(foreground="#ffffff")
auto.configure(highlightbackground="#d9d9d9")
auto.configure(highlightcolor="#757de8")
auto.configure(overrelief="flat")
auto.configure(pady="0")
auto.configure(relief="flat")
auto.configure(text="Auto")
auto.config(command=autoControl)

config = Button(root)
config.place(relx=0.747, rely=0.46, height=94, width=117)
config.configure(activebackground="#757de8")
config.configure(activeforeground="#ffffff")
config.configure(background="#002984")
config.configure(cursor="hand2")
config.configure(disabledforeground="#a3a3a3")
config.configure(font="-family {Consolas} -size 24")
config.configure(foreground="#ffffff")
config.configure(highlightbackground="#d9d9d9")
config.configure(highlightcolor="#757de8")
config.configure(overrelief="flat")
config.configure(pady="0")
config.configure(relief="flat")
config.configure(text="CONFIG", command=configTemp)

salir = Button(root)
salir.place(relx=0.747, rely=0.722, height=94, width=117)
salir.configure(activebackground="#757de8")
salir.configure(activeforeground="#ffffff")
salir.configure(background="#757de8")
salir.configure(cursor="hand2")
salir.configure(disabledforeground="#a3a3a3")
salir.configure(font="-family {Consolas} -size 24")
salir.configure(foreground="#ffffff")
salir.configure(highlightbackground="#d9d9d9")
salir.configure(highlightcolor="#757de8")
salir.configure(overrelief="flat")
salir.configure(pady="0")
salir.configure(relief="flat")
salir.configure(text="Salir", command=exit)


# Temperaturas minima/máxima
lbl_maxTemp = Label(root)
lbl_maxTemp.place(relx=0.39, rely=0.306, height=21, width=144)
lbl_maxTemp.configure(activebackground="#f9f9f9")
lbl_maxTemp.configure(activeforeground="black")
lbl_maxTemp.configure(background="#3f51b5")
lbl_maxTemp.configure(disabledforeground="#a3a3a3")
lbl_maxTemp.configure(font="-family {Consolas} -size 12")
lbl_maxTemp.configure(foreground="#ffffff")
lbl_maxTemp.configure(highlightbackground="#d9d9d9")
lbl_maxTemp.configure(highlightcolor="black")
lbl_maxTemp.configure(text="Temp. máxima:" + str(maxTemp)+"°")
lbl_maxTemp.configure(width=144)


# Actualiza hora
def clock():
    while(True):
        reloj = datetime.datetime.now().strftime("%H:%M:%S")
        hora.configure(text=reloj)
        time.sleep(.5)

# Obtiene la temperatura


def getTemp():
    global temp
    temp = Conexion.temp()
    temperatura.config(text=temp+"°")
    return temp

# Obtiene la humedad


def getHumid():
    humid = Conexion.humid()
    humedad.config(text=humid+"%")
    return humid

# Actualiza los valores de la interfaz


def updateGUI():
    reloj = datetime.datetime.now().strftime("%H:%M:%S")
    temp = str(getTemp())
    time.sleep(.5)
    humid = str(getHumid())

    Database.intsertData(reloj, temp, humid)
    root.after(200000, updateGUI)


def handleAuto():
    global autoStatus, maxTemp ,temp
    if(autoStatus == "ON"):
        if (temp > maxTemp):
                controLed()

    root.after(20000,handleAuto)



updateGUI()
handleAuto()
threading.Thread(target=clock).start()
root.mainloop()
