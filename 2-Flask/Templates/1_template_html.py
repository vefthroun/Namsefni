from flask import Flask
# The render_template() function invokes the Jinja template engine that comes bundled with the Flask framework. 
from flask import render_template

app = Flask(__name__)

"""
Jinja substitutes {{ ... }} blocks with the corresponding values, given by the arguments provided in the render_template() call.
HTML special characters are escaped automatically to prevent XSS attacks.
"""

@app.route("/")
def index():
    # skilum html (index.html) sem er vistuð í templates möppu (þurfum ekki að vísa í hana sérstaklega) 
    return render_template("template1.html")
  

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  
    
