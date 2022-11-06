import json

# dictionary
d = {
        'first_name': 'Guido',
        'second_name': 'Rossum',
        'titles': ['BDFL', 'Developer']
}

# convert dictionary to JSON (string containing JSON)
# dumps fyrir strengi, dump fyrir skrár
json_string = json.dumps(d) 

# '{"first_name": "Guido", "last_name": "Rossum", "titles": ["BDFL", "Developer"]}'
print(json_string)

# json.dumps(x, indent=2)  læsilegra í terminal með print() skipun
