### JSON  
[JSON](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON) er opið gagnaskiptasnið sem notar læsilegan texta til að geyma, sækja og senda gagnahluti. 
Uppbygging samanstendur af eigindi (key) og gildi (value) pörum. 
JSON er læsilegt og vinsælt gagnsnið á manna máli. JSON er notað með ýmsum forritunarmálum. [An introduction to JSON](https://towardsdatascience.com/an-introduction-to-json-c9acb464f43e)


#### JSON málskipan
 * key/value parasamband
 * Gögn eru aðgreind með kommu
 * {}, Slaufusvigi eru utan um JSON object og innri objecta 
 * [], hornklofi er utan um fylki/lista
 * key verður að vera með tvöföldum gæsalöppum og vera strengur
 * Ekki hægt að commenta í JSON skrá
 * JSON hefur ekki föll
 * JSON er í formi strengs.
 * JSON skráarsnið er með .json endingu, the MIME type for JSON text is "application/json"
 * Þú getur notað JSONLint til að validate JSON. http://jsonlint.com/ 

---

### JSON með Python 

#### kóðasýnidæmi

1. [JSON syntax](1_JSON_Syntax.json)
1. [JSON sýnidæmi](2_JSON_EXAMPLES.json)
1. [JSON í Dictionary](3_JsonToDictionary.py)
1. [Dictionary í JSON](4_dictionaryToJson.py)
1. [Að lesa úr JSON skrá](5_lesa_skra.py)
1. [Að skrifa í skrá](6_skrifaSkra.py)
1. [Að skrifa í JSON skrá](6_skrifa_Json_skra.py)
1. [Að lesa úr JSON skrá hýst á netinu (Gist)](7_urllib_request.py)
1. [Að vinna úr dictionary sem kemur frá API](8_dictionary_API.py)


#### Bjargir
* [JSON in Python (W3Schools)](https://www.w3schools.com/python/python_json.asp)
* [Reading and writing JSON to a python file](https://www.geeksforgeeks.org/reading-and-writing-json-to-a-file-in-python/)
* [Python's urllib.request for HTTP Requests](https://realpython.com/urllib-request/)
* [Working with JSON](https://www.youtube.com/watch?v=9N6a-VLBa2I) (myndband)
* [Append to JSON file using Python](https://www.geeksforgeeks.org/append-to-json-file-using-python/)

---

### JSON með Flask

#### Kóðasýnidæmi

1. [Að skila JSON](Flask_return_JSON.py)
1. [Að skila JSON með Jsonify](jsonify.py)
1. [Að sækja JSON frá API](API.py)

#### Bjargir

* [JSON Support in Flask](https://tedboy.github.io/flask/interface_api.json_support.html#module-flask.json)
* [flask.jsonify](https://tedboy.github.io/flask/generated/flask.jsonify.html)

---
