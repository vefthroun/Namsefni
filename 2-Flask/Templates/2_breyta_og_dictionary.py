from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    # data
    title = "Jinja"
    user = {'username': 'Jón Jónsson', 'aldur': 37}
   
    # sendum dictionary (user) og breytuna (title) í template
    return render_template('template2.html', title=title, user=user)

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  
    
