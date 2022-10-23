
from flask import Flask, render_template
app = Flask(__name__)

# Mixing Loops & Conditionals
# https://python-web.teclado.com/section07/lectures/07_jinja2_loops/#mixing-loops-conditionals

@app.route('/')
def index():
    
    # list of tuples
    user_os = [
        ("Miller", "Windows"),
        ("Bob", "MacOS"),
        ("Zach", "Linux"),
        ("Annie", "Linux"),
        ("Farah", "Windows"),
        ("George", "Windows"),
    ]

    return render_template("template8.html", user_os=user_os)
    
if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  
    
