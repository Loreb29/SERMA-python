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
ImageHuellaCarga = customtkinter.CTkImage(light_image=Image.open("image\\HuellaCarga.png"),size=(150,150))
huellaCargalabel = customtkinter.CTkLabel(app, text="" , image=ImageHuellaCarga, height=50, width=50)
botonIniciar = customtkinter.CTkButton(master = app, text="Iniciar")
stringBuscador = ""
buscador = customtkinter.CTkEntry(app,corner_radius=50,textvariable=stringBuscador, width=200 )
contador = 1 + 0

def entras():
    botonIniciar.place_forget()
    huellaCargalabel.place_forget()
    if(contador == 2):
        alerta = customtkinter.CTkToplevel()

        boto = customtkinter.CTkButton(master = alerta, text="Error en la huella",
                                                command= lambda: alerta.wm_forget)
        boto.pack(pady=10)
    else:
        inicioProgreso()
            
    
t = threading.Timer(3, entras)


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


def inicioProgreso():
    global contador
    contador = contador + 1
    t = threading.Timer(3, entras)
    huellaCargalabel.place(relx=0.45, y=550)
    t.start()
    
    



inicio = customtkinter.CTkLabel(app,text="Inicio de sesión\nusuario", font=("Helvetica",38), fg_color='transparent')
inicio.place(relx=0.06, y=150)

iniciodoc = customtkinter.CTkLabel(app,text="Inicio de sesión\ndocente", font=("Helvetica",38), fg_color='transparent')
iniciodoc.place(relx=0.76, y=150)

ImageUser = customtkinter.CTkImage(light_image=Image.open("image\\Navarrete.png"),size=(300,300))
logolabel = customtkinter.CTkLabel(app, text="" , image=ImageUser, height=30, width=30)

ImageHuella = customtkinter.CTkImage(light_image=Image.open("image\\Huella.png"),size=(50,50))

user = customtkinter.StringVar(app)
#contra = customtkinter.StringVar(app)


Contraseñalabel = customtkinter.CTkLabel(app, text="Contraseña", font=("Helvetica",24) )
#Contraseñalabel.place(relx=0.4, y=550)


#contraseña = customtkinter.CTkEntry(app, placeholder_text="Ingresa tu contraseña",corner_radius=50,show="*",textvariable=contra )
#contraseña.place(relx=0.5, y=550)

def pantallainicio():
    button.place_forget()
    buttondoc.place_forget()
    labelSERMA.place_forget()

button = customtkinter.CTkButton(master = app, text="Ingresar", command=pantallainicio)
button.place(relx=0.1, y=600)



buttondoc = customtkinter.CTkButton(master = app, text="Ingresar", command=inicioProgreso)
buttondoc.place(relx=0.8, y=600)
ImgSERMA = customtkinter.CTkImage(light_image=Image.open("image\\SERMA.png"),size=(300,300))
labelSERMA = customtkinter.CTkLabel(app, text="" , image=ImgSERMA, height=30, width=30)
labelSERMA.place(relx=0.38, y=150)

def escritorio():
    bienvenido.place_forget()
    ImageUser = customtkinter.CTkImage(light_image=Image.open("image\\Mado.png"),size=(300,300))
    logolabel = customtkinter.CTkLabel(app, text="" , image=ImageUser, height=30, width=30)
    logolabel.place(relx=0.38, y=150)
    buscador.place(relx=0.4, y=500)
    ImageHuella = customtkinter.CTkImage(light_image=Image.open("image\\lupa.png"),size=(50,50))
    huellabutton = customtkinter.CTkButton(app, text="" , image=ImageHuella, height=30, width=30, command=buscar,fg_color='transparent' )
    huellabutton.place(relx=0.55, y=480)

def buscar():
    os.startfile(programs[buscador.get()])


programs = {
    'google': r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    'github': r"C:\Users\ASUS\AppData\Local\GitHubDesktop\GitHubDesktop.exe",
    'notocar': r"steam://rungameid/2600140",
    'word': r"C:\Program Files\Microsoft Office\root\Office16\WINWORD.EXE",
    'powerpoint': r"C:\Program Files\Microsoft Office\root\Office16\POWERPNT.EXE",
    'excel': r"C:\Program Files\Microsoft Office\root\Office16\EXCEL.EXE",
    'chat': r"E:\Users\Datos 2022\Desktop\WhatsApp"
}

app.mainloop()