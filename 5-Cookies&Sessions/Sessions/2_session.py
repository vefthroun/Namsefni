from flask import Flask, render_template, request, session, redirect, url_for

# https://pythonbasics.org/flask-sessions/

app = Flask(__name__)

app.config["SECRET_KEY"] = "OCML3BRawWEUeaxcuKHLpw"

"""
Secret key

- The session object requires your app to have a value set for the SECRET_KEY variable
- app.config["SECRET_KEY"] = "something secret"  

    import os
    # Koma í veg fyrir cross site request forgery (CSRF) attacks. Að cookies séu breytt 
    
    app.config["SECRET_KEY"] = ""
    
    # búum til einkvæma runu. 
    app.secret_key = os.urandom(8)  
    
    # Önnur leið;  import secrets og secrets.token_hex(16)  
    print(app.secret_key)

"""

users = {
    "julian": {
        "username": "julian",
        "email": "julian@gmail.com",
        "password": "example",
        "bio": "Some guy from the internet"
    },
    "clarissa": {
        "username": "clarissa",
        "email": "clarissa@icloud.com",
        "password": "sweetpotato22",
        "bio": "Sweet potato is life"
    }
}

@app.route("/")
@app.route("/sign-in", methods=["GET", "POST"])
def sign_in():

    if request.method == "POST":

        req = request.form

        username = req.get("username")
        password = req.get("password")

        if not username in users:
            print("Username not found")
            return redirect(request.url)
        else:
            user = users[username]  # user = dictionary

        if not password == user["password"]:
            print("Incorrect password")
            return redirect(request.url)

        else:
            # búum ti session
            session["USERNAME"] = user["username"]
            print(session)
            return redirect(url_for("profile"))

    return render_template("sign_in.html")


@app.route("/profile")
def profile():

    if not session.get("USERNAME") is None:
        username = session.get("USERNAME")
        user = users[username]  # dictionary
        return render_template("profile.html", user=user)
    else:
        print("No username found in session")
        return redirect(url_for("sign_in"))

# Eyða session
@app.route("/sign-out")
def sign_out():
    session.pop("USERNAME", None)
    return redirect(url_for("sign_in"))


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
