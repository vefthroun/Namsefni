
# data er dictionary sem inniheldur listann results
# results listi inniheldur  mismunandi gengisupplýsingar í dictionary gagnasniði
# data inniheldur þrjú gengi.
data = {
	'results': [{
		'shortName': 'ISK',
		'longName': 'Íslensk króna',
		'value': 130,
		'askValue': 1,
		'bidValue': 1,
		'changeCur': 0,
		'changePer': '0.00'
	},{
		'shortName': 'USD',
		'longName': 'Bandarískur dalur',
		'value': 130,
		'askValue': 130.89,
		'bidValue': 129.98,
		'changeCur': 0.360374,
		'changePer': '0.00'
	},{
		'shortName': 'USD',
		'longName': 'Bandarískur dalur',
		'value': 130,
		'askValue': 130.89,
		'bidValue': 129.98,
		'changeCur': 0.360374,
		'changePer': '0.00'
	},
	{
		'shortName': '',
		'longName': 'Pund',
		'value': 181,
		'askValue': 181.20,
		'bidValue': 180.92,
		'changeCur': 0.4123,
		'changePer': '0.00'
	}]
}
# print(data["results"])  		# listi
# print(data["results"][0]) 	# fyrsta stak (dictionary) í lista
# print(data["results"][1]) 	# annað stak (dictionary) í lista
# print(data["results"][0]["shortName"])  	# ISK gildið sem shortName (Key) vísar á í dictionary
# print(data["results"][0].shortName) 		# virkar í Jinja template en ekki í python, auðvelt að ruglast


# -------------------------------------------------------------
# Sýnidæmi með lista, dictionary, for in lykkju og if setningu.
# -------------------------------------------------------------

# Sýnidæmi 1
"""
# data["results"] er listi
for item in data["results"]:
	print(item['longName'])  
		# Íslensk króna
		# Bandarískur dalur
		# Bandarískur dalur
		# Pund
"""

# Sýnidæmi 2
"""
gengi = [] 
for item in data["results"]:
	if item["shortName"] is not None:  # True if empty string, empty list, equals to zero. “None” is Python’s name for a null reference.
		gengi.append(item["shortName"])  # bætum við í listann gengi

print(gengi) # ['ISK', 'USD', 'USD', '']
# if item["shortName"]: # ['ISK', 'USD', 'USD']
"""

# Sýnidæmi 3
"""
gengi = [] 
for item in data["results"]:
	if item["shortName"] not in gengi:  # setjum bara einu sinni sömu gengisupplýsingar.
		# bætum við gengisupplýsingum (shortName) í listann sem heitir gengi
		gengi.append(item["shortName"])  
print(gengi)
"""


