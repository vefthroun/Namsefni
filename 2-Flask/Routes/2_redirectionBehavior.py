# import Flask class in Python
from flask import Flask

# Create app, that hosts the application
app = Flask(__name__)

"""
Unique URLs / Redirection Behavior: 
https://flask.palletsprojects.com/en/2.1.x/quickstart/#unique-urls-redirection-behavior
"""

# Ef þú slærð inn vefslóð án skástriks í enda (/projects) þá mun Flask e. redirect á /projects/
@app.route('/projects/')
def projects():
    return 'The project page'
    
# Ef þú slærð inn vefslóð með skrástriki í enda /about/ þá munt þú fá 404 villu. (ekki redirekt)
@app.route('/about')
def about():
    return 'The about page'

# This starts the web app 
if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  
  
# Keyrðu python skránna og skoðaðu url í vafra

   
