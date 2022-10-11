# sækjum einnig render_template
from flask import Flask, render_template

app = Flask(__name__)

"""
Include
https://jinja.palletsprojects.com/en/2.11.x/templates/#include

Önnur leið til að búta niður vef í endurnýtanlega skráarparta.

{% include 'header.html' %}
    Body
{% include 'footer.html' %}
"""

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'guest'}
    return render_template('include.html', title='Home', user=user)

# This starts the web app 
if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  
    
