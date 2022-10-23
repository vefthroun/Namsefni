from flask import Flask, render_template
app = Flask(__name__)

"""
Jinja substitutes {{ ... }} blocks with the corresponding values, given by the arguments provided in the render_template() call.
HTML special characters are escaped automatically to prevent XSS attacks.
"""

@app.route('/')
def index():
    # data
    title = "Jinja"
    user = {'username': 'Jón Jónsson'}
   
    # sendum dictionary (user) og breytuna (title) í template
    return render_template('template2.html', title=title, user=user)

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  
    
