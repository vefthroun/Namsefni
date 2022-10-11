
from flask import Flask, redirect

# Create app, that hosts the application
app = Flask(__name__)

"""
Redirects
https://flask.palletsprojects.com/en/2.1.x/quickstart/#redirects-and-errors

"""

# To redirect a user to another endpoint, use the redirect() function. 
@app.route('/admin')
def admin():
    # logic, ex. user and password
    return redirect("/login")

# Signup page
@app.route('/login')
def login():
    return 'login form'


# This starts the web app 
if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  


   
