from flask import Flask, session
import os
# https://github.com/nhorvath/Pyrebase4
import pyrebase   # pip3 install pyrebase4 

app = Flask(__name__)

# used to sign session cookies for protection against cookie data tampering.
app.secret_key = os.urandom(8)

# stillingar til að tengjast firebase realtime database á firebase.google.com 
firebaseConfig = {
    ...
}

fb = pyrebase.initialize_app(firebaseConfig)

# pyrebase: https://github.com/nhorvath/Pyrebase4#authentication
auth = fb.auth()

# Get a reference to the database service
db = fb.database()


@app.route('/signup')
def signup():
    name = "Gunnar Þórunnarson"
    display_name = "Gunni"
    photo_url = "slóð á ljósmynd af mér"
    email = "dummy2@example.is"
    password = "1234567"

    try:
        # Creating users
        # https://github.com/nhorvath/Pyrebase4#creating-users
       
        user = auth.create_user_with_email_and_password(email, password)
        # print(user) # localId er id á user fyrir auth.
       
        # Add user info
        # user = auth.update_profile(display_name, photo_url, delete_attribute)
    
        # userdata to save in db
        data = {
            "name": name,
            "email": email,
            "avatar": display_name,
            "selfie": photo_url
        }
        # write userdata to db.
        db.child("users").push(data)

    except:
        print("could not create user")
    return "Athugaðu færslu"

@app.route('/login')
def login():
    try:
        # To sign in user using email and password
        user = auth.sign_in_with_email_and_password("email@example.is", "1234567")
        
        # A user's idToken expires after 1 hour
        user = auth.refresh(user['refreshToken'])  # sjá líka Custom tokens
        # now we have a fresh token
        print(user['idToken'])      
       
        # færum id auðkenni í session
        session['user'] = user['idToken']
        
        print("sign In Successfull")
    except:
        print("Some thing happend! could not sign in")
    
    return "Skoðaðu print í terminal"
    
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)

