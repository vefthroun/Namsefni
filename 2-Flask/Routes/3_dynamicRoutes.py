from flask import Flask

# escapes characters so it is safe to use in HTML, https://pypi.org/project/MarkupSafe/
from markupsafe import escape

app = Flask(__name__)

"""

# Dynamic routes: 
https://flask.palletsprojects.com/en/2.1.x/quickstart/#variable-rules

Hægt er að búa til URL sem eru dýnamísk (ekki harðkóðuð).

You can add variable sections to a URL by marking sections with <variable_name>. 
Your function then receives the <variable_name> as a keyword argument.

Dæmi:
    @app.route('/wiki/<pagename>')    # td. /wiki/Learning_Python
    def show_wiki_page(pagename):     
      ...
"""

# Skilar það sem þú skrifa í URL t.d. /user/Gunnar 
# http://127.0.0.1:5000/user/Gunnar  birtir strenginn "User: Gunnar"
@app.route('/user/<username>')
def show_user_profile(username):  # hægt að hafa sjálfgefið gildi: username="Guest"): 
    # show the user profile for that user
    return 'User: %s' % escape(username) 
           # %s %  string formatting: https://www.learnpython.org/en/String_Formatting
           # escapes() so it is safe to use input characters in HTML

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  

# Keyrðu python skránna og skrifaðu nafnið þitt í URL.
