# Parse JSON from url 
import json
import urllib.request

# download raw json object
url = "https://api.gdax.com/products/BTC-EUR/ticker"
data = urllib.request.urlopen(url).read().decode()

# parse json object
obj = json.loads(data)

# output some object attributes
print('$ ' + obj['price'])
print('$ ' + obj['volume'])


"""
# Annað dæmi
# Parse JSON from url
import urllib.request, json
with urllib.request.urlopen('https://apis.is/currency/') as response:
   data = json.loads(response.read().decode())
   
print(data) # dictionary
"""
