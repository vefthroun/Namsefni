from flask import Flask
app = Flask(__name__)

@app.route('/demo1')
def demo1():
    # skilum textastreng í vafra
    return "Halló Heimur!"

# You can bind more than one route to a single callback (Chaining Decorators)
@app.route('/')
@app.route('/index')
def demo2():
    return "Halló Heimur!"

# blöndum saman html elementum og texta í streng sem við skilum.
@app.route('/')
@app.route('/index')
def demo3():
    return "<h1>Halló Heimur!</h1>"

# Við getum skilað html vefsíðu sem streng
@app.route('/')
def demo4():
    # breyta sem geymir html í strengjaformi
    html = '''
    <!DOCTYPE html>
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
          <h1>Halló</h1>
          <a href="/sida1">Tengill</a>  <!-- tengill á routið (undirsíða) /sida1 -->
    </body>
    '''
    return html


if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  


   
