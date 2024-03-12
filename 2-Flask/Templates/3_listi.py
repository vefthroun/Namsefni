from flask import Flask, render_template
app = Flask(__name__)

# Looping Through List Objects
# https://python-web.teclado.com/section07/lectures/07_jinja2_loops/#looping-through-list-objects

@app.route('/')
def index():
    users = ['Gunnar', 'Daníel', 'Guðmundur','Sigríður']
    return render_template('template3.html', users=users)

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  
    
