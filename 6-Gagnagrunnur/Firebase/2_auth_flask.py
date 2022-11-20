from flask import Flask, session
import pyrebase, os

app = Flask(__name__)

# session lykill
app.secret_key = os.urandom(8)

# tenging við Firebase gagnagrunninn 
config = {
    "apiKey": "NOTA YKKAR KEY",
    "authDomain": "verkefni6-4265f.firebaseapp.com",
    "projectId": "verkefni6-4265f",
    "storageBucket": "verkefni6-4265f.appspot.com",
    "messagingSenderId": "746762172223",
    "appId": "1:746762172223:web:4bb950f0fa7b8d1168058a",
    "measurementId": "G-PBS5F76K22",
    "databaseURL": "https://NAFN Á GAGNAGRUNNI.firebaseio.com",
}

fb = pyrebase.initialize_app(config)
auth = fb.auth()

@app.route('/signup')
def signup():
    try:
        user = auth.create_user_with_email_and_password("email@example.is","1234567")
    except:
        print("could not create user")
    return "Athugaðu færslu"


@app.route('/login')
def login():
    try:
        # To sign in user using email and password
        sign_user = auth.sign_in_with_email_and_password("email@example.is", "1234567")
        # before the 1 hour expiry:
        sign_user = auth.refresh(sign_user['refreshToken'])
        # now we have a fresh token
        print(sign_user['idToken'])      
        session['user'] = sign_user['idToken']
        print(session['user'])
        print("sign In Successfull")
    except:
        print("Some thing happend!! could not sign in")
    
    return "Skoðaðu print í terminal"
    
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)

