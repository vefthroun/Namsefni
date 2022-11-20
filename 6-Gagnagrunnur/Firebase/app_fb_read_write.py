# https://github.com/nhorvath/Pyrebase4  
import pyrebase # pip3 install pyrebase4 

# stillingar til að tengjast firebase realtime database á firebase.google.com 
firebaseConfig = {
 # config breytur ...
}

# init app með tengingu við gagnagrunn 
firebase=pyrebase.initialize_app(firebaseConfig)

# database
db=firebase.database()

# búa til gögn fyrir gagnagrunn
data1 = {"age": 25, "address": "Tækniskólinn", "employed": True, "name": "Daníel"}
data2 = {"age": 30, "address": "Tækniskólinn", "employed": True, "name": "Gunnar"}

# skrifa gögn í gagnagrunn í flokkinn teachers. Skoðaðu svo gagnagrunninn á firebase.google.com
db.child("teachers").push(data1)
db.child("teachers").push(data2)


# að lesa gögn (alla kennara) frá gagnagrunn
response = db.child("teachers").get().val()   # fáum raðað dictionary




"""
from flask import Flask
import pyrebase

app = Flask(__name__)

# tengin við firebase realtime database á firebase.google.com 
config = {
    # hér kemur tengingin þín við Firebase gagnagrunninn ( realtime database )
}
fb = pyrebase.initialize_app(config)

db = fb.database()

# Test route til að setja gögn í db
@app.route('/skrifa')
def index():
    # skrifum nýjan í grunn hnútur sem heitir notandi 
    db.child("notandi").push({"notendanafn":"user", "lykilorð":psw)}) 
    return "Skrifað í grunn"

# Test route til að sækja öll gögn úr db
@app.route('/lesa')
def lesa():	
   # förum í grunn og sækjum allar raðir ( öll gögn )
   response = db.child("notandi").get().val()  # fáum raðað dictionary í response
   data = list(response.items()) 	       # breytum í lista með tuples
   return "Lesum úr grunni"

if __name__ == "__main__":
	app.run(debug=True)

"""
