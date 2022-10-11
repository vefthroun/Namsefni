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
