## Verkefni 6

- Lykilmatsþáttur
- 30% af heildareinkunn
- Allt námsefni áfanga undir 

---

### Verkefnalýsing

Útfærðu persónulegan bloggvef með Flask, [sýnidæmi](https://blog-admin-ui.netlify.app/). Efnisval (texti og myndir) er valfrjálst en færslurnar þurfa að vera **10** að lágmarki (ekki bull). Notaðu t.d. Barebones CSS safn og / eða eigið fyrir uppsetningu (layout) og útlit. Gert er ráð fyrir sjálfstæðum vinnubrögðum.  Verkefnið er einstaklingsverkefni.

Efni vefsins má vera annað en nefnt er hér að ofan eins og fréttatengt efni, íþróttir, kvikmyndir eða bara eitthvað tengt áhugamáli.  Sammþykki verður að fá frá kennara samt sem áður.

1. Forsíða: 
    1. birtir alla pistla sem allir geta lesið, nýjasti birtist efst. 
1. Flokkar:
    1. birtir alla pistla í flokki sem allir geta lesið. 
1. Valmynd: 
    1. forsíða, flokkar, admin, innskráning og úskráning.
1. Footer:
    1. inniheldur upplýsingar um höfund verkefnis, skólaupplýsingar (Tölvubraut, Tækniskólinn) og vefslóða á hýsingu vefs.
1. Innskráning:
    1. aðeins admin notandi á að geta skráð sig inn og séð Admin. Notaðu netfangið admin@admin.is og lykilorðið 123456.
    1. Admin notandi getur útskráð sig.
1. Admin. 
    1. yfirlit yfir alla pistla (titill, flokkur, dagsetning) raðað eftir dagsetningum (nýjast efst)
    1. takki til að bæta við pistil.
    1. takki á pistil til að uppfæra eða eyða pistil.
    1. takki til að búa til flokk.
1. Pistill (undir admin).
    1. form þar sem hægt er að uppfæra, eyða og skrifa nýja pistla. 
    1. pistill: 
        1. hver skráning fær ID 
        1. fyrirsögn 
        1. flokkur 
        1. ljósmynd 
        1. pistill 
        1. dagsetning 
1. Vefsíður fyrir 404 og 500 villumeldingar.

---

### Námsmat 

Einkunn:

- 10 
   - Vefurinn er hýstur (e. live production) með [PythonAnywhere](https://www.pythonanywhere.com/).
   - Settu upp Firebase Realtime Database í locked mode með [Security rules](https://medium.com/@juliomacr/10-firebase-realtime-database-rule-templates-d4894a118a98)   
   - Útfærðu upload virkni í formi fyrir ljósmyndir í [Cloud Storage Firebase](https://firebase.google.com/docs/storage?authuser=0)
- 9
   - Admin notandi getur búið til nýjan flokk (dýnamískt).
   - Öll framsetning á vef til fyrirmyndar og hnökralaus
       - Eigið CSS og / eða Barebones CSS safn
       - Hugað að textaframsetningu (letur og litaval, skerpa)
       - Hugað að framsetningu mynda (mátuleg stærð, myndir skalast rétt)
- 8 
   - Upload á ljósmynd í static möppu.
   - Ljósmynd birtist með réttum hætti á forsíðu með réttum pistli.
- 7 
    - Admin: 
        - allir pistlar eru birtir og raðaðir eftir dagsetningum (nýjast efst)
        - hnappur / hlekkur til að uppfæra og eyða pistil
   - Admin hefur töfluuppsetningu með CSS ( Dashboard )
   - CRUD (Create, Read, Updade, Delete) aðgerðir með Pistla með HTML Formi í gagnagrunni og birtir á forsíðu. 
- 6
   - Flokkar í valmynd verða drop-down.
   - CKEditor eða sambærilegur notaður til að skrá nýjan pistil.
- 5   
   - Nota flash message til að láta vita að submit hafi tekist.   
   - Nota url_for þar sem það á við ( t.d. CSS ).
   - Nota redirect / HTML Meta Refresh þar sem það á við.
- 4  
   - Pistlar birtast á forsíðu koma úr Firebase Real Time Database.  Allir geta lesið.  Framsetning frjáls, dagsetning á íslensku formatti.     
   - Adminsvæði aðeins fyrir innskráðan admin notanda (user:admin@admin.is ,password:123456), upplýsingar geymdar á Firebase Authentication.  Útfæra með SESSION
   - Adminsvæði þar sem pistlar eru skrifaðir með HTML Formi í Firebase Realtime gagnagrunn.  
        1. hver skráning fær ID 
        1. fyrirsögn 
        1. flokkur
        1. pistill
        1. dagsetning (_íslenskt format_)
   - Admin getur skráð sig út ( logout )
   - Valmynd inniheldur hlekkina; forsíða, login (fyrir admin) og flokka, gögn koma úr lista / dict í .py skrá.
   - Hægt er að velja flokk í valmynd sem birtir flokkaða pistla.
   - Jinja Template; breytur, lykkjunotkun, base og extends, include (head, footer, valmynd).
   - Static og dynamic route.
   - Error route ( ekki skila strengjum )
   - Vandað til verka með CSS uppsetningu (eigin og Barebones CSS safn þar sem það á við).
- 3 
   - Engin harðkóðun.
   - Forsíða, gögn koma frá dictionary eða breytum.
   - Footer, gögn úr breytum.
   - Jinja Template; breytur og include (head og footer).
- 2 
   - Forsíða birtir gögn harðkóðuð í Jinja template.  
   - Footer inniheldur upplýsingar um höfund verkefnis, ártal og skólaupplýsingar (Tölvubraut, Tækniskólinn).
   - Vefsíður fyrir 404 og 500 villumeldingar (frjáls útfærsla).
   - static route.
- 1 
   - Stórlega ábótavant.
   - Keyrir ekki.
- 0 
   - Vantar, lausn tekin af netinu eða unnin af öðrum.

---

### Skil

- Skilaðu þjappaðri (zip/rar) möppu með öllum skrám (ekki venv) 
- Skilaðu einnig vefslóð á hýsingu, admin innskráningar upplýsingum (user:admin@admin.is, password:123456) og skjámynd að gagnagrunni á Firebase og Security Rules ef þú útfærir gagnagrunninn í Locked Mode.

**Gangi þér vel!**
