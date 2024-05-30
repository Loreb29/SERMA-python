
import pyrebase

#Autenticación de la base de datos
firebaseConfig={
    "apiKey": "AIzaSyAxNfMqdzjGirpGok1RlOwOI-f8W_ACG_Q",
    "authDomain": "serma-8c60c.firebaseapp.com",
    "databaseURL": "https://serma-8c60c-default-rtdb.firebaseio.com",
    "projectId": "serma-8c60c",
    "storageBucket": "serma-8c60c.appspot.com",
    "messagingSenderId": "313118845898",
    "appId": "1:313118845898:web:5081165c3c222ea4a97d33"
}


#Variables inciales de la base de datos y autentificación   
firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()
db = firebase.database()


#Metodo para crear usuario e ingresar sus datos en la base de datos
def crearUsuario(email, password, nombre , docente):

    try:
        user = auth.create_user_with_email_and_password(email= email, password=password)
        ingresarDatos(format(user['localId']), nombre, docente)
    except:
       print("El usuario ya existe")




#Ingresa a la base de datos los datos personales de nuestro usuario tomando como clave la idLocal
def ingresarDatos(user, nombre, docente):
    if( docente == 0):
        db.child("user").child(user).set({ 'nombre':nombre, 'docente':docente } )  



#Inicio de sesión que retorna False o True
def login(email, password):
    try:
        user = auth.sign_in_with_email_and_password(email= email, password=password)
        return True
    except:
        print("Credenciales incorrectas")
        return False
    

def crearMateria(materia):
    try:   
        db.child("materia").set(materia)
    except:
        print("La materia ya existe")






# Metodo sin revisar
def crearGuia(materia):
    result = db.coll
    data = {"guia1":{"descricion":"The world magic", "tarea":"Encontrar palabras magicas"}}
    db.child("materia").child(materia).set(data)



#Consulta y devuelve un arreglo con el nombre de las materias 
def consultarMaterias():
    lista = db.child("materia").get() 
    return crearArreglo(lista)


#Consulta y devuelve un arreglo con el nombre de las guias
def consultarGuia(materia):
    lista = db.child("materia").child(materia).get()    
    return crearArreglo(lista)


def consultarDatosGuia(materia, guia):
    lista = db.child("materia").child(materia).child(guia).get()  


#Genera un arreglo con los nombre del objeto que pasa
def crearArreglo(objeto):
    arreglo = []
    for u in objeto.each():
        arreglo.append(u.key())
    
    return arreglo






   
   

  
#login("Cristian@gmail.com","123")

#crearUsuario("Cristian@gmail.com","123456","Cristian", "1")