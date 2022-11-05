from flask import Flask, json
app = Flask(__name__)

# Hýsum JSON skrá á Github.
# Gists: https://miguelpiedrafita.com/articles/github-gists (max 60 request pr klst nema notað sé token). 
# Vistaðu skránna með .JSON sniðmáti.
# veldu `raw` og afritaðu vefslóð (url) og bættu við .json við endingu 

with open("https://gist.githubusercontent.com/GunnarThorunnarson/13839d272efae357adc1edbcd91f2938/raw/5faf23d220437b74adc73a94ba3edd2a0e01a8c2/nemendur.json", encoding='utf-8') as skra:
    gogn = json.load(skra) # sækjum data úr Json skrá

# Prentum nafnið Þórður, gogn = dictionary 
print(gogn["nemendur"][0]["nafn"])

@app.route('/')
def index():
    return gogn["nemendur"][0]["nafn"] # Þórður

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  
