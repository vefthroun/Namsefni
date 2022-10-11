from flask import Flask, render_template, request, make_response
app = Flask(__name__)

# búum til cookie
@app.route("/")
def index():
    resp = make_response(render_template("3.html"))  # notum template
   
    # búum til cookies
    resp.set_cookie("type", "choclate chip")
    resp.set_cookie("chocolate type", "dark")
    resp.set_cookie("chewy", "yes")
    # að eyða cookie þá  resp.set_cookie('username', expires=0)   
    
    return resp     # skilum template cookies.html

# sækjum cookies
@app.route("/cookies")
def cookies():
    # We use request.cookies to access the cookies
    cookies = request.cookies
    
    # cookies is a serialized Python dictionary 
    print(request.cookies)  # ImmutableMultiDict([('chocolate type', 'dark'), ('chewy', 'yes'), ('type', 'choclate chip')])
   
    flavor = cookies.get("type")  # sækjum úr cookie gildi með key
    print(flavor)   # 'chocolate chip'

    return "Tegund: " + flavor + " smákaka."     # template væri snyrtilegra.


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)

# https://pythonbasics.org/flask-cookies/

"""
Opnaðu Developer tools í vafra og veldu Application (chrome). 

1. Prófaðu að nota refresh í vafra og sjáðu hvað gerist á http://127.0.0.1:5000/cookies
2. Prófaðu að opna annan vafrategund með sömu slóð http://127.0.0.1:5000/cookies og sjáðu hvað gerist.
3. lokaðu vafranum alveg (ekki bara tab/glugga) og opnaðu aftur http://127.0.0.1:5000/cookies , hvað gerist?
"""
