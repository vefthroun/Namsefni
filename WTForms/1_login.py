# import Flask class in Python
from flask import Flask, render_template
# wrapper utan um form WTForms
from flask_wtf import FlaskForm
# vinnum beint með WTForms
from wtforms import StringField, PasswordField

# Create app, that hosts the application. Don't worry about that __name__ object, it's just a convention.
app = Flask(__name__)
# direct access to config, til að geta notað WTform þarf secret key.
app.config["SECRET_KEY"] = "Lykill"

# form fyrir login
class LoginForm(FlaskForm):
    username = StringField("username")
    password = PasswordField("password")


@app.route('/form', methods=["GET","POST"])
def form():
    # búum til object (instance of class) til að senda í template
    form = LoginForm()
    
    # athugum hvort búið sé að submit form frá notanda. 
    if form.validate_on_submit():
        # birtum gögn úr forminu.
        return "<p> The username is {}. The password is {} </p>".format(form.username.data, form.password.data)
        # annars skilum tómt form til útfyllingar.
    return render_template("form.html", form=form)  


# This starts the web app 
if __name__ == '__main__':
    # run, starts a built-in development server
    app.run(debug=True, use_reloader=True)   
           

"""

# form.html

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Form</title>
</head>
<body>
    <form method="POST", action="{{ url_for('form') }}">
        <!-- Cross Site Request Forgery protection --> 
        {{ form.csrf_token }}
        {{ form.username.label }}
        {{ form.username }}
        {{ form.password.label }}
        {{ form.password }}
        <input type="submit" value="Submit">
    </form>
</body>
</html>

"""
