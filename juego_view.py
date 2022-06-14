"""
Proycecto de Analisis de algoritmos
Vista del juego buscaManzas
Autor: Brayan Herney Taimal Cuastumal
"""

from tkinter import  Tk, Frame, Canvas, Button,Label, ALL

x, y =40,40
direction = ''
posicion_food = (15,15)
posicion_pared=(40,200)
posicion_pared2=(280,40)
posicion_pared3=(280,280)
posicion_pared4=(360,280)
posicion_snake = [(40,40)]
nueva_posicion =[(15,15)]
a = '->'

"""Metodo para definir las coordenadas del recorrido (arriba, abajo, izquierda, derecha"""
def coordenadas_snake():
    global direccion, posicion_snake,x,y ,nueva_posicion,a 

    if direction =='up': # arriba
        y =  y-80
        nueva_posicion[0:] = [(x, y)]
        a='^'
        if y >=520:
            y=520
        elif y <=0:
            y=520
    elif direction =='down':  # abajo
        y = y+80 
        nueva_posicion[0:] = [(x, y)]
        a='v'
        if y >=480:
            y=-40
        elif y<=0:
            y=-40   
    elif direction == 'left': # izquierda
        x = x-80
        nueva_posicion[0:] = [(x, y)]
        a='<-'
        if x >=560:
            x = 520
        elif x <=0:
            x=520
        
    elif direction == 'right':  # derecha
        x = x + 80
        nueva_posicion[0:] = [(x, y)]
        a='->'
        if x >=480:
            x=-40
        elif x <=0:
            x=-40

    posicion_snake = nueva_posicion + posicion_snake[:-1]

    for parte, lugar in zip(canvas.find_withtag("snake"), posicion_snake):
        canvas.coords(parte, lugar)


"""Metodo para determinar y validar las direcciones"""
def direccion(event):
    global direction

    if event == 'left':
        if direction != 'right':
            direction = event
    elif event == 'right':
        if direction != 'left':
            direction = event
    elif event == 'up':
        if direction != 'down':
            direction = event
    elif event == 'down':
        if direction != 'up':
            direction = event


"""Metodo para dar inicio al juego"""
def movimiento():
    global posicion_food, posicion_snake,nueva_posicion

    coordenadas_snake()

    if posicion_snake[0] == posicion_pared or posicion_snake[0] == posicion_pared2 or posicion_snake[0] == posicion_pared3 or posicion_snake[0] == posicion_pared4:
        cruzar_snake()

    if posicion_food == posicion_snake[0]:
        n = len(posicion_snake)

        cantidad['text'] = 'Cantidad 🍎 : {}'.format(n)

        #posicion_food = (random.choice(posiciones), random.choice(posiciones))
        posicion_food = (440,440)
        posicion_snake.append(posicion_snake[-1])

    
        if posicion_food not in posicion_snake:
            canvas.coords(canvas.find_withtag("food"), posicion_food)

        canvas.create_text(*posicion_snake[-1], text='O' , fill='green2', 
            font = ('Arial',30), tag ='snake')

    
        if posicion_snake[-1] == nueva_posicion[0] and len(posicion_snake)>=4: 
            cruzar_snake()


        for i in posicion_snake:
            if len(posicion_snake)==3:
                maximo_nivel()
        
    cantidad.after(500,movimiento)

def cruzar_snake():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, 
        text=f"VUELVE A INTENTARLO,\n pero antes responde \n el cuestionario \n\n 🍎",fill='red',
        font=('Arial',20,'bold'))

"""Metodo para determinar si el usuario llego a su meta"""
def maximo_nivel():
    canvas.delete(ALL)
    canvas.create_text(canvas.winfo_width() / 2, canvas.winfo_height() / 2, 
        text=f"EXELENTE\n\n Ahora ve a responder \n el cuestionario \n\n 🍎🍎🍎",fill='green2',
        font=('Arial',25,'bold'))
         
    
"""Metodo para salir de la vista de juego e ir al cuestionario"""
def irCuestionario ():
    ventana.destroy()
    ventana.quit()

"""Se iniciliza la vista"""
ventana = Tk()
ventana.config(bg='black')
ventana.title('Juego busca Manzana')
ventana.geometry('485x510')
ventana.resizable(0,0)

"""Se inicializa los Frames"""
frame_1 = Frame(ventana, width=485, height=25, bg='black')
frame_1.grid(column=0, row=0)
frame_2 = Frame(ventana, width=485, height=490, bg='black')
frame_2.grid(column=0, row=1)

"""Se determinan las direcciones segun el usuario indique"""
ventana.bind("<KeyPress-Up>", lambda event:direccion('up'))
ventana.bind("<KeyPress-Down>", lambda event:direccion('down'))
ventana.bind("<KeyPress-Left>", lambda event:direccion('left'))
ventana.bind("<KeyPress-Right>",  lambda event:direccion('right'))


"""Se forma una matriz de 6x6"""
canvas = Canvas(frame_2, bg='black', width=550, height=550)
canvas.pack()

for i in range(0,480,80):
    for j in range(0,480,80):
        canvas.create_rectangle(i,j,i+80, j+80,fill='gray10', outline='blue')


canvas.create_text(440,440, text='🍎', fill='red2',
 font = ('Arial',30), tag = 'food')

canvas.create_text(40,200, text='🟨', fill='white',
 font = ('Arial',50), tag = 'food')

canvas.create_text(280,40, text='🟨', fill='white',
 font = ('Arial',50), tag = 'food')

canvas.create_text(280,280, text='🟨', fill='white',
 font = ('Arial',50), tag = 'food')

canvas.create_text(360,280, text='🟨', fill='white',
 font = ('Arial',50), tag = 'food')

button1 = Button(frame_1, text='Ir al cuestionario', bg='orange' ,
    command = irCuestionario)
button1.grid(row=0, column=0, padx=20)

button2 = Button(frame_1, text='Iniciar', bg='aqua', 
    command = movimiento)
button2.grid(row=0, column=1, padx=20)

cantidad =Label(frame_1, text='Cantidad 🍎 :', bg='black', 
    fg = 'white', font=('Arial',12, 'bold'))
cantidad.grid(row=0, column=2, padx=20)

ventana.mainloop()