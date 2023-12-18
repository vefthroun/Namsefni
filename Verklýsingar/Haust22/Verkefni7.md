## Verkefni 7 

- Lykilmatsþáttur
- 20% af heildareinkunn 

---

### Verkefnalýsing

Útfærðu persónulegan bloggvef með Flask, [sýnidæmi](https://blog-admin-ui.netlify.app/). Efnisval (texti og myndir) er valfrjálst en færslurnar þurfa að vera **10** að lágmarki (ekki bull). Notaðu CSS safn (**samt ekki Bootstrap**) eða eigið CSS fyrir uppsetningu (layout) og útlit. Gert er ráð fyrir sjálfstæðum vinnubrögðum.

1. Forsíða: 
    1. birtir alla pistla sem allir geta lesið, nýjasti birtist efst. 
1. Flokkar:
    1. birtir alla pistla í flokki sem allir geta lesið. 
1. Valmynd: 
    1. forsíða, flokkar, admin, innskráning og úskráning.
1. Footer:
    1. inniheldur upplýsingar um höfund verkefnis, skólaupplýsingar (Tölvubraut, Tækniskólinn) og vefslóða á hýsingu vefs.
1. Innskráning:
    1. aðeins admin notandi á að geta skráð sig inn og séð Admin. Notaðu netfangið dummy@mail.com og lykilorðið 12345678
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
        1. Flokkur 
        1. ljósmynd 
        1. pistill 
        1. dagsetning 
1. Vefsíður fyrir 404 og 500 villumeldingar.

---

### Námsmat 

Einkunn:

- 10 
   - Vefurinn er hýstur (e. live production) með [PythonAnywhere](https://www.pythonanywhere.com/).
   - Settu upp Firebase Realtime Database í locked mode með security rules.    
   - Útfærðu upload virkni í formi fyrir ljósmyndir í [Cloud Storage Firebase](https://firebase.google.com/docs/storage?authuser=0)
   - Admin notandi getur búið til nýjan flokk (dýnamískt).
   - CSS: Vefur er responsive (mobile og desktop) og framsetning er til fyrirmyndar.
   - _Valkvæmt: Náðu í gögn úr API fyrir fyrstu 10 færslurnar og skrifaðu beint í fb gagnagrunn._
   - _Valkvæmt: Profile_ 
        - _Profile upplýsingar (nafn, email, mynd) fengið frá Firebase Authentication._
        - _form til að uppfæra profile upplýsingar._
        - _takki til að breyta lykilorði (reset)._
- 9 
   - Upload (ljósmynd) á miðlara í static möppu.
   - Hugað er að stærð mynda og framsetningu með CSS.
- 8  
   - CRUD aðgerðir með Pistla með WTFormi og WYSIWYG HTML í Firebase Realtime Gagnagrunnur og birtir á forsíðu.
   <!-- Pistill: Hægt er að velja úr nokkrum tilbúnum myndum, mynd með pistil sem er hýst á miðlara (static mappa). -->
   - Authentication með Firebase fyrir innskráningu.
   <!-- - hak til að birta ekki pistil_  -->
- 7 
    - Admin (nema að búa til flokk). 
        - Er vernduð með SESSIONS
        - allir pistlar eru birtir og raðaðir eftir dagsetningum (nýjast efst)
        - takka (link) til að bæta við pistil.
        - takka (link) til að uppfæra og eyða pistil.
   - Admin hefur töfluuppsetningu með CSS.
   - CRUD aðgerðir með Pistla með WTFormi í gagnagrunni eða JSON skrá og birtir á forsíðu. 
   - Valmynd inniheldur hlekkina; forsíða, flokkar (drop-down), admin, login og logout.
   - _Valkvæmt: Notaðu macros (hjálparfall) til að losna við endurtekningar._
- 6
   - Pistlar eru skrifaðir með WTFormi í gagnagrunni (eða JSON skrá) og birtir á forsíðu. 
   - Pistilsíðan er vernduð með SESSIONS.
   - Innskráning með WTForm og authentication.
   - Notað er flash message til að láta vita hvort innskráning tókst eða ekki.
   - Logout takki til að útskrá admin notanda. 
   - Valmynd inniheldur hlekkina; forsíða, flokkar (drop-down), admin, login og logout.
   - CSS uppsetning og framsetning á Innskráningu er í lagi.
- 5  
   - Valmynd inniheldur hlekkina; forsíða, flokkar (drop-down) og admin.
   - Dagsetning er birt með íslensku sniðmáti. (date format) á forsíðu
   - Adminsvæði þar sem pistlar eru skrifaðir með formi í Firebase Realtime gagnagrunni eða JSON skrá.
        1. hver skráning fær ID 
        1. fyrirsögn (input)
        1. Flokkur  (drop-down)
        1. ljósmynd (url)
        1. pistill (textarea)
        1. dagsetning (_timestamp_)
   - Pistlar eru birtir á forsíðu úr Firebase Realtime gagnagrunni eða JSON skrá. 
   - Notaðu flash message til að láta vita að submit hafi tekist.   
   - Notað er for_url fyrir linka.
   - Forsíða. Hugað er að margin, padding, letur og leturgerð með CSS.
   - Rétt notkun á HTML elements (HTML tag). Sjá t.d. [HTML Best Practices](https://www.freecodecamp.org/news/html-best-practices/) og [HTML Style Guide](https://www.w3schools.com/html/html5_syntax.asp)
- 4  
   - Gagnagrind; listi sem inniheldur dictionaries, breytur.
   - Myndir eru með vefslóðir, hýstar t.d. á imgur.com.
   - Pistlar eru birtir á forsíðu (ekki _timestamp_). 
   - Valmynd inniheldur hlekkina; forsíða og flokkar, gögn koma úr lista.
   - Hægt er að velja flokk í valmynd sem birtir flokkaða pistla.
   - Vefsíður fyrir 404 og 500 villumeldingar
   - Jinja Template; breytur, lykkjunotkun, base og extends, include (head, footer, valmynd).
   - static og dynamic route.
   - CSS uppsetning (eigin eða safn).
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
- Skilaðu einnig vefslóð á hýsingu, admin innskráningar upplýsingum og skjámynd að gagnagrunni á firebase. 

**Gangi þér vel!**
