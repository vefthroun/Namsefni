import json

"""
with statement
with is a tool for properly managing external resources (like files) in your program.
Nánar: https://realpython.com/python-with-statement/#using-the-python-with-statement
"""

# Opnum skránna 5.json (JSON skrá verður að vera til)
# It is highly recommended to specify the encoding type when working with files in text mode. 
with open("5.json", mode="r", encoding='utf-8') as skra:
    gogn = json.load(skra) # sækjum data úr Json skrá

# Prentum gogn = dictionary 
#print(gogn["nemandi"])

# Prentum nafnið Þórður
print(gogn["nemandi"][0]["nafn"])
