
import json, pathlib, logging

# dictinary (json hlut)
bekkur = {
    'nemandi':[
      {'nafn':'Daniel','braut':'tbr13'},
      {'nafn':'Hilmir','braut':'tbr16'}
    ]
}
print(bekkur) # debug

# Bætum við nemanda í listann, dict. færslu 
bekkur['nemandi'].append({'nafn':'Alex','braut':'tbr19'})

# Lúppum i gegnum listann
# key 'nemandi' er listi með dictionaries.
for i in bekkur['nemandi']:
    print("Nafn :", i['nafn'])

# JSON skrá sem við ætlum að skrifa í
file_path = pathlib.Path("bekkur.json")
   
try:
    # Skrifum (yfirskrifum all) i skránna bekkur.json
    # Ef hún er ekki til þá er búin til sjálfkrafa.
    with file_path.open(mode="w") as file:
        # dump er fyrir skrár, dumps fyrir strengi
        json.dump(bekkur, file)
        file.close() 
except OSError as error:
    logging.error("Writing to file %s failed due to: %s", file_path, error)
