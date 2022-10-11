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
@app.route('/')
def index():
    return "Skrifað í grunn"

# Test route til að sækja öll gögn úr db
@app.route('/lesa')
def lesa():
    return "Lesum úr grunni"

if __name__ == "__main__":
	app.run(debug=True)

# skrifum nýjan í grunn hnútur sem heitir notandi 
# db.child("notandi").push({"notendanafn":"user", "lykilorð":psw)}) 

# # förum í grunn og sækjum allar raðir ( öll gögn )
# u = db.child("notandi").get().val()
# lst = list(u.items())
