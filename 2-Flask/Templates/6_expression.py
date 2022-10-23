from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    # data
    first_name = "Captain"
    last_name = "Marvel"
    kwargs = {
        "color": "brown",
        "animal_one": "fox",
        "animal_two": "dog",
        "orange_amount": 10,
        "apple_amount": 20,
        "first_name": first_name,
        "last_name": last_name,
    }
    # Notum dictionary unpacking operator ** til að vinna með breytur í template.
    return render_template("template6.html", **kwargs)

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  
    
