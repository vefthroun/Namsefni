import json

# dictinary (json hlut)
bekkur = {
    'nemandi':[
      {'nafn':'Daniel','braut':'tbr13'},
      {'nafn':'Hilmir','braut':'tbr16'}
    ]
}

# debug
print(bekkur) 

# Bætum við nemanda í listann, dict. færslu 
bekkur['nemandi'].append({'nafn':'Alex','braut':'tbr19'})

# key 'nemandi' er listi með dictionaries.
for i in bekkur['nemandi']:
    print("Nafn :", i['nafn'])

# Skrifum (yfirskrifum) i skránna bekkur.json. Ef hún er ekki til þá er búin til sjálfkrafa.
with open("bekkur.json","w") as skra:
    # dump er fyrir skrár, dumps fyrir strengi
    json.dump(bekkur, skra)
    skra.close() 
