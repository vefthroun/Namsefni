[Firebase](https://firebase.google.com/) er platform þróað af Google til að búa til vef- og símaöpp.
Firebase býður uppá [Realtime Database](https://firebase.google.com/docs/database?authuser=0) en með slíkan gagnagrunn getum við í rauntíma framkvæmt CRUD aðgerðir þ.e. að lesa, skrifa, eyða eða uppfæra gögn í gagnagrunn.

## Skjáfyrirlestrar 

#### Firebase gagnagrunnur

1. [Firebase kynning](https://youtu.be/U5aeM5dvUpA).
1. [Að búa til Firebase gagnagrunn (10 mín)](https://youtu.be/6c27DhyWfQI)

##### Firebase Python: Authentication, Storage, Realtime Database CRUD tutorials

1. [Firebase Python: Authentication, Storage, Realtime Database CRUD tutorials](https://www.youtube.com/watch?v=s-Ga8c3toVY&t=1348s)
   - 00:00:00 - Introduction
   - 00:01:00 - Installing Pyrebase + Connecting to Firebase
   - 00:07:28 - Authentication
   - 00:18:28 - Firebase Storage
   - 00:30:08 - Firebase Realtime Database: Introduction, Structure, Data Types
   - 00:34:40 - Realtime Database CRUD: Create
   - 00:41:28 - Realtime Database CRUD: Update
   - 00:48:43 - Realtime Database CRUD: Delete
   - 00:52:30 - Realtime Database CRUD: Read
   - 01:04:30 - Realtime Database CRUD: Query
   - [Flask kóði með FB authentication](https://github.com/vefthroun/Namsefni/blob/main/6-Gagnagrunnur/Firebase/Authenticate/2_auth_flask.py)
   
##### Realtime Database

1. [Flask app tenging við Firebase gagnagrunn og að skrifa/lesa upplýsingar (13 mín)](https://youtu.be/NDCar59xGRI)
   - [kóðaskráin í videoinu](https://github.com/vefthroun/Namsefni/blob/main/6-Gagnagrunnur/Firebase/app.py)
   - í sýndarumhverfi (virtual env) þarf að sækja: `pip install pyrebase4`
   - Það þarf einnig að bæta við í `config` heitið á gagnagrunninum:<br> `"databaseURL": "https://nafnágagnagrunni.firebaseio.com"`
1. [html form og Firebase gagnagrunnur (14 mín)](https://youtu.be/wyWal1sG6Ms)
1. [Að sækja gögn úr Firebase gagnagrunn og setja í lista (14 mín)](https://youtu.be/64ocVeKm194)

---
#### Tutorials (vefgreinar)

- [Login með auth()](https://parasmani300.medium.com/pyrebase-firebase-in-flask-d249a065e0df)
- [Pyrebase4 viðbótin og aðgerðir](https://github.com/nhorvath/Pyrebase4#database)
   - sýndarumhverfi (venv): `pip install pyrebase4`
- [How to parse Pyrebase OrderedDict](https://stackoverflow.com/questions/51976401/how-to-parse-pyrebase-ordereddict/51989082)
- [tuples](https://realpython.com/python-lists-tuples/#python-tuples)
