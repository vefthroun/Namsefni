from flask import Flask

app = Flask(__name__)

"""
Það væri heppilegra að aðskilja gögn betur frá útliti og framsetningu en til þess
þá þurfum við að nota template tungumál eins og t.d. Jinja.

"""

@app.route('/')
@app.route('/index')
def index():

    # dictionary
    user = {'username': 'Gunnar'}

    # erfitt að debugga 
    return '''
    <html>
        <head>
            <title>Verk.2</title>
        </head>
        <body>
            <h1>Halló, ''' + user['username'] + '''!</h1>
        </body>
    </html>'''


# This starts the web app 
if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  
    
# Keyrðu python skránna og skoðaðu url í vafra
