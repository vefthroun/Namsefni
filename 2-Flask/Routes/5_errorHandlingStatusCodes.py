
# import Flask class in Python
from flask import Flask

# Create app, that hosts the application
app = Flask(__name__)

"""
Errors and status codes:
If you want to customize the error page, you can use the errorhandler() decorator:
https://flask.palletsprojects.com/en/2.1.x/quickstart/#redirects-and-errors

By default 200 is assumed which translates to: all went well.
"""

@app.route('/')
def index():
    return 'Halló heimur!'

# Client error
# Note the 404 after the render_template() call. 
# This tells Flask that the status code of that page should be 404 which means not found. 
@app.errorhandler(404)
def pagenotfound(error):
    return "Sorry, page not found!", 404

# Server error
@app.errorhandler(500)
def servernotfound(error):
    return "Server is down!", 500

# This starts the we
# b app 
if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  

# Keyrðu python skránna og prófaðu undirsíðu t.d. http://127.0.0.1:5000/test

   
