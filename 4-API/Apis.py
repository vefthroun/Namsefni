from flask import Flask, render_template, json
import urllib.request  # til að ná í json skrár á internetinu

app = Flask(__name__)

# Sækjum gengi
with urllib.request.urlopen("https://apis.is/currency/") as url:
    data = json.loads(url.read().decode())
print (data)

@app.route('/')
def currency():
    return render_template('gengi.html', data=data)

if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)

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
