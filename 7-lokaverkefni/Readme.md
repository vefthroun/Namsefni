## Nokkur mikilvæg atriði varðandi lokaverkefnið.

* Verkefnið er lykilmatsverkefni, lágmarkseinkunn til að ná er 4.
* Verkefnavinnan stendur í rétt um 2 vikur, tíminn líður hratt.
* Byrjaðu strax.
* Lestu vandlega verklýsingu.
* Byrjaðu á að útfæra lágmarkskröfur til að ná 4.
* Þegar þú hefur náð lágmarks kröfum bætiru 1 við einkunnina þína með meiri útfærslum ( sjá verklýsingu Námsmat -> einkunn 0-10 )
* Atriðin / úrfærslurnar hér fyrir neðan eru frá einkunn 8 og upp í 10.
* Gangi þér vel.  


### Upload á Firebase Storage

Firebase býður upp á þjónustuna Storage til að hýsa myndir, hljóðskrár, video og aðrar skrár.  Skránum er hægt að "uploada" og "downloada" til of frá geymslunni í gegnum Python Flask.

Firebase Storage is a stand-alone solution for uploading user generated content like images and videos from an iOS and Android device, as well as the Web. In typical Firebase fashion, there's no server required. Firebase Storage is designed specifically for scale, security, and network resiliency.

* [Python Flask Upload to Storage](https://github.com/kanuarj/FirebasePython/blob/master/Storage/app.py) _kóðadæmi_
* [Python + Firebase Cloud Storage - Upload/Download Files | Pyrebase](https://www.youtube.com/watch?v=I1eskLk0exg) _myndband_

---

### Upload á server (eða á pythonanywhere)

Mjög einfalt að Upload-a skrá með Python Flask. Ef þú ætlar að uploada t.d. mynd inn á pythonanywhere svæðið þitt í t.d. möppuna static þarftu að stilla UPLOAD_FOLDER rétt.  <br>
``` app.config['UPLOAD_FOLDER'] = "/home/þittnotendanafn/mysite/static" ``` <br>
ef þú ert með möppuna static undir mysite möpunni ( mysite er default mappa )
 
* [Flask-File-Upload](https://github.com/arpanneupane19/Flask-File-Uploads/blob/main/main.py) _kóðadæmi_
* [How to Upload Files with Flask Using Python (Með WTForms)](https://www.youtube.com/watch?v=GeiUTkSAJPs) _myndband_

---

<!--
### Paginate. 

* Ef vefsíða er að birta mikið af gögnum ( tweet / blog / ... ) getur verið þreytandi að scrolla niður alla síðuna til að finna réttu gögnin.  *Paginate* er leið til að brjóta gögnin niður í minni einingar og birta færri færlsur á hverri síðu en dreifa svo gögnunum á fleiri síður.  Tilheyrandi flipar birtast til að birta mismunandi síður...



* [Python 3 Flask Bootstrap 4 Pagination Example to Paginate Array of Users Using flask-paginate](https://www.youtube.com/watch?v=vt0OXl2WCGI) _myndband_
* [Flask-paginate](https://flask-paginate.readthedocs.io/en/master/)
* [What is pagination](https://www.techtarget.com/whatis/definition/pagination)

---
-->

### Deployment og hýsing á [pythonanywhere](https://www.pythonanywhere.com/). 

PythonAnywhere is an online integrated development environment and web hosting service based on the Python programming language. Founded by Giles Thomas and Robert Smithson in 2012, it provides in-browser access to server-based Python and Bash command-line interfaces, along with a code editor with syntax highlighting (Wikipedia). <br>
Verðum að gera ``` pip install pyrebase4 ``` í Bash console inn á pythonanywhere þjóninum.


* [How to deploy a Python (Flask) web app on a (PythonAnywhere) live server](https://www.youtube.com/watch?v=75-oCKUx3oU) _myndband_


<!--

## Undirbúningur

Viðfangsefni lokaverkefnisins er frjálst en það þýðir ekki að það eigi að vera skipulagslaust og innihald eintómt bull (_dummy texti_). Við eigum að nota allt sem við höfum lært í vefhönnun sem að gagni getur komið í lokaverkefninu.

### Viðfangsefni

Lýsið í stuttu máli um hvað lokaverkefnið er í **Verkefni 7, README.md** skránni.

Hér er dæmi um umfjöllunarefni (_xyz er ykkar val_)

> Lokaverkefnið er bloggsíða sem fjallar um **XYZ**. Á forsíðu eru greinar um **XYZ** sem allir geta lesið og eru skráðar af ritstjóra. Á undirsíðu eru upplýsingar sem fengnar eru frá **XYZ API**. Það er hægt að skrá sig inn á spjallrás þar sem notendur geta spjallað saman um **XYZ**. Ekki er hægt að komast á spjallrásina nema innskráðir notendur.

### Veftré (_Site map_)

Búið til veftré sem lýsir skipulagi og virkni sem á að vera í vefnum. Það getur verið í textasniði og skráð eins og hér er sýnt.

```
    index ('/') innihald kemur úr (xyz) gagnagrunni 
    |
    |_ Um XYZ ('/about') innihald kemur úr (xyz) API endpoint
    |
    |_ Innskráning ('/login') - _Firebase authentication_
    |   |_ spjallrás ('/blog') lokuð með _session_
    |   |   |_ skrifað í fb gagnagrunn ('/write')
    |   |   |_ breyta grein í fb gagnagrunn ('/update')
    |   |   |_ eyða grein í fb gagnagrunn ('/delete')
    |   |   |_ útskráning (session log out)
    |   |_ innskráning mistókst ('/login_error')
    |
    |_ Nýskráning ('/register')- _Firebase authentication_
        |_ nýskráning tókst ('/register_ok')  
        |   |_ skráðu þig á spjallrásina ('/login')
        |_ nýskráning mistókst ('/register_error')

```

### Gagnagrunnur

Notendur sem skráðir eru inn með _Firebase Authentication_ geta skrifað í gagnagrunnstöfluna _Póstar_. Notendur eiga að geta skrifað pistla og leiðrétt pistlana sína. Þeir birtast í spjallrásinni. Notendur eiga að geta eytt sínum pistlum.

#### Póstar (tafla)
1. Hver skráning fær sér ID (KEY node)
1. Fyrirsögn (skráð í input)
1. Pistill (skráður í textarea)
1. Höfundur (skráður í input)
1. Dagsetning (sjálfvirk - _timestamp_)

### Niðurstaða 

Lýsið í stuttu máli hvað gekk vel að leysa og hvað vantar upp á að verkefnaáætlunin hafi staðist í **Verkefni 7, README.md**. 

-->
