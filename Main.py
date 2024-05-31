import customtkinter
from PIL import Image
import logica

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("blue")
itipo=0
cuenta=False
#IMPORTANTE, itipo define si es docente o estudiante
app = customtkinter.CTk()
app.attributes("-fullscreen", True)
app.title("SERMA")
app.after(201, lambda :app.iconbitmap('image\\SERMA.ico'))
Width = app.winfo_screenwidth()
Height= app.winfo_screenheight()
bienvenido = customtkinter.CTkLabel(app,text="Bienvenido a SERMA", font=("Helvetica",80))

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
usuario = customtkinter.CTkEntry(app,corner_radius=50,placeholder_text="Ingresa tu correo",font=("Helvetica",11))
contraseña = customtkinter.CTkEntry(app, placeholder_text="Ingresa tu contraseña",font=("Helvetica",11),corner_radius=50,show="*")
Contraseñalabel = customtkinter.CTkLabel(app, text="Contraseña", font=("Helvetica",24) )
materr= customtkinter.CTkLabel(master = app,text="Materias", font=("Helvetica",20), fg_color='transparent')
guiass= customtkinter.CTkLabel(master = app,text="Guias", font=("Helvetica",20), fg_color='transparent')
descripcion=customtkinter.CTkLabel(app,text="Desc Guia", font=("Helvetica",38), fg_color='transparent')
tarea=customtkinter.CTkLabel(app,text="Desc Guia", font=("Helvetica",38), fg_color='transparent')
def devolverse():
    if cuenta==True:
        listamaterias.place_forget()
        listaguias.place_forget()
        crearmat.place_forget()
    materr.place_forget()
    guiass.place_forget()
    textoinicio.place_forget()
    usuario.place_forget()
    contraseña.place_forget()
    BotonInicio.place_forget()
    olvidaste.place_forget()
    BotonCrear.place_forget()
    BotonDevolverse.place_forget()
    labelSERMA.place(relx=0.38, y=150)
    BotonDoc.place(relx=0.8, y=600)
    BotonEst.place(relx=0.1, y=600)
    labelDoc.place(relx=0.77, y=270)
    labelEst.place(relx=0.07, y=270)
    iniciarDoc.place(relx=0.76, y=150)
    iniciarEst.place(relx=0.06, y=150)
  
def estudianteEntrar():
#Este ese ejecuta cuando se da click al boton para ingresar como estudiante
    global itipo
    itipo=0
    aparecer()

def docenteEntrar():
#Este ese ejecuta cuando se da click al boton para ingresar como docente
    global itipo
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
    descripcion.place_forget()
    tarea.place_forget()
    textoinicio.place(relx=0.4, y=130)
    usuario.place(relx=0.45, y=250)
    contraseña.place(relx=0.45, y=280)
    BotonInicio.place(relx=0.45, y=320)
    olvidaste.place(relx=0.45, y=370)
    BotonCrear.place(relx=0.45, y=420)
    BotonDevolverse.place(relx=0.85, y=20)

def iniciosesion():
    #cuando se da click al boton de iniciar sesion, se ejecuta esto
    global usuario
    global contraseña
    global user
    global contra
    global descripcion
    global tarea
    global tareaa
    bru="123"
    user=usuario.get()
    contra=contraseña.get()
    valido=logica.login(user,contra)
    def crearmateria():
        #aca crear materias nuevas
        #tarea.configure(text="Encontrar palabras magicas")
        #tarea.update()
        #print(tarea.cget("text")) Con esto consigo el text
        #lambda: para que tenga parametros
        print("Huh")
    def añadirguias(e):
        #aca añadir las guias con un for
        print(e)
        

             


    def finmen():
        #se cierra el pop up de mal inicio de sesión
        alerta.destroy()
        alerta.update()
    if valido:
        global listamaterias
        global listaguias
        global crearmat
        global BotonDevolverse
        global cuenta,app
        cuenta=True
        textoinicio.place_forget()
        usuario.place_forget()
        contraseña.place_forget()
        BotonInicio.place_forget()
        olvidaste.place_forget()
        BotonCrear.place_forget()
        #BotonDevolverse.configure(text="Hm")Cambiar texto
        #BotonDevolverse.update()
        if itipo==1:
            listamaterias=customtkinter.CTkScrollableFrame(app,height=650)
            listaguias=customtkinter.CTkScrollableFrame(app,height=650)
        else:
            listamaterias=customtkinter.CTkScrollableFrame(app,height=640)
            listaguias=customtkinter.CTkScrollableFrame(app,height=640)
        crearmat=customtkinter.CTkButton(master=app,text="Crear materia",command=crearmateria)
        #aca añadir las materias con un for

        listaa=logica.consultarMaterias()
        for u in listaa: 
            btn = customtkinter.CTkButton(listamaterias,text=u, command=lambda j=u: añadirguias(j) )           
            btn.pack(pady=10)


        descripcion.place(relx=0.6, y=200)
        tarea.place(relx=0.6, y=400)
        if itipo==1:
            listamaterias.place(relx=0.01, y=90)
            listaguias.place(relx=0.2,y=90)
            materr.place(relx=0.06, y=60)
            guiass.place(relx=0.25,y=60)
            crearmat.place(relx=0.035, y=20)
        else:
            materr.place(relx=0.06, y=40)
            listamaterias.place(relx=0.01, y=70)
            listaguias.place(relx=0.2,y=70)
            guiass.place(relx=0.25,y=40)
    else:
        alerta = customtkinter.CTkToplevel()
        alerta.title("Recuperar contraseña")
        alerta.after(201, lambda :alerta.iconbitmap('image\\SERMA.ico'))
        Mensaj= customtkinter.CTkLabel(master = alerta,text="Correo y/o contraseña invalidos\nIngresa datos validos", font=("Helvetica",12), fg_color='transparent')
        But=customtkinter.CTkButton(master = alerta, text="Ok",command=finmen)
        Mensaj.pack(pady=10)
        But.pack(pady=10)
        
def cambiardatos():
#Se ejecuta cuando se da al boton de que se olvido la contraseña
    def cambioAccion():
        #Se ejecuta cuando se da al boton de recuperar credenciales, cierra la ventana pop up
        alerta.destroy()
        alerta.update()
    global correonuevo
    alerta = customtkinter.CTkToplevel()
    alerta.title("Recuperar contraseña")
    alerta.after(201, lambda :alerta.iconbitmap('image\\SERMA.ico'))
    A12= customtkinter.CTkLabel(master = alerta,text="Inserte su correo", font=("Helvetica",12), fg_color='transparent')
    boto = customtkinter.CTkButton(master = alerta, text="Recuperar contraseña",command=cambioAccion)
    usuarioolvido = customtkinter.CTkEntry(master = alerta,corner_radius=50,textvariable=correonuevo)
    A12.pack(pady=10)
    usuarioolvido.pack(pady=10)
    boto.pack(pady=10)

def crearUsuario():
    alerta = customtkinter.CTkToplevel()
    alerta.title("Crear usuario")
    alerta.after(201, lambda :alerta.iconbitmap('image\\SERMA.ico'))
    A1= customtkinter.CTkLabel(master = alerta,text="Inserta tus datos", font=("Helvetica",12), fg_color='transparent')
    nombredatosnuevo = customtkinter.CTkEntry(master = alerta,corner_radius=50,placeholder_text="Ingresa tu nombre",font=("Helvetica",11))
    correodatosnuevo = customtkinter.CTkEntry(master = alerta,corner_radius=50,placeholder_text="Ingresa tu correo",font=("Helvetica",11))
    contradatosnuevo = customtkinter.CTkEntry(master = alerta,corner_radius=50,placeholder_text="Ingresa tu contraseña",font=("Helvetica",11),show="*")
    A1.pack(pady=10)
    nombredatosnuevo.pack(pady=10)
    correodatosnuevo.pack(pady=10)
    contradatosnuevo.pack(pady=10)
    def cambioAccion():
        #Se ejecuta cuando se da al boton de recuperar credenciales, cierra la ventana pop up
        global nombrecreado
        global correocreado
        global contracreado
        global itipo
        nombrecreado=nombredatosnuevo.get()
        correocreado=correodatosnuevo.get()
        contracreado=contradatosnuevo.get()
        logica.crearUsuario(correocreado,contracreado,nombrecreado,itipo)
        alerta.destroy()
        alerta.update()
    boto = customtkinter.CTkButton(master = alerta, text="Crear",command=cambioAccion)
    boto.pack(pady=10)



BotonEst = customtkinter.CTkButton(master = app, text="Ingresar", command=estudianteEntrar)
BotonEst.place(relx=0.1, y=600)

BotonInicio = customtkinter.CTkButton(master = app, text="Iniciar sesion", command=iniciosesion)

olvidaste = customtkinter.CTkButton(master = app, text="¿Olvidaste tus datos?", command=cambiardatos)

BotonDoc = customtkinter.CTkButton(master = app, text="Ingresar", command=docenteEntrar)
BotonDoc.place(relx=0.8, y=600)

BotonCrear=customtkinter.CTkButton(master = app, text="Crear cuenta", command=crearUsuario)

BotonDevolverse=customtkinter.CTkButton(master = app, text="Volver al inicio", command=devolverse)
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