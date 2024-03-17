import json

json_string = '{"first_name": "Guido", "last_name":"Rossum"}'

parsed_json = json.loads(json_string)

print(parsed_json)


d = {
        'first_name': 'Guido',
        'second_name': 'Rossum',
        'titles': ['BDFL', 'Developer']
}

json_string = json.dumps(d) 

print(json_string)