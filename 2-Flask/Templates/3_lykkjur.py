# sækjum einnig render_template
from flask import Flask, render_template

app = Flask(__name__)

"""
Jinja template and loops
"""
@app.route('/')
def index():
    # dictionary
    user = {'username': 'guest'}
    # list
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('template2.html', title='Home', user=user, posts=posts)

# This starts the web app 
if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)