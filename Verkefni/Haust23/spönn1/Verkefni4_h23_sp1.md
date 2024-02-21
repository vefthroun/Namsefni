## Verkefni 
- 10% af heildareinkunn
- Viðfangsefni:
  1. [Firebase Authentication](https://firebase.google.com/products/auth?gclid=Cj0KCQiAveebBhD_ARIsAFaAvrEtvE57H2m6H_lRneDW80cc-iUJLxlzvZRbKca57QR-9vnX0QwBLVwaAug8EALw_wcB&gclsrc=aw.ds).
  1. [HTML Forms](https://www.w3schools.com/html/html_forms.asp) 
  1. [Sessions](https://github.com/vefthroun/kennarar/tree/main/Namsefni/5-Cookies%26Sessions)
  1. [Flash message](https://flask.palletsprojects.com/en/2.2.x/patterns/flashing/)(Valkvætt)
  1. [Barebones Form](https://acahir.github.io/Barebones/?)
  1. [Datetime timestamp](https://www.programiz.com/python-programming/datetime/timestamp-datetime)
  <!-- 1. Tek út WTForm haust '23 vegna tímaskorts -->
   
  
---

### Verkefnalýsing
1. Skráningarsíða (signup).  Nýskráning með email og password.  Password verður að vera amk 6 tákn (bókstafir/tölustafir), email verður að vera gilt og má ekki vera til fyrir í gagnagrunni.  Notum Firebase Authentication til að vista upplýsingar.
1. Innskráningarsíða (login) er með email/password [Firebase Authentication](https://github.com/nhorvath/Pyrebase4#authentication). Notaðu netfangið `dummy@mail.com` og lykilorðið `123456`.
1. Adminsíða sýnir profile úr Firebase Authentication.
    - email innskráðs notanda ( email )
    - hvenær innskráður notandi nýskráði sig fyrst ( createdAt ), íslenskt format dd.mm.áááá kk:mm:ss
    - hvenær innskráður notandi skráði sig inn síðast ( lastLoginAt ), íslenskt format dd.mm.áááá kk:mm:ss
1. Það á ekki ekki að vera hægt að fara beint inná Adminsíðu nema að hafa aðgang.
1. Notaðu session til aðgansstýringar 
1. Notaðu flash message til að láta vita hvort aðgerðir hafa tekist (valkvætt).
1. Útfærðu útskráningar virkni (eyða session).
1. Notaðu alla eiginleika Jinja template úr fyrri verkefnum.
1. Notaðu Barebones, eigið css eða annað fyrir framsetningu. 
1. Engin harðkóðun.

---

### Námsmat og skil

1. Uppsetning HTML Form og formvinnslu (login og register form). Tékk á innsláttarsvæði, ekki tóm og rétt format með email og password (10%)
1. Notandi nýskráir sig:
  - Gögn skráð í Firebase Authentication með réttum hætti (15%)
  - Rétt bugðist við ef gögn eru ekki rétt eða email þegar til í kerfi  (5%)
1. Notandi skráir sig inn, vefsíða með HTML Form og virkni:
  - Gögn tekin úr formi og pöruð við gögn í Firebase Authentication (10%)
  - Ef notandi er til þarf að setja í gang session og opna á admin hluta (10%)
  - Ef notandi er ekki til þarf að bregðast við með viðeigandi hætti (10%)
1. Innskráður notandi kemst inn á admin hluta, stýrt með session, eftirfarandi gögn birt:
    - email innskráðs notanda  (5%)
    - hvenær innskráður notandi nýskráði sig fyrst ( createdAt ), íslenskt format dd.mm.áááá kk:mm  (10%)
    - hvenær innskráður notandi skráði sig inn síðast ( lastLoginAt ), íslenskt format dd.mm.áááá kk:mm  (10%)
1. Útskráning (5%)
1. Barebones, eigið eða annað Css (5%)
1. Flash message (5%)

Skilaðu þjappaðri ( zip/rar ) möppu með öllum skrám (ekki venv) á Innu.
