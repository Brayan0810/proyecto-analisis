"""
Proycecto de Analisis de algoritmos
Main
Autor: Brayan Herney Taimal Cuastumal
"""

"""Imporatar las librerias necesarias"""
from tkinter import Entry, Label, messagebox, Frame, Tk, Button, Toplevel,ttk, Scrollbar, VERTICAL, HORIZONTAL,StringVar,END
from conexion_mysql import*

from nivel3 import*

class Registro(Frame):

    """inicializar ventana, creacion de los frames y conexion base de datos"""
    def __init__(self, master, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
                                    
        self.frame1 = Frame(master)
        self.frame1.grid(columnspan=2, column=0,row=0)
        self.frame2 = Frame(master, bg='gray22')
        self.frame2.grid(column=0, row=1)
        self.frame3 = Frame(master)
        self.frame3.grid(rowspan=2, column=1, row=1)

        self.frame4 = Frame(master, bg='gray20')
        self.frame4.grid(column=0, row=2)

        self.codigo = StringVar()
        self.nombre = StringVar()
        self.pregunta1 = StringVar()
        self.pregunta2 = StringVar()
        self.pregunta3 = StringVar()
        self.buscar = StringVar()

        self.base_datos = Database()
        self.create_wietgs()

    """creacion de los wietgs para la GUI"""
    def create_wietgs(self):
        Label(self.frame1, text = 'R E G I S T R O \t D E \t D A T O S',bg='gray22',fg='white', font=('Orbitron',15,'bold')).grid(column=0, row=0)
        
        """Para ingreso de datos"""
        Label(self.frame2, text = 'Por favor registra tus respuestas',fg='white', bg ='green', font=('Rockwell',12,'bold')).grid(columnspan=2, column=0,row=0, pady=5)
        Label(self.frame2, text = 'Codigo',fg='white', bg ='gray22', font=('Rockwell',13,'bold')).grid(column=0,row=1, pady=15)
        Label(self.frame2, text = 'Nombre',fg='white', bg ='gray22', font=('Rockwell',13,'bold')).grid(column=0,row=2, pady=15)
        Label(self.frame2, text = '¿Que tanto te gustó \n el test?. (0 a 5)',fg='white', bg ='gray22', font=('Rockwell',13,'bold')).grid(column=0,row=3, pady=15)
        Label(self.frame2, text = '¿Lo volverias a jugar?.\n (0 a 5)', fg='white',bg ='gray22', font=('Rockwell',13,'bold')).grid(column=0,row=4, pady=15)
        Label(self.frame2, text = '¿Lo recomendarias?. \n (0 a 5)',fg='white', bg ='gray22', font=('Rockwell',13,'bold')).grid(column=0,row=5, pady=15)

        Entry(self.frame2,textvariable=self.codigo , font=('Arial',12)).grid(column=1,row=1, padx =5)
        Entry(self.frame2,textvariable=self.nombre , font=('Arial',12)).grid(column=1,row=2)
        Entry(self.frame2,textvariable=self.pregunta1 , font=('Arial',12)).grid(column=1,row=3)
        Entry(self.frame2,textvariable=self.pregunta2 , font=('Arial',12)).grid(column=1,row=4)
        Entry(self.frame2,textvariable=self.pregunta3 , font=('Arial',12)).grid(column=1,row=5)
       
        Label(self.frame4, text = 'Control',fg='white', bg ='black', font=('Rockwell',12,'bold')).grid(columnspan=3, column=0,row=0, pady=1, padx=4)         
        Button(self.frame4,command= self.agregar_datos, text='REGISTRAR', font=('Arial',10,'bold'), bg='green2').grid(column=0,row=1, pady=10, padx=4)
        Button(self.frame4,command = self.ventana_promedio, text='Promedio', font=('Arial',10,'bold'), bg='blue').grid(column=1,row=1, padx=10)        
        Button(self.frame4,command = self.eliminar_fila, text='ELIMINAR', font=('Arial',10,'bold'), bg='red').grid(column=2,row=1, padx=4)
        Button(self.frame4,command = self.mostrar_ordenado, text='Ordenar por mayor nivel satisfaccion', font=('Arial',10,'bold'), bg='blue').grid(columnspan=2,column = 1, row=2)
        #Entry(self.frame4,textvariable=self.buscar , font=('Arial',12), width=10).grid(column=0,row=2, pady=1, padx=8)
        Button(self.frame4,command = self.mostrar_todo, text='MOSTRAR DATOS DE MYSQL', font=('Arial',10,'bold'), bg='green').grid(columnspan=3,column=0,row=3, pady=8)

        self.tabla = ttk.Treeview(self.frame3, height=21)
        self.tabla.grid(column=0, row=0)

        ladox = Scrollbar(self.frame3, orient = HORIZONTAL, command= self.tabla.xview)
        ladox.grid(column=0, row = 1, sticky='ew') 
        ladoy = Scrollbar(self.frame3, orient =VERTICAL, command = self.tabla.yview)
        ladoy.grid(column = 1, row = 0, sticky='ns')

        self.tabla.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
       
        """creacion de columnas"""
        self.tabla['columns'] = ('Nombre', 'Pregunta 1', 'Pregunta 2', 'Pregunta 3')

        self.tabla.column('#0', minwidth=100, width=120, anchor='center')
        self.tabla.column('Nombre', minwidth=100, width=130 , anchor='center')
        self.tabla.column('Pregunta 1', minwidth=100, width=120, anchor='center' )
        self.tabla.column('Pregunta 2', minwidth=100, width=120 , anchor='center')
        self.tabla.column('Pregunta 3', minwidth=100, width=105, anchor='center')

        self.tabla.heading('#0', text='Codigo', anchor ='center')
        self.tabla.heading('Nombre', text='Nombre', anchor ='center')
        self.tabla.heading('Pregunta 1', text='Pregunta 1', anchor ='center')
        self.tabla.heading('Pregunta 2', text='Pregunta 2', anchor ='center')
        self.tabla.heading('Pregunta 3', text='Pregunta 3', anchor ='center')


        estilo = ttk.Style(self.frame3)
        estilo.theme_use('alt') #  ('clam', 'alt', 'default', 'classic')
        estilo.configure(".",font= ('Helvetica', 12, 'bold'), foreground='red2')        
        estilo.configure("Treeview", font= ('Helvetica', 10, 'bold'), foreground='black',  background='white')
        estilo.map('Treeview',background=[('selected', 'green2')], foreground=[('selected','black')] )

        self.tabla.bind("<<TreeviewSelect>>", self.obtener_fila)  # seleccionar  fila
        

    """metodo para agregar los datos de usuarios"""
    def agregar_datos(self):
        self.tabla.get_children()
        codigo = self.codigo.get()
        nombre = self.nombre.get()
        modelo = self.pregunta1.get()
        precio = self.pregunta2.get()
        cantidad = self.pregunta3.get()
        datos = (nombre, modelo, precio, cantidad)
        if codigo and nombre and modelo and precio and cantidad !='':        
            self.tabla.insert('',0, text = codigo, values=datos)
            self.base_datos.inserta_usuario(codigo, nombre, modelo, precio, cantidad)


    def limpiar_datos(self):
        self.tabla.delete(*self.tabla.get_children())
        self.codigo.set('')
        self.nombre.set('')
        self.pregunta1.set('')
        self.pregunta2.set('')
        self.pregunta3.set('')
        

    def buscar_nombre(self):
        nombre_producto = self.buscar.get()
        nombre_producto = str("'" + nombre_producto + "'")
        nombre_buscado = self.base_datos.busca_usuario(nombre_producto)
        self.tabla.delete(*self.tabla.get_children())
        i = -1
        for dato in nombre_buscado:
            i= i+1                       
            self.tabla.insert('',i, text = nombre_buscado[i][1:2], values=nombre_buscado[i][2:6])


    def mostrar_todo(self):
        self.tabla.delete(*self.tabla.get_children())
        registro = self.base_datos.mostrar_usuarios()
        i = -1
        for dato in registro:
            i= i+1                       
            self.tabla.insert('',i, text = registro[i][1:2], values=registro[i][2:6])
    
    def mostrar_ordenado(self):
        self.tabla.delete(*self.tabla.get_children())
        registro = self.base_datos.mostrar_total_ordenado()
        i = -1
        for dato in registro:
            i= i+1                       
            self.tabla.insert('',i, text = registro[i][1:2], values=registro[i][2:6])

    """Elminar usuario"""
    def eliminar_fila(self):
        fila = self.tabla.selection()
        if len(fila) !=0:        
            self.tabla.delete(fila)
            nombre = ("'"+ str(self.nombre_borar) + "'")       
            self.base_datos.elimina_usuario(nombre)


    """obtener fila del usuario"""
    def obtener_fila(self, event):
        current_item = self.tabla.focus()
        if not current_item:
            return
        data = self.tabla.item(current_item)
        self.nombre_borar = data['values'][0]    
   
    """Ventana que presenta los promedios de las 3 preguntas"""
    def ventana_promedio(self):

        promedio1 = self.base_datos.calcular_promedio1()
        promedio2 = self.base_datos.calcular_promedio2()
        promedio3 = self.base_datos.calcular_promedio3()
        messagebox.showinfo(title= "Promedio", message = f"promedio de la pregunta 1 es: {promedio1} \npromedio de la pregunta 2 es: {promedio2} \npromedio de la pregunta 3 es: {promedio3} ")
        

def main():
    ventana = Tk()
    ventana.wm_title("Registro de Datos en MySQL")
    ventana.config(bg='gray22')
    ventana.geometry('1000x550')
    #ventana.resizable(0,0)
    app = Registro(ventana)
    app.mainloop()

if __name__=="__main__":
    main()