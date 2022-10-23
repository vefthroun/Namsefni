from flask import Flask, render_template
app = Flask(__name__)

"""
Include er Leið til að búta niður vef í endurnýtanlega skráarparta.
https://jinja.palletsprojects.com/en/3.0.x/templates/#include

{% include 'header.html' %}
    Body
{% include 'footer.html' %}
"""

@app.route('/')
def index():
    user = {'username': 'Gunnar'}
    return render_template('include.html', title='Tölvubraut', user=user)

# This starts the web app 
if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  
    
