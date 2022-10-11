from flask import Flask, render_template, request, make_response
app = Flask(__name__)


# let's set a cookie with the key of flavor and the value of chocolate chip:
@app.route("/")
@app.route("/cookies")
def cookies():

    # By using make_response() we can build and modify our request ahead of sending it.
    resp = make_response("Cookies 2")
    
    # búum til cookie og bætum við resp object.
    # request.path to access the path of the current route
    # flavor cookie now has an Expires on date along with a value for Path of /cookies.
    resp.set_cookie(
        "flavor2", 
        value="chocolate chip",
        max_age=10
    )

    # skilar "Cookies" streng
    return resp

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)

# https://pythonbasics.org/flask-cookies/

"""
Cookies eru í vaframinni 
1. Opnaðu Developer tools í vafra og veldu Application (chrome). 
2. Smelltu á Cookies og skoðaðu upplýsingarnar. 
3. Hinkraðu í 10 sekúnudur, flavor eyðist þá.

"""
