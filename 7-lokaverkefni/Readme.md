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
