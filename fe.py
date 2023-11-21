from tkinter import *
from tkinter import ttk
from backend import *


class Vista:
    def __init__(self, master):
        self.obj_base = Base()
        self.master = master
        self.master.title("Katarina System")
        self.master.configure(background='white')
        self.master.geometry("900x500")
        self.buttons()
        self.fos()
        self.column(master)

    def fos(self):
        self.v_make = StringVar()
        self.v_model = StringVar()
        self.v_year = IntVar()
        self.v_plate = StringVar()

        self.make = Label(self.master, text="Make", background="light blue")
        self.make.grid(row=0, column=0, sticky=W)

        self.model = Label(self.master, text="Model", background="light blue")
        self.model.grid(row=1, column=0, sticky=W)

        self.year = Label(self.master, text="Year", background="light blue")
        self.year.grid(row=0, column=2, sticky=W)

        self.plate = Label(self.master, text="Plate", background="light blue")
        self.plate.grid(row=1, column=2, sticky=W)

        self.entry_make = Entry(
            self.master, textvariable=self.v_make, width=20)
        self.entry_make.grid(row=0, column=1, sticky=W, padx=10, pady=5)

        self.entry_model = Entry(
            self.master, textvariable=self.v_model, width=20)
        self.entry_model.grid(row=1, column=1, sticky=W, padx=10, pady=5)

        self.entry_year = Entry(
            self.master, textvariable=self.v_year, width=20)
        self.entry_year.grid(row=0, column=3, sticky=W, padx=10, pady=5)

        self.entry_plate = Entry(
            self.master, textvariable=self.v_plate, width=20)
        self.entry_plate.grid(row=1, column=3, sticky=W, padx=10, pady=5)

    def column(self, master):

        self.tree = ttk.Treeview(master)
        self.tree["columns"] = ("Make", "Model", "Year", "Plate")
        self.tree.column("#0", width=90, minwidth=50, anchor=W)
        self.tree.column("Make", width=140, minwidth=90)
        self.tree.column("Model", width=140, minwidth=90)
        self.tree.column("Year", width=140, minwidth=90)
        self.tree.column("Plate", width=140, minwidth=90)
        self.tree.heading("#0", text="ID")
        self.tree.heading("Make", text="MODEL")
        self.tree.heading("Model", text="MAKE")
        self.tree.heading("Year", text="YEAR")
        self.tree.heading("Plate", text="PLATE")
        self.tree.grid(row=10, column=0, columnspan=5)

    def buttons(self):

        self.button_submit = Button(
            self.master,
            text="Submit",
            background="grey",
            foreground="white",
            width=10,
            font=5,
            command=lambda: self.submit())
        self.button_submit.grid(row=7, column=20)

        self.button_modify = Button(
            self.master,
            text="Update",
            background="grey",
            foreground="white",
            width=10,
            font=5,
            command=lambda: self.modify())
        self.button_modify.grid(row=8, column=20)

        self.button_delete = Button(
            self.master,
            text="Delete",
            background="grey",
            foreground="white",
            width=10,
            font=5,
            command=lambda: self.delete())
        self.button_delete.grid(row=9, column=20)

    def submit(
        self,
    ):
        self.obj_base.submit(self.v_model.get(),
                             self.v_make.get(), self.v_year.get(), self.v_plate.get(), self.tree)
    def delete(
        self,
    ):
        self.obj_base.delete(self.tree)

    def modify(
            self,
    ):
        self.obj_base.modify(self.v_model.get(
        ), self.v_make.get(), self.v_year.get(), self.v_plate.get(), self.tree)

    def update(
        self,
    ):
        self.obj_base.update_treeview(self.tree)
