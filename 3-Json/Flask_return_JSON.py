from flask import Flask, json
app = Flask(__name__)

# Hægt er að skila dictionary án þess að þurfa að breyta í JSON í Flask
# FLASK sér um að breyta dictionary í JSON sjálfvirkt.

# Parsing JSON
@app.route('/')
def index():

    # dictionary
    data = {
        'first_name': 'Guido',
        'second_name': 'Rossum',
        'titles': ['BDFL', 'Developer']
    }

    # skilum JSON
    return data 
    # skoðaðu skrá í vafra, prófaðu hægri smella og velja "view page source"

app.run(debug=True)
