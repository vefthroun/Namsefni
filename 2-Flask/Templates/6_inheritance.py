from flask import Flask, render_template

app = Flask(__name__)

"""
Template Inheritance

Move the parts of the page layout that are common to all templates to one base template, 
from which all other templates are derived.

base.html      the general page structure, (base template); head, body, header, nav, footer etc.
index.html     the content part, example index.html inherit (extends) from base.html

The extends statement establishes the inheritance link between the two templates. 
Jinja2 knows that when it is asked to render index.html it needs to embed it inside base.html. 
The two templates have matching block statements with name content.

"""

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'guest'}
    return render_template('index.html', title='Home', user=user)

# This starts the web app 
if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  
    
