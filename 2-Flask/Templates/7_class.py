from flask import Flask, render_template
app = Flask(__name__)


# define custom data structure with a class
class GalileanMoons:
    def __init__(self, first, second, third, fourth):
        self.first = first
        self.second = second
        self.third = third
        self.fourth = fourth


@app.route('/')
def index():

    # custom data structure operations
    moons = GalileanMoons("Io", "Europa", "Ganymede", "Callisto")
    
    # dictionary
    kwargs = { "moons": moons }

    return render_template("template7.html", **kwargs)

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  
    
