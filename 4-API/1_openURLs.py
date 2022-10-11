# til að ná json skrár yfir netið
import urllib.request

# sækjum source code frá python.org
with urllib.request.urlopen('http://python.org/') as response:
   print(response.read()) # skoðum í terminal
