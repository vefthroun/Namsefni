from flask import Flask, render_template, request, session, redirect, url_for
import pyrebase

app = Flask(__name__)

# tengin við firebase realtime database á firebase.google.com
config = {
    # Þið setjið ykkar tengiupplýsingar hér ...
}
fb = pyrebase.initialize_app(config)
db = fb.database()


@app.route('/')
def index():
    return "<a href='/breyta'>Breyta</a><br><a href='/eyda'>Eyða</a>"


@app.route('/eyda')
def eyda():
    # Þið setjið ykkar upplýsingar hér
    db.child("bill").child("____").remove()
    return "Bíl eytt úr db"


@app.route('/breyta')
def breyta():
    # Þið setjið ykkar upplýsingar hér
    db.child("bill").child("____").update({"nr":"????", "tegund":"????", "utegund":"????", "argerd":"????","akstur":"????"})
    return "Bíl breytt í db"


if __name__ == "__main__":
	app.run(debug=True)
