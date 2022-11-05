from flask import Flask, json
app = Flask(__name__)

# Tengjumst við skránna 5.json (verður að vera til) sem við hýsum á Github 
with open("slóðáskrá.json", encoding='utf-8') as skra:
    gogn = json.load(skra) # sækjum data úr Json skrá

# Prentum nafnið Gunnar, gogn = dictionary 
print(gogn["nemandi"][0]["nafn"])

@app.route('/')
def index():
    return gogn["nemandi"][0]["nafn"] # Þórður

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  
