
# https://github.com/nhorvath/Pyrebase4
import pyrebase     # pip3 install pyrebase4 

# stillingar til að tengjast firebase realtime database á firebase.google.com 
firebaseConfig = { ... }

# init app með tengingu við gagnagrunn 
firebase=pyrebase.initialize_app(firebaseConfig)

# database
db=firebase.database()

# búa til gögn fyrir gagnagrunn
data1 = {"age": 40, "address": "Tækniskólinn", "employed": True, "name": "Daníel"}
data2 = {"age": 35, "address": "Tækniskólinn", "employed": True, "name": "Gunnar"}
data3 = {"age": 50, "address": "Tækniskólinn", "employed": True, "name": "Konráð"}



# Write

# Þetta kemur samt ekki í veg fyrir duplicate data, þar sem einkvæmur lykill er auto generated
db.child("teachers").push(data1)
db.child("teachers").push(data2)

# að skrifa gögn með einkvæmnum lykli (konni) sem ég bý til (ekki auto generated).
db.child("teachers").child("konni").set(data3) 
# ef ég keyri þessa aðgerð aftur, þá eru gögn yfirskrifuð.



# Update
# update býr til ný eigindi ef það er ekki til fyrir. 

# Update, vísa í þekkt key (konni) og uppfærum aldur
db.child("teachers").child("konni").update({"age": 60})

# Til að velja ákveðinn kennara (Gunnar) með einkvæman lykil sem ég þekki ekki
kennarar = db.child("teachers").get() # sækjum alla kennara
for kennari in kennarar.each():
    if kennari.val()["name"] == "Gunnar":
        # uppfærum aldurinn á Gunnari 
        db.child("teachers").child(kennari.key()).update({"age":45})
        print(kennari.key()) # fæ einkvæman lykil
        print(kennari.val()) # fæ dictionary 


	
# Delete

# fjarlægja eigindi, aldur hja Konna með þekkt key
db.child("teachers").child("konni").child("age").remove()
# fjarlægja node, Konni með þekkt key
db.child("teachers").child("konni").remove()




# Read 

# Að sækja alla kennara frá gagnagrunni
kennarar = db.child("teachers").get().val()   # fáum raðað dictionary 

# Að sækja einn kennara
kennari = db.child("teachers").child("konni").get()    # eða db.child("teachers").child("-NHLOClVYBga-ZqVCA8L").get()
print(kennari.val())  # fæ Ordered dict með lista af tuples
# OrderedDict([('address', 'Tækniskólinn'), ('age', 60), ('employed', True), ('name', 'Konráð')])

# Við gætum þá breytt þessu í dictionary sem inniheldur dictionaries
kennarar = dict(db.child("teachers").get().val())   # typecast
print(kennarar)
# {'-NHLOCke9NpiVrkjSlrA': {'address': 'Tækniskólinn', 'age': 40, 'employed': True, 'name': 'Daníel'}, '-NHLOClVYBga-ZqVCA8L': {'address': 'Tækniskólinn', 'age': 45, 'employed': True, 'name': 'Gunnar'}, 'konni': {'address': 'Tækniskólinn', 'age': 60, 'employed': True, 'name': 'Konráð'}}

# Eða listi með tuples
kennari = db.child("teachers").child("konni").get().val()
kennaralisti = list(kennari.items())  # breytum í lista með tuples
print(kennaralisti) # [('address', 'Tækniskólinn'), ('age', 60), ('employed', True), ('name', 'Konráð')]




# Condtitional Requests
# Pyrebase:  https://github.com/nhorvath/Pyrebase4#conditional-requests

# Í Rules: bætum við field til að geta gert skilyrtar fyrirspurnir 
# "teachers" : { ".indexOn" : ["address","age","employed","name"] }

# Ég vil sækja nafnið Daníel
results = db.child("teachers").order_by_child("name").equal_to("Daníel").get()
print(results.val()) # OrderedDict([('-NHLOCke9NpiVrkjSlrA', {'address': 'Tækniskólinn', 'age': 40, 'employed': True, 'name': 'Daníel'})])

# til að fá dictionary (gætum líka fengið fleiri en eina niðurstöðu)
for kennari in results.each():
    print(kennari.val())        # {'address': 'Tækniskólinn', 'age': 40, 'employed': True, 'name': 'Daníel'}
    print(kennari.val()["age"]) # 40

# Sækjum alla kennara sem eru 45 ára og eldri, age er heiltala (int)
results = db.child("teachers").order_by_child("age").start_at(45).get()
for kennari in results.each():
    print(kennari.val()["name"])   # Gunnar, Konráð
