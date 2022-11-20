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

