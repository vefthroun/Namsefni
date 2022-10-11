from flask import Flask, render_template, request, make_response
app = Flask(__name__)


# let's set a cookie with the key of flavor and the value of chocolate chip:
@app.route("/")
@app.route("/cookies")
def cookies():

    # By using make_response() we can build and modify our request ahead of sending it.
    resp = make_response("Cookies")
    
    # búum til cookie flavor (key) sem geymir streng (value), og bætum við resp object.
    resp.set_cookie("flavor", "chocolate chip")
    
    # skilar "Cookies" streng
    return resp

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)

# https://pythonbasics.org/flask-cookies/

"""
Cookies eru í vaframinni 
1. Opnaðu Developer tools í vafra og veldu Application (chrome). 
2. Smelltu á Cookies og skoðaðu upplýsingarnar. Þú munt finna að flavour (key) inniheldur cookie (gildi)
3. Prófaðu að eyða cookie þar og smelltu á refresh.

"""
