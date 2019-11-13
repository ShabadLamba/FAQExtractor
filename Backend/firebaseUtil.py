import pyrebase
import requests


class firebaseUtil:

    config = {
        "apiKey": "AIzaSyA60pxujJvEyhN6SkANmkhSqUMLMaJEgDI",
        "authDomain": "questionsandanswersdatabase.firebaseapp.com",
        "databaseURL": "https://questionsandanswersdatabase.firebaseio.com/",
        "projectId": "questionsandanswersdatabase",
        "storageBucket": "questionsandanswersdatabase.appspot.com",
        "messagingSenderId": "610071156368",
        "appId": "1:610071156368:web:73bb8022a2c8dedc"
    }
    firebase = pyrebase.initialize_app(config)
    db = firebase.database()

    def __init__(self):
        firebase = self.firebase
        db = self.db

    def firebaseAuth(self):
        # Get a reference to the auth service
        auth = self.firebase.auth()

        email = "shabad.l@imimobile.com"
        password = "123@lamba"

        # Log the user in
        user = auth.sign_in_with_email_and_password(email, password)

        # before the 1 hour expiry:
        user = auth.refresh(user['refreshToken'])
        # now we have a fresh token
        # print(user['idToken'])

        # Get a reference to the database service
        return user

    def setData(self, user, keyName, listOfData):
        self.db.child("data").child("qna").child(
            keyName).set(listOfData, user["idToken"])

    def getData(self):
        return(self.db.child("data").child("qna").get().val())
