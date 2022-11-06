import json

# dictionary
d = {
        'first_name': 'Guido',
        'second_name': 'Rossum',
        'titles': ['BDFL', 'Developer']
}

# convert dictionary to JSON (string containing JSON)
# dumps fyrir strengi, dump fyrir skrár
json_string_data = json.dumps(d) 

# '{"first_name": "Guido", "last_name": "Rossum", "titles": ["BDFL", "Developer"]}'
print(json_string_data)
