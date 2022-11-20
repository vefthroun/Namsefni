
# https://github.com/nhorvath/Pyrebase4
# þarf pip3 install pyrebase4 
import pyrebase

# stillingar til að tengjast firebase realtime database á firebase.google.com 
firebaseConfig = {
  "apiKey": "Setja ykkar eigin KEY",
  "authDomain": "vefur3.firebaseapp.com",
  "databaseURL": "https://NAFN Á Gagnagrunni.firebaseio.com",
  "projectId": "vefur3",
  "storageBucket": "vefur3.appspot.com",
  "messagingSenderId": "723537595408",
  "appId": "1:723537595408:web:13bd005e43576b1b318e95"
}

#  init app með tengingu við gagnagrunn 
firebase=pyrebase.initialize_app(firebaseConfig)

# Authentication: Build -> Authentication á https://console.firebase.google.com/
# authentication á user í fb.
auth=firebase.auth()

# login
email=input("enter email")
password=input("enter password")

# login validation þar sem einn notandi er þegar til í fb.
try:
    user = auth.sign_in_with_email_and_password(email, password) 
    print("Successfully signed in!")
    print(user)
except:
    print("Invalid user or password. Try Again!")

    
# Að búa til user með python, pyrebase
# user = auth.create_user_with_email_and_password("test@tskoli.is","1234567")
# print(user)
