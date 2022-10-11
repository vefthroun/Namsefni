
from flask import Flask, json

app = Flask(__name__)


# Parsing JSON
@app.route('/')
def index():

    # To change string to JSON

    # Take the following string containing JSON data:
    json_string = '{"first_name": "Guido", "last_name":"Rossum"}'

    # It can be parsed like this:
    parsed_json = json.loads(json_string)

    # and can now be used as a normal dictionary:
    print(parsed_json)

    return "Full name: " + parsed_json["first_name"] + " " + parsed_json["last_name"]

app.run(debug=True)
