import sqlite3
import re
from tkinter.messagebox import *
from dec import timestamp_submit
from dec import timestamp_delete
from dec import timestamp_modify


class Base:
    def __init__(self, ):
        try:
            con = sqlite3.connect("db.db")
            cursor = con.cursor()
            cursor.execute(
                """CREATE TABLE IF NOT EXISTS cars
                (id INTEGER PRIMARY KEY AUTOINCREMENT, 
                make varchar(10) NOT NULL,
                model varchar(10) NOT NULL,
                year varint(4),
                plate varchar(7) NOT NULL
                )"""
            )
            con.commit()
        except:
            print("Connection Error")

    def conexion(
            self,
    ):
        con = sqlite3.connect("db.db")
        return con

    def update_treeview(self, mytrvw):
        records = mytrvw.get_children()
        for element in records:
            mytrvw.delete(element)

        sql = "SELECT * FROM cars ORDER BY id ASC"
        con = self.conexion()
        cursor = con.cursor()
        datainf = cursor.execute(sql)

        resultado = datainf.fetchall()
        for fila in resultado:
            print(fila)
            mytrvw.insert("", 0, text=fila[0], values=(
                fila[1], fila[2], fila[3], fila[4]))

    def close_connection(
            self,
    ):
        print("connection closed")

    @timestamp_submit
    def submit(self, make, model, year, plate, mytrvw):
        cadena = make
        patron = "^[A-Za-záéíóú0-9]*$"
        if re.match(patron, cadena):
            con = self.conexion()
            print(make, model, year, plate)
            cursor = con.cursor()
            data = (make, model, year, plate)
            sql = "INSERT INTO cars(make, model, year, plate) VALUES(?, ?, ?, ?)"
            cursor.execute(sql, data)
            con.commit()
            print("Vehicle submitted properly!")
            self.update_treeview(mytrvw)
        else:
            showerror("Error", "The format is incorrect")

    @timestamp_modify
    def modify(self, make, model, year, plate, mytrvw):
        cadena = make
        patron = "^[A-Za-záéíóú0-9]*$"
        if re.match(patron, cadena):
            valor = mytrvw.selection()
            item = mytrvw.item(valor)
            mi_id = item['text']
            con = self.conexion()
            cursor = con.cursor()
            datainf = (make, model, year, plate, mi_id)
            print(datainf)
            sql = "UPDATE cars SET(make, model, year, plate)=(?,?,?,?) WHERE id=?"
            cursor.execute(sql, datainf)
            con.commit()
            print(sql, datainf)
            self.update_treeview(mytrvw)
        else:
            showerror("Error", "There is an error in the format")

    @timestamp_delete
    def delete(self, mytrvw):
        valor = mytrvw.selection()
        item = mytrvw.item(valor)
        mi_id = item['text']
        con = self.conexion()
        cursor = con.cursor()
        data = (mi_id,)
        sql = "DELETE FROM cars WHERE id = ?;"
        cursor.execute(sql, data)
        con.commit()
        self.update_treeview(mytrvw)
