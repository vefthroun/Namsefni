
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
bekkur['nemandi'].append({'nafn':'Jón','braut':'tbr19'})

# Lúppum i gegnum listann
# key 'nemandi' er listi með dictionaries.
for i in bekkur['nemandi']:
    print("Nafn :", i['nafn'])

# JSON skrá 
file_path = pathlib.Path("bekkur.json")
   
try:
    # Skrifum (yfirskrifum) i skránna bekkur.json
    # Ef hún er ekki til þá er búin til sjálfkrafa.
    with file_path.open(mode="w") as file:
        # dump er fyrir skrár, dumps fyrir strengi
        json.dump(bekkur, file)
        file.close() 
except OSError as error:
    logging.error("Writing to file %s failed due to: %s", file_path, error)

"""
pathlib.Path is a class that represents concrete paths to physical files in your computer. 
Calling .open() on a Path object that points to a physical file opens it just like open() would do. 
So, Path.open() works similarly to open(), but the file path is automatically provided by the Path object you call the method on.

logging
Check for possible issues, such as a missing file, writing and reading access.
"""
