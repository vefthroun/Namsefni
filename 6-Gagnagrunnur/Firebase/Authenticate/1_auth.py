import pyrebase


# tengin við firebase realtime database á firebase.google.com 
# hér kemur tengingin þín við Firebase gagnagrunninn ( realtime database )
config = {
    "apiKey": "Setja ykkar eigin KEY",
    "authDomain": "verkefni6-4265f.firebaseapp.com",
    "projectId": "verkefni6-4265f",
    "storageBucket": "verkefni6-4265f.appspot.com",
    "messagingSenderId": "746762172223",
    "appId": "1:746762172223:web:4bb950f0fa7b8d1168058a",
    "measurementId": "G-PBS5F76K22",
    "databaseURL": "https://NAFN Á Gagnagrunni.firebaseio.com",
}

fb = pyrebase.initialize_app(config)
auth = fb.auth()
user = auth.create_user_with_email_and_password("test5@tskoli.is","1234567")
print(user)
