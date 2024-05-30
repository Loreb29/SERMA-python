
import pyrebase

firebaseConfig={
    "apiKey": "AIzaSyAxNfMqdzjGirpGok1RlOwOI-f8W_ACG_Q",
    "authDomain": "serma-8c60c.firebaseapp.com",
    "databaseURL": "https://serma-8c60c-default-rtdb.firebaseio.com",
    "projectId": "serma-8c60c",
    "storageBucket": "serma-8c60c.appspot.com",
    "messagingSenderId": "313118845898",
    "appId": "1:313118845898:web:5081165c3c222ea4a97d33"
}


firebase = pyrebase.initialize_app(firebaseConfig)

db = firebase.database()

data = {"guia1":{"descricion":"The world magic", "tarea":"Encontrar palabras magicas"}}

db.child("materia").child("inglés").set(data)