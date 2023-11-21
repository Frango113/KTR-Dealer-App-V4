from tkinter import Tk
import fe


class Controlador:
    def __init__(self, master):
        self.master_controlador = master
        self.obj_vista = fe.Vista(self.master_controlador)


if __name__ == "__main__":
    master = Tk()
    app = Controlador(master)
    try:
        app.obj_vista.update()
    except:
        print("Error: N/A")
    master.mainloop()
