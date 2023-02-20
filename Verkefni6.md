## Verkefni 6

- Lykilmatsþáttur
- 30% af heildareinkunn
- Allt námsefni áfanga undir 

---

### Verkefnalýsing

Útfærðu persónulegan bloggvef með Flask, [sýnidæmi](https://blog-admin-ui.netlify.app/). Efnisval (texti og myndir) er valfrjálst en færslurnar þurfa að vera **10** að lágmarki (ekki bull). Notaðu PureCSS safn og eigið CSS fyrir uppsetningu (layout) og útlit. Gert er ráð fyrir sjálfstæðum vinnubrögðum.  Verkefnið er einstaklingsverkefni.

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
       - Eigið CSS og PureCSS safn
       - PureCSS Responsive Grid
       - Hugað að textaframsetningu (letur og litaval, skerpa)
       - Hugað að framsetningu mynda (mátuleg stærð, myndir skalast rétt)
- 8 
   - Upload (ljósmynd) á miðlara í static möppu.
   - Ljósmynd birtist með réttum hætti á forsíðu með réttum pistli.
- 7 
    - Admin (nema að búa til flokk). 
        - Er vernduð með SESSIONS
        - allir pistlar eru birtir og raðaðir eftir dagsetningum (nýjast efst)
        - takka (link) til að uppfæra og eyða pistil.
   - Admin hefur töfluuppsetningu með CSS ( Dashboard )
   - CRUD aðgerðir með Pistla með WTFormi í gagnagrunni og birtir á forsíðu. 
   - Valmynd inniheldur hlekkina; forsíða, flokkar (drop-down), admin, login og logout.
   - Notaðu macros (hjálparfall) til að losna við endurtekningar þegar WTForm er birt í Jinja template.
- 6
   - Pistlar eru skrifaðir með WTFormi í gagnagrunni og birtir á forsíðu. 
   - Innskráning með WTForm og Firebase Authentication.
   - Notað er flash message til að láta vita hvort innskráning tókst eða ekki.
   - Logout takki til að útskrá admin notanda. 
   - Valmynd inniheldur hlekkina; forsíða, flokkar (drop-down), admin, login og logout.
   - CSS uppsetning og framsetning á Innskráningu er í lagi.
- 5  
   - Valmynd inniheldur hlekkina; forsíða, flokkar (drop-down) og admin.
   - Pistlar eru birtir á forsíðu úr Firebase Realtime gagnagrunni. 
   - Notaðu flash message til að láta vita að submit hafi tekist.   
   - Notað er for_url fyrir linka.
   - Notað er redirect þar sem það á við.
   - Notað HTML Meta Refresh þar sem það á við.
   - Forsíða. Hugað er að margin, padding, letur og leturgerð með CSS.
   - Rétt notkun á HTML elements (HTML tag). Sjá t.d. [HTML Best Practices](https://www.freecodecamp.org/news/html-best-practices/) og [HTML Style Guide](https://www.w3schools.com/html/html5_syntax.asp)
- 4  
   - Pistlar birtast á forsíðu koma úr Firebase Real Time Database.  Allir geta lesið.  Framsetning frjáls, dagsetning á íslensku formatti.     
   - Adminsvæði aðeins fyrir innskráðan admin notanda (user:admin@admin.is ,password:123456), upplýsingar geymdar á Firebase Authentication.
   - Adminsvæði þar sem pistlar eru skrifaðir með formi í Firebase Realtime gagnagrunn.  
        1. hver skráning fær ID 
        1. fyrirsögn (input)
        1. Flokkur  (drop-down)
        1. ljósmynd (url)
        1. pistill (textarea)
        1. dagsetning (_timestamp_)
   - Myndir eru með vefslóðir, hýstar t.d. á imgur.com eða picsum.photos. 
   - Valmynd inniheldur hlekkina; forsíða og flokkar, gögn koma úr lista.
   - Hægt er að velja flokk í valmynd sem birtir flokkaða pistla.
   - Jinja Template; breytur, lykkjunotkun, base og extends, include (head, footer, valmynd).
   - Static og dynamic route.
   - Error route og vefsíður fyrir 404 og 500 villumeldingar
   - CSS uppsetning (eigin og PureCSS safn þar sem það á við).
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
