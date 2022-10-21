from flask import Flask
app = Flask(__name__)

@app.route('/')
def demo1():
    # skilum textastreng í vafra
    return "Halló Heimur!"

# You can bind more than one route to a single callback (Chaining Decorators)
@app.route('/')
@app.route('/index')
def demo2():
    # blöndum saman html elementum og texta í streng sem við skilum.
    return "<h1>Halló Heimur!</h1>"

# Við getum skilað heillri html vefsíðu sem streng
@app.route('/index')
def demo3():
    return '''
    <!DOCTYPE html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
          <h1>Halló</h1>
    </body>
    '''

# Getum notað dictionary í return 
@app.route('/index')
def demo4():
    user = {'username': 'Gunnar'} # dictionary
    return "<h1>Halló, " + user['username'] + "!</h1>"


if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  # This will allow the app to display a proper Python error message, so you can fix the typo/syntax error.


   
