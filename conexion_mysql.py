"""
Proycecto de Analisis de algoritmos
Conexion con MySQL
Autor: Brayan Herney Taimal Cuastumal
"""

import pymysql


class Database:

    """Conexion con la base de datos MySQL"""
    def __init__(self):
        self.conexion = pymysql.connect(
            host='localhost',
            user='root',
            password='root12345',
            db='proyecto_analisis'
        )
        self.cursor = self.conexion.cursor()
        

    """Metodo para agregra los datos de usuarios"""
    def inserta_producto(self,codigo, nombre, modelo, precio, cantidad):
        cur = self.conexion.cursor()
        sql='''INSERT INTO usuario (CODIGO, NOMBRE, PREGUNTA1, PREGUNTA2, PREGUNTA3) 
        VALUES('{}', '{}','{}', '{}','{}')'''.format(codigo, nombre, modelo, precio, cantidad)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()

    """Metodo para mostrar los datos de los usuarios"""
    def mostrar_productos(self):
        cursor = self.conexion.cursor()
        sql = "SELECT * FROM usuario " 
        cursor.execute(sql)
        registro = cursor.fetchall()
        return registro

    
    def busca_producto(self, nombre_producto):
        cur = self.conexion.cursor()
        sql = "SELECT * FROM usuario WHERE NOMBRE = {}".format(nombre_producto)
        cur.execute(sql)
        nombreX = cur.fetchall()
        cur.close()     
        return nombreX 


    def elimina_productos(self,nombre):
        cur = self.conexion.cursor()
        sql='''DELETE FROM usuario WHERE NOMBRE = {}'''.format(nombre)
        cur.execute(sql)
        self.conexion.commit()    
        cur.close()

    def calcular_promedio1(self):
        cursor = self.conexion.cursor()
        sql = "select AVG(pregunta1) as promedio_pregunta1 from usuario" 
        cursor.execute(sql)
        promedio = cursor.fetchall()
        return promedio

    def calcular_promedio2(self):
        cursor = self.conexion.cursor()
        sql = "select AVG(pregunta2) as promedio_pregunta2 from usuario" 
        cursor.execute(sql)
        promedio = cursor.fetchall()
        return promedio

    def calcular_promedio3(self):
        cursor = self.conexion.cursor()
        sql = "select AVG(pregunta3) as promedio_pregunta3 from usuario" 
        cursor.execute(sql)
        promedio = cursor.fetchall()
        return promedio
