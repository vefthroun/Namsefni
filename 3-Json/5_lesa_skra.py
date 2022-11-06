import json

# Opnum JSON skránna 5.json verður að vera til
with open("5.json", encoding='utf-8') as skra:
    gogn = json.load(skra) # sækjum data úr Json skrá

# Prentum nafnið Þórður, gogn = dictionary 
print(gogn["nemandi"][0]["nafn"])
