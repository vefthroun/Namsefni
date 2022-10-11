from flask import Flask, render_template, request
app = Flask(__name__)

# https://www.tutorialspoint.com/flask/flask_sending_form_data_to_template.htm

# signup
@app.route("/")
@app.route("/signup")
def login():
        return render_template("signup.html")

# formvinnsla
@app.route("/signup_process", methods = ['POST', 'GET'])
def result():
        if request.method == 'POST':
            # sækjum streng/gildi úr name breytum frá formi 
            result = request.form  # request.form skilar dictionary 
        return render_template("signup_result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
