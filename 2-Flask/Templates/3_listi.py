from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    users = ['Gunnar', 'Daníel']
    return render_template('template3.html', users=users)

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  
    
