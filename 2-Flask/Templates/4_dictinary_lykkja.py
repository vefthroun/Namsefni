from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    
    # dictionary
    cuisines = {
        "Italy": "Neapolitan Pizza",
        "France": "Baguette",
        "Spain": "Churros",
        "Japan": "Sushi",
        "India": "Dosa",
    }

    return render_template("template4.html", cuisines=cuisines)

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  
    
