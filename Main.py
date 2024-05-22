import tkinter
import customtkinter , os
from PIL import Image
from PIL import ImageOps
from PIL import ImageDraw
import threading
import time

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")
itipo=0
#IMPORTANTE, itipo define si es docente o estudiante
app = customtkinter.CTk()
app.attributes("-fullscreen", True)
Width = app.winfo_screenwidth()
Height= app.winfo_screenheight()
bienvenido = customtkinter.CTkLabel(app,text="Bienvenido a SERMA", font=("Helvetica",80))
botonIniciar = customtkinter.CTkButton(master = app, text="Iniciar")
stringBuscador = ""
buscador = customtkinter.CTkEntry(app,corner_radius=50,textvariable=stringBuscador, width=200 )
contador = 1 + 0

user = customtkinter.StringVar(app)
contra=customtkinter.StringVar(app)

correonuevo=customtkinter.StringVar(app)

nombrecreado=customtkinter.StringVar(app)
correocreado=customtkinter.StringVar(app)
usuariocreado= customtkinter.StringVar(app)
contracreado=customtkinter.StringVar(app)


iniciarEst = customtkinter.CTkLabel(app,text="Inicio de sesión\nusuario", font=("Helvetica",38), fg_color='transparent')
iniciarEst.place(relx=0.06, y=150)

iniciarDoc = customtkinter.CTkLabel(app,text="Inicio de sesión\ndocente", font=("Helvetica",38), fg_color='transparent')
iniciarDoc.place(relx=0.76, y=150)

textoinicio = customtkinter.CTkLabel(app,text="Ingresa tus datos", font=("Helvetica",38), fg_color='transparent')
usuario = customtkinter.CTkEntry(app,corner_radius=50,textvariable=stringBuscador)
contraseña = customtkinter.CTkEntry(app, placeholder_text="Ingresa tu contraseña",corner_radius=50,show="*",textvariable=contra)

Contraseñalabel = customtkinter.CTkLabel(app, text="Contraseña", font=("Helvetica",24) )

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
#Este ese ejecuta cuando se da click al boton para ingresar como estudiante
    itipo=0
    aparecer()

def docenteEntrar():
#Este ese ejecuta cuando se da click al boton para ingresar como docente
    itipo=1
    aparecer()

def aparecer():
    #aparece los elementos de la interfaz para inicio de sesión
    labelSERMA.place_forget()
    BotonDoc.place_forget()
    BotonEst.place_forget()
    labelDoc.place_forget()
    labelEst.place_forget()
    iniciarDoc.place_forget()
    iniciarEst.place_forget()
    textoinicio.place(relx=0.4, y=130)
    usuario.place(relx=0.45, y=250)
    contraseña.place(relx=0.45, y=280)
    BotonInicio.place(relx=0.45, y=320)
    olvidaste.place(relx=0.45, y=370)
    BotonCrear.place(relx=0.45, y=420)

def iniciosesion():
    #cuando se da click al boton de iniciar sesion, se ejecuta esto
    textoinicio.place_forget()
    usuario.place_forget()
    contraseña.place_forget()
    BotonInicio.place_forget()
    olvidaste.place_forget()
    BotonCrear.place_forget()

def cambiardatos():
#Se ejecuta cuando se da al boton de que se olvido la contraseña
    def cambioAccion():
        #Se ejecuta cuando se da al boton de recuperar credenciales, cierra la ventana pop up
        alerta.destroy()
        alerta.update()
    alerta = customtkinter.CTkToplevel()
    alerta.title("Recuperar contraseña")
    A12= customtkinter.CTkLabel(master = alerta,text="Inserte su correo", font=("Helvetica",12), fg_color='transparent')
    boto = customtkinter.CTkButton(master = alerta, text="Recuperar contraseña",command=cambioAccion)
    usuarioolvido = customtkinter.CTkEntry(master = alerta,corner_radius=50,textvariable=correonuevo)
    A12.pack(pady=10)
    usuarioolvido.pack(pady=10)
    boto.pack(pady=10)

def crearUsuario():
#Se ejecuta cuando se da al boton de crear usuario 
    def cambioAccion():
        #Se ejecuta cuando se da al boton de recuperar credenciales, cierra la ventana pop up
        
        alerta.destroy()
        alerta.update()
    alerta = customtkinter.CTkToplevel()
    alerta.title("Crear usuario")
    boto = customtkinter.CTkButton(master = alerta, text="Crear",command=cambioAccion)
    A1= customtkinter.CTkLabel(master = alerta,text="Inserte nombre", font=("Helvetica",12), fg_color='transparent')
    nombredatosnuevo = customtkinter.CTkEntry(master = alerta,corner_radius=50,textvariable=nombrecreado)
    A2= customtkinter.CTkLabel(master = alerta,text="Inserte correo", font=("Helvetica",12), fg_color='transparent')
    correodatosnuevo = customtkinter.CTkEntry(master = alerta,corner_radius=50,textvariable=correocreado)
    A4= customtkinter.CTkLabel(master = alerta,text="Inserte contraseña", font=("Helvetica",12), fg_color='transparent')
    contradatosnuevo = customtkinter.CTkEntry(master = alerta,corner_radius=50,textvariable=contracreado)
    A1.pack(pady=10)
    nombredatosnuevo.pack(pady=10)
    A2.pack(pady=10)
    correodatosnuevo.pack(pady=10)
    A4.pack(pady=10)
    contradatosnuevo.pack(pady=10)
    boto.pack(pady=10)


BotonEst = customtkinter.CTkButton(master = app, text="Ingresar", command=estudianteEntrar)
BotonEst.place(relx=0.1, y=600)

BotonInicio = customtkinter.CTkButton(master = app, text="Iniciar sesion", command=iniciosesion)

olvidaste = customtkinter.CTkButton(master = app, text="¿Olvidaste tus datos?", command=cambiardatos)

BotonDoc = customtkinter.CTkButton(master = app, text="Ingresar", command=docenteEntrar)
BotonDoc.place(relx=0.8, y=600)

BotonCrear=customtkinter.CTkButton(master = app, text="Crear cuenta", command=crearUsuario)

ImgSERMA = customtkinter.CTkImage(light_image=Image.open("image\\SERMA.png"),size=(300,300))
labelSERMA = customtkinter.CTkLabel(app, text="" , image=ImgSERMA, height=30, width=30)
labelSERMA.place(relx=0.38, y=150)

ImgDoc = customtkinter.CTkImage(light_image=Image.open("image\\profesor.png"),size=(250,250))
labelDoc = customtkinter.CTkLabel(app, text="" , image=ImgDoc, height=30, width=30)
labelDoc.place(relx=0.77, y=270)

ImgEst= customtkinter.CTkImage(light_image=Image.open("image\\estudiante.png"),size=(250,250))
labelEst = customtkinter.CTkLabel(app, text="" , image=ImgEst, height=30, width=30)
labelEst.place(relx=0.07, y=270)


app.mainloop()