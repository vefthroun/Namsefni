
# import Flask class in Python
from flask import Flask

# Create app, that hosts the application
app = Flask(__name__)

# You can bind more than one route to a single callback (Chaining Decorators)
@app.route('/')
@app.route('/index')
def page():
    # blöndum saman html elementum og texta í streng sem við skilum.
    return "<h1>Halló Heimur!</h1>"

# This starts the web app 
if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  # This will allow the app to display a proper Python error message, so you can fix the typo/syntax error.
  
# Keyrðu python skránna og skoðaðu url í vafra

   
