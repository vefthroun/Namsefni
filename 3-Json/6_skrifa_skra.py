# python sýnidæmi (Flask ekki notað)
import json

# Skilgreinum breytuna bekkur sem geymir dict (json hlut)
bekkur = {
    'nemandi':[
      {'nafn':'Daniel','braut':'tbr13'},
      {'nafn':'Hilmir','braut':'tbr16'}
    ]
}

# Skoðum innihald bekkur breytunnar - debug
print(bekkur)

# Lúppum i gegnum "allann bekkinn"

# dict key value 'nemandi' inniheldur lista
for i in bekkur['nemandi']:
    print("Nafn :", i['nafn'])# hver i er i raun gildi í listanum 'nemandi', getum hér notað key value 'nafn'

# auð lína
print()

# Bætum við nemandi..
bekkur['nemandi'].append({'nafn':'Alex','braut':'tbr19'})

# Prentum aftur lista með nýjum nemanda
for i in bekkur['nemandi']:
    print("Nafn :", i['nafn'])

# Skrifum i skrána bekkur.json, ef hún er ekki til þá er hún bil til sjálfkrafa.
with open("6.json","w") as skra:
    # dump er fyrir skrár, dumps fyrir strengi
    json.dump(bekkur, skra)
    skra.close() 
