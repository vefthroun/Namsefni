import json

"""
with statement
with is a tool for properly managing external resources (like files) in your program.
It requires both a setup phase and a teardown phase. 
The teardown phase requires you to perform some cleanup actions, such as closing a file or closing a network connection. 
If you forget to perform these cleanup actions, then your application keeps the resource alive. 
This might compromise valuable system resources, such as memory and network bandwidth.

Nánar hér: https://realpython.com/python-with-statement/#using-the-python-with-statement
"""

# Opnum JSON skránna 5.json (skrá verður að vera til)
with open("5.json", encoding='utf-8') as skra:
    gogn = json.load(skra) # sækjum data úr Json skrá

# Prentum nafnið Þórður, gogn = dictionary 
print(gogn["nemandi"][0]["nafn"])
