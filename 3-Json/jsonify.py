
from flask import Flask, jsonify

app = Flask(__name__)

# listi með dictionary
countries = [
    {"id": 1, "name": "Thailand", "capital": "Bangkok", "area": 513120},
    {"id": 2, "name": "Australia", "capital": "Canberra", "area": 7617930},
    {"id": 3, "name": "Egypt", "capital": "Cairo", "area": 1010408},
]

@app.route('/')
def index():
    # flask.jsonify: https://tedboy.github.io/flask/generated/flask.jsonify.html
    return jsonify(countries) # skilar JSON object

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
    
