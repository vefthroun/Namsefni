## Firebase
[Firebase](https://firebase.google.com/) er platform þróað af Google til að búa til vef- og símaöpp.
Firebase býður uppá [Realtime Database](https://firebase.google.com/docs/database?authuser=0) hýstan í skýinu en með slíkan gagnagrunn sem er settu upp sem JSON tré getum við í rauntíma framkvæmt NoSQL CRUD aðgerðir þ.e. að lesa, skrifa, eyða eða uppfæra gögn. 

- [Introducing Firebase Realtime Database](https://youtu.be/U5aeM5dvUpA)
- _Ítarefni: [What is a NoSQL Database?](https://www.youtube.com/watch?v=v_hR4K4auoQ&ab_channel=Firebase) Realtime DB og Firestore DB_

---

### Að búa til Firebase Realtime Database.

[Getting started](https://www.youtube.com/watch?v=pP7quzFmWBY&ab_channel=Firebase) _að 3:13 mín_

1. Búðu til aðgang hjá Google.
1. Veldur Get Started -> Add Project -> Slepptu Google Analytic 
1. Veldu Web app -> Build -> Realtime Database. Ekki velja Firestore Database, hér er [samanburður](https://firebase.google.com/docs/database/rtdb-vs-firestore)
   1. Start in test mode: Þegar þú ert að prófa þig áfram í 30 daga. Hver sem er getur lesið og eytt gögnum úr gagnagrunni.
   1. Start in locked mode: Gögn eru örugg, read/write með security rules.
1. Tannhjól (valmynd efst vinstra megin á skjá) -> Project Settings -> scroll neðst -> Config -> afrita info úr firebaseConfig til að tengjast gagnagrunni (tómur).

---

### Firebase Realtime Databas með Pyrebase 4 

1. [Pyrebase4](https://github.com/nhorvath/Pyrebase4#database)  
1. [Flask app tenging við Firebase gagnagrunn og skrifa/lesa](https://youtu.be/NDCar59xGRI) _(13 mín)_
   - [kóðaskráin í videoinu](https://github.com/vefthroun/Namsefni/blob/main/6-Gagnagrunnur/Firebase/app.py)
   - í sýndarumhverfi (virtual env) þarf að sækja: `pip install pyrebase4`
   - Það þarf einnig að bæta við í `config` heitið á gagnagrunninum:  `"databaseURL": "https://nafnágagnagrunni.firebaseio.com"`

<!-- 
Úrelt: 
1. [Búa til tóman gagnagrunn](https://youtu.be/6c27DhyWfQI)
1. [html form og Firebase gagnagrunnur (14 mín)](https://youtu.be/wyWal1sG6Ms)
1. [Að sækja gögn úr Firebase gagnagrunn og setja í lista (14 mín)](https://youtu.be/64ocVeKm194)

-->

---

### Firebase Python: _Authentication, Storage, Realtime Database CRUD tutorial_

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

---

### Tutorials (vefgreinar)

- [Login með auth()](https://parasmani300.medium.com/pyrebase-firebase-in-flask-d249a065e0df)
- [How to parse Pyrebase OrderedDict](https://stackoverflow.com/questions/51976401/how-to-parse-pyrebase-ordereddict/51989082)
- [tuples](https://realpython.com/python-lists-tuples/#python-tuples)
- [Getting Started with Cloud Firestore with Python](https://www.youtube.com/watch?v=yylnC3dr_no&ab_channel=Firebase)
   - _Admin SDK read/write to Firestore DB: notar server side kóða til að sækja quotes frá REST API og skrifa í gagnagrunn, líka senda notification til notendur_ 
- [How to Get Started with Firebase Using Python](https://www.freecodecamp.org/news/how-to-get-started-with-firebase-using-python/) _CRUD með Admin Database API_ 
