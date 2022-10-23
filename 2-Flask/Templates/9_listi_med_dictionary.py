from flask import Flask, render_template
app = Flask(__name__)


# listi sem inniheldur dictionary 
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
    
    return render_template('template9.html', title='Home', user=user, posts=posts)


if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)
