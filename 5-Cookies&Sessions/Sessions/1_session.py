from flask import Flask, render_template, session, redirect
import os

app = Flask(__name__)

# session lykill
app.secret_key = os.urandom(8)
# print(os.urandom(8))

# id, heiti, mynd, verð
vorur = [
    [0, "Peysa",  "peysa.jpg",  2500],
    [1, "Buxur",  "buxur.jpg",  3500],
    [2, "Jakki",  "jakki.jpg",  13500]
]

# forsíðan 
@app.route('/') 
@app.route('/index') 
def index():
    return render_template('vorur.html', vorur=vorur)

# Bætum vöruauðkenni (key) í körfuna
@app.route('/add/<int:id>') 
def add(id):
    # búum til körfu
    karfa = []
    # ef við höfum bætt við id af vöru áður þá
    if "cart_items" in session:
        # sækjum vöruids úr sessions
        karfa = session['cart_items']
        # bætum valda vöru (id) við körfu
        karfa.append(vorur[id])
        # uppfærum session
        session['cart_items'] = karfa
        # skoðum
        print(session['cart_items'])
    # ef karfan er tóm
    else:
        # bætum vöruid í körfu (dictionary)
        karfa.append(vorur[id])
        # bætum vöruid í session
        session['cart_items'] = karfa
        # skoðum 
        print(session['cart_items'])
    # förum aftur á forsíðuna
    return redirect('/index')

# Skoðum körfuna
@app.route("/karfa")
def karfa():
    karfa = []
    # Karfan er ekki tóm
    if 'cart_items' in session:
        karfa = session['cart_items']
        print(karfa)
        return "sjá körfu í console"
    # Karfan er tóm
    else:
        return "Karfan er tóm!"
if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
