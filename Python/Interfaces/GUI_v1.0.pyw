try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True




def vp_start_gui():    
    global val, w, root
    root = tk.Tk()
    root = Root (root)    
    root.mainloop()

w = None
def create_Root(root, *args, **kwargs):    
    global w, w_win, rt
    rt = root
    w = tk.rootlevel (root)
    root = Root (w)    
    return (w, root)

def destroy_Root():
    global w
    w.destroy()
    w = None

class Root:
    def __init__(self, root=None):
        #Config rootlevel
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()        
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        root.geometry("589x457+508+214")
        root.title("Control de temperatura")
        root.configure(background="#3f51b5")
        root.configure(highlightbackground="#f0f0f0")
        root.configure(highlightcolor="#5c6bc0")

        


        self.lbl_maxTemp = tk.Label(root)
        self.lbl_maxTemp.place(relx=0.39, rely=0.306, height=21, width=144)
        self.lbl_maxTemp.configure(activebackground="#f9f9f9")
        self.lbl_maxTemp.configure(activeforeground="black")
        self.lbl_maxTemp.configure(background="#3f51b5")
        self.lbl_maxTemp.configure(disabledforeground="#a3a3a3")
        self.lbl_maxTemp.configure(font="-family {Consolas} -size 12")
        self.lbl_maxTemp.configure(foreground="#ffffff")
        self.lbl_maxTemp.configure(highlightbackground="#d9d9d9")
        self.lbl_maxTemp.configure(highlightcolor="black")
        self.lbl_maxTemp.configure(text="Temp. máxima: 0°")
        self.lbl_maxTemp.configure(width=144)

        self.lbl_minTemp = tk.Label(root)
        self.lbl_minTemp.place(relx=0.39, rely=0.372, height=21, width=144)
        self.lbl_minTemp.configure(activebackground="#f9f9f9")
        self.lbl_minTemp.configure(activeforeground="black")
        self.lbl_minTemp.configure(background="#3f51b5")
        self.lbl_minTemp.configure(disabledforeground="#a3a3a3")
        self.lbl_minTemp.configure(font="-family {Consolas} -size 12")
        self.lbl_minTemp.configure(foreground="#ffffff")
        self.lbl_minTemp.configure(highlightbackground="#d9d9d9")
        self.lbl_minTemp.configure(highlightcolor="black")
        self.lbl_minTemp.configure(text="Temp. mínima: 0°")
    
    


def clock():
        time = datetime.datetime.now().strftime("%H:%M:%S")
        Root.Hora.configure(text=time)
        #lab['text'] = time
        Root.after(1000, clock) # run itself again after 1000 ms        
clock()
# run first time

if __name__ == '__main__':
    vp_start_gui()





