from flask import Flask, json

app = Flask(__name__)

# Parsing JSON
@app.route('/')
def index():

    # dictionary
    d = {
        'first_name': 'Guido',
        'second_name': 'Rossum',
        'titles': ['BDFL', 'Developer']
    }

    # convert dictionary to JSON (string containing JSON)
    # dumps fyrir strengi, dump fyrir skrár
    # indent=2 til að fá læsilegt format
    json_string_data = json.dumps(d, indent=2)

    # '{"first_name": "Guido", "last_name": "Rossum", "titles": ["BDFL", "Developer"]}'
    print(json_string_data)

    return json_string_data 
    # skoðaðu skrá í vafra, prófaðu hægri smella og velja "view page source"
app.run(debug=True)

