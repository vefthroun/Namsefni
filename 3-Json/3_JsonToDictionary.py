import json

    # To change string to JSON
    # Take the following string containing JSON data:
    json_string = '{"first_name": "Guido", "last_name":"Rossum"}'

    # It can be parsed like this:
    parsed_json = json.loads(json_string)

    # and can now be used as a normal dictionary:
    print(parsed_json)
