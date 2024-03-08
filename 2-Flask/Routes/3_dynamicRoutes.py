from flask import Flask
# escapes characters so it is safe to use in HTML, https://pypi.org/project/MarkupSafe/
from markupsafe import escape
app = Flask(__name__)

"""
Hægt er að búa til URL sem eru dýnamísk (ekki harðkóðuð).
https://flask.palletsprojects.com/en/2.3.x/quickstart/#variable-rules
"""

# Parameters can be used when creating routes. 
# A parameter can be a string (text) like this: /product/cookie.
@app.route('/product/<name>')
def demo1(name):
  return "The product is " + str(name) # The product is cookie


# Skilar það sem þú skrifa í URL t.d. Gunnar  t.d. http://127.0.0.1:5000/user/Gunnar  
@app.route('/user/<username>')
def demo2(username):                       
    return 'User: %s' % (username)    # birtir strenginn "User: Gunnar"
                                      # string formatting: https://www.learnpython.org/en/String_Formatting
    
# að óvirkja html og JavaScript með escape falli                                          
@app.route('/user/<username>')
def demo3(username="Guest"):              # hægt að hafa sjálfgefið gildi
    return 'User: %s' % escape(username)    # escapes() so it is safe to use input characters in HTML
                                            
       
if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  

# Keyrðu python skránna og skrifaðu nafnið þitt í URL.
