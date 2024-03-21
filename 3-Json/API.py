from flask import Flask, render_template, json
# til að ná í json skrár hýsta á netinu API
# Ef vesen með Mac, ein lausn: Applications Folder -> Python folder, and click on the Install Certificates.command file
import urllib.request  

app = Flask(__name__)

# Sækjum gengi
with urllib.request.urlopen("https://apis.is/currency/arion") as response:
    data = json.loads(response.read())

# læsilegra
print (json.dumps(data, indent=2))
'''
@app.route('/')
def currency():
    return render_template('gengi.html', data=data)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)
'''
"""

# gengi.html
<html>
    <head>       
        <title>APIs sýnidæmi</title>
        <meta charset="utf-8"/>
    </head>
    <body>
        <h1>Gengi gjaldmiðla</h1>
        <div class="col-5">
        {% for item in data['results'] %}
            <p>{{ item['longName'] }} {{ item['shortName'] }}, gengi ISKR: {{ item['value'] }}</p>
        {% endfor %}
        </div>
    </div>
    <p>Apis.is: http://docs.apis.is/#endpoint-currency</p>
    </body>
</html>

"""
