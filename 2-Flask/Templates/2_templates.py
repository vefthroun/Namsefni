# sækjum einnig render_template
from flask import Flask, render_template
app = Flask(__name__)

"""
Simple Jinja template use case.
The render_template() function invokes the Jinja template engine that comes bundled with the Flask framework. 
Jinja substitutes {{ ... }} blocks with the corresponding values, given by the arguments provided in the render_template() call.
HTML special characters are escaped automatically to prevent XSS attacks.

"""

@app.route('/')
def demo2():
    # data
    title = "Jinja"
    user = {'username': 'Jón Jónsson'}
    
    # sendum dictionary (user) og breytuna (title) í template
    # skilum html (index.html) sem er vistuð í templates möppu (þurfum ekki að vísa í hana) 
    return render_template('template1.html', title=title, user=user)


if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  
    
