from flask import Flask
app = Flask(__name__)

"""
Static files. 
https://flask.palletsprojects.com/en/2.1.x/quickstart/#static-files

Búðu til möppuna static við hlið kóðaskránum þínum og notaðu /static sem vísun í html.
Í static möppu geymir þú gögn einsog CSS skrár, JavaScript, myndir og aðrar "binary" skrár.

Ideally your web server is configured to serve them for you, but during development Flask can do that as well. 
Just create a folder called static next to your module and it will be available at /static on the application.
"""

@app.route('/')
def index():
   return '''
            <!DOCTYPE html>
            <html>
                <head>
                    <title>Hello world</title>
                    <meta charset="utf-8">
                    <!-- style.css skráin er í static möppu -->
                    <link rel="stylesheet" href="/static/styles.css">
                </head>
                <body>
                    <h1>Halló heimur í bláum lit með CSS!</h1>
                    <!-- myndin er í static möppu -->
                    <img src="/static/Flask.png" alt="Flask logo">
                </body>
            </html>
        '''

# This starts the web app 
if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  

