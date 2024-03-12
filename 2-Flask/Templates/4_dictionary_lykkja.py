from flask import Flask, render_template
app = Flask(__name__)

# Looping Through Dictionary Objects
# https://python-web.teclado.com/section07/lectures/07_jinja2_loops/#looping-through-dictionary-objects

@app.route('/')
def index():
    
    # dictionary
    cuisines = {
        "Italy": "Neapolitan Pizza",
        "France": "Baguette",
        "Spain": "Churros",
        "Japan": "Sushi",
        "India": "Dosa",
        'Iceland': 'Hákarl'
    }

    return render_template("template4.html", cuisines=cuisines) 

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  
    
