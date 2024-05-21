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
        Bienvenido()
            
    
t = threading.Timer(3, entras)


def validacion():
     if contra.get()== "1234":
          Bienvenido()

def Bienvenido():

    
    print("si")
    inicio.place_forget()
    contraseña.place_forget()
    Contraseñalabel.place_forget()
    button.place_forget()
    logolabel.place_forget()
    huellabutton.place_forget()

    
    bienvenido.place(relx=0.38, rely=0.4)
    f = threading.Timer(3, escritorio)
    f.start()


def inicioHuella():
    
    contraseña.place_forget()
    Contraseñalabel.place_forget()
    button.place_forget()
    global botonIniciar
    botonIniciar._command = inicioProgreso
    if(contador == 1):
        
        botonIniciar.place(relx=0.45, y=710)
    else:
        print("Vamos")
        botonIniciar.place_forget()
        botonIniciar.destroy()
        botonIniciar = customtkinter.CTkButton(master = app, text="Intentar nuevamente",command = inicioProgreso)
        botonIniciar.place(relx=0.45, y=710)
   
    
   

    



def inicioProgreso():
    global contador
    contador = contador + 1
    t = threading.Timer(3, entras)
    huellaCargalabel.place(relx=0.45, y=550)
    t.start()
    
    



inicio = customtkinter.CTkLabel(app,text="Nicolas", font=("Helvetica",38), fg_color='transparent')
inicio.place(relx=0.45, y=150)


ImageUser = customtkinter.CTkImage(light_image=Image.open("image\\Navarrete.png"),size=(300,300))
logolabel = customtkinter.CTkLabel(app, text="" , image=ImageUser, height=30, width=30)
logolabel.place(relx=0.4, y=200)

ImageHuella = customtkinter.CTkImage(light_image=Image.open("image\\Huella.png"),size=(50,50))
huellabutton = customtkinter.CTkButton(app, text="" , image=ImageHuella, height=30, width=30, command=inicioHuella)
huellabutton.place(relx=0.9, y=700)


user = customtkinter.StringVar(app)
contra = customtkinter.StringVar(app)


Contraseñalabel = customtkinter.CTkLabel(app, text="Contraseña", font=("Helvetica",24) )
Contraseñalabel.place(relx=0.4, y=550)


contraseña = customtkinter.CTkEntry(app, placeholder_text="Ingresa tu contraseña",corner_radius=50,show="*",textvariable=contra )
contraseña.place(relx=0.5, y=550)


button = customtkinter.CTkButton(master = app, text="Ingresar", command=validacion)
button.place(relx=0.45, y=600)


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