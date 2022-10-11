from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/form", methods = ['POST', 'GET'])
def form():
    # birtum formið
    if request.method == 'GET':
        return render_template("form.html")
    
    # formvinnsla 
    if request.method == 'POST':
        # sækjum gildin úr name breytum úr formi  
        kwargs = {
            "title": request.form["title"],
            "isbn": request.form["isbn"],
            "author": request.form["author"],
            "timestamp": request.form["timestamp"]
        }    
        return render_template("form_result.html", **kwargs)
        # *args og **kwargs útskýrt: https://realpython.com/python-kwargs-and-args/

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)

# Working with Forms in Flask (myndband): https://www.youtube.com/watch?v=KW_ItlO5kR4
