import tkinter
import customtkinter , os
from PIL import Image
from PIL import ImageOps
from PIL import ImageDraw
import threading
import time

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")

app = customtkinter.CTk()
app.attributes("-fullscreen", True)
Width = app.winfo_screenwidth()
Height= app.winfo_screenheight()
bienvenido = customtkinter.CTkLabel(app,text="Bienvenido a SERMA", font=("Helvetica",80))
botonIniciar = customtkinter.CTkButton(master = app, text="Iniciar")
stringBuscador = ""
buscador = customtkinter.CTkEntry(app,corner_radius=50,textvariable=stringBuscador, width=200 )
contador = 1 + 0

#def entras():
#    botonIniciar.place_forget()
#    huellaCargalabel.place_forget()
#    if(contador == 2):
#        alerta = customtkinter.CTkToplevel()
#
#        boto = customtkinter.CTkButton(master = alerta, text="Error en la huella",
#                                                command= lambda: alerta.wm_forget)
#        boto.pack(pady=10)
#    else:
#        inicioProgreso()
            
    
#t = threading.Timer(3, entras)


#def validacion():
#     if contra.get()== "1234":
#          Bienvenido()

#def Bienvenido():
#    print("si")
#    inicio.place_forget()
#    contraseña.place_forget()
#    Contraseñalabel.place_forget()
#    button.place_forget()
#    logolabel.place_forget()
#    bienvenido.place(relx=0.38, rely=0.4)
#    f = threading.Timer(3, escritorio)
#    f.start()    


#def inicioProgreso():
#    global contador
#    contador = contador + 1
#    t = threading.Timer(3, entras)
#    huellaCargalabel.place(relx=0.45, y=550)
#    t.start()

iniciarEst = customtkinter.CTkLabel(app,text="Inicio de sesión\nusuario", font=("Helvetica",38), fg_color='transparent')
iniciarEst.place(relx=0.06, y=150)

iniciarDoc = customtkinter.CTkLabel(app,text="Inicio de sesión\ndocente", font=("Helvetica",38), fg_color='transparent')
iniciarDoc.place(relx=0.76, y=150)

user = customtkinter.StringVar(app)
#contra = customtkinter.StringVar(app)


Contraseñalabel = customtkinter.CTkLabel(app, text="Contraseña", font=("Helvetica",24) )
#Contraseñalabel.place(relx=0.4, y=550)


#contraseña = customtkinter.CTkEntry(app, placeholder_text="Ingresa tu contraseña",corner_radius=50,show="*",textvariable=contra )
#contraseña.place(relx=0.5, y=550)

#def creartexto():
#    button.place_forget()
#    buttondoc.place_forget()
#    labelSERMA.place_forget()
#    file=open('escrito.txt','a+')
#    file.write("Lorem ipsum it ns")
#    file.seek(0)
#    #print(file.read(100))
#    #Si no hago file read, se limpia
#    file.truncate()
#    file.close()

#def leertexto():
#    f=open('escrito.txt','r')
#    escrit=f.read(100)
#    print(escrit.find('#'))
#    f.close()
    
def estudianteEntrar():
    print("uy")

def docenteEntrar():
    print("uy")

BotonEst = customtkinter.CTkButton(master = app, text="Ingresar", command=estudianteEntrar)
BotonEst.place(relx=0.1, y=600)

BotonDoc = customtkinter.CTkButton(master = app, text="Ingresar", command=docenteEntrar)
BotonDoc.place(relx=0.8, y=600)
ImgSERMA = customtkinter.CTkImage(light_image=Image.open("image\\SERMA.png"),size=(300,300))
labelSERMA = customtkinter.CTkLabel(app, text="" , image=ImgSERMA, height=30, width=30)
labelSERMA.place(relx=0.38, y=150)

#def escritorio():
#    bienvenido.place_forget()
#    ImageUser = customtkinter.CTkImage(light_image=Image.open("image\\Mado.png"),size=(300,300))
#    logolabel = customtkinter.CTkLabel(app, text="" , image=ImageUser, height=30, width=30)
#    logolabel.place(relx=0.38, y=150)
#    buscador.place(relx=0.4, y=500)
#    ImageHuella = customtkinter.CTkImage(light_image=Image.open("image\\lupa.png"),size=(50,50))
#    huellabutton = customtkinter.CTkButton(app, text="" , image=ImageHuella, height=30, width=3,fg_color='transparent' )
#    huellabutton.place(relx=0.55, y=480)




app.mainloop()