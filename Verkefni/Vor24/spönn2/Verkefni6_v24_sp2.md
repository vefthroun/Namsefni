## Verkefni 6

- Lykilmatsþáttur
- 30% af heildareinkunn
- Allt námsefni áfanga undir 

---

### Verkefnalýsing

Útfærðu persónulegan bloggvef með Flask, [sýnidæmi](https://blog-admin-ui.netlify.app/). Efnisval (texti og myndir) er valfrjálst en færslurnar þurfa að vera **10** að lágmarki (ekki bull). Notaðu eigið CSS eða PureCSS fyrir uppsetningu (_layout_) og útlit. Gert er ráð fyrir sjálfstæðum vinnubrögðum.  Verkefnið er einstaklingsverkefni.

1. Forsíða: 
    1. birtir alla pósta sem allir geta lesið, nýjasti birtist efst. 
    1. birtir json gögn (td. af TMDB + hægt að lesa um myndir nánar)
1. Efnisyfirlit (_menu_): 
    1. forsíða | ritstjórn/admin | innskráning | nýskráning | útskráning.
1. Nýskráning
   1. Notandi getur skráð sig til að fá aðgang að ritsíðu (blog) - _lykilorð endurtekið tvívegis_
1. Innskráning:
    1. Notandi sem er skráður í FB authentication á að geta skráð sig inn og skrifað pósta. 
    1. Eftir útskráningu er ekki hægt að fara aftur í ritsíðuna.
1. Admin/ritstjórn (blogsíðan). 
    1. Yfirlit yfir alla pósta <!--(titill, flokkur, dagsetning) raðað eftir dagsetningum --> (nýjasti efst)
    1. Takki til að bæta við póst.
    1. Takki til að uppfæra póst
    1. Takki til eyða pósti.
1. Vefsíður fyrir 404, 405 og 500 villumeldingar.
1. Footer:
    1.Inniheldur upplýsingar um höfund verkefnis, skólaupplýsingar (Tölvubraut, Tækniskólinn) og vefslóð á hýsingu vefs.

<!-- 1. Pistill (undir admin).
    1. Form þar sem hægt er að uppfæra, eyða og skrifa nýja pistla. 
    1. pistill: 
        1. hver skráning fær ID 
        1. fyrirsögn 
        1. flokkur 
        1. ljósmynd 
        1. pistill 
        1. dagsetning -- ath! ekki nægur tími til að útfæra þessa lausn -->
---

### Námsmat 

Einkunn:

- 10 
   - Vefurinn er hýstur (e. live production) með [PythonAnywhere](https://www.pythonanywhere.com/).   
   - Á admin síðu er hægt að hlaða inn (upload) ljósmyndir í [Cloud Storage Firebase](https://firebase.google.com/docs/storage?authuser=0)
   - Á admin síðu er hægt að bæta ljósmynd við póst 
   <!-- Admin notandi getur búið til nýjan flokk (dýnamískt). engar upplýsingar að finna um þessa lausn á kennarar geymslunni -->
   <!-- Settu upp Firebase Realtime Database í locked mode með [Security rules](https://medium.com/@juliomacr/10-firebase-realtime-database-rule-templates-d4894a118a98)
   Tími of naumur til að útskýra þetta dæmi -->
- 9 
    - Öll framsetning á vef til fyrirmyndar og hnökralaus
       - Myndir eru hýstar í Firbase Storage og eru birtar á vefnum. 
       - Eigið CSS safn  eða annað tilbúið CSS safn
       - Responsive Grid
       - Hugað að textaframsetningu (letur og litaval, skerpa)
       - Hugað að framsetningu mynda (mátuleg stærð, myndir skalast rétt)
- 8 
   - Ritstjórn / Admin síða. 
        - Er vernduð með SESSIONS
        - Allir pistlar eru birtir og nýjasti birtur efst
        - Takkar (link) til að uppfæra og eyða pósti.
   <!-- Admin hefur töfluuppsetningu með CSS ( Dashboard ) engar upplýsingar að finna um þessa lausn á kennarar geymslunni -->
   - CRUD aðgerðir er hægt að framkvæma á admin síðu með WTFormi í gagnagrunni. 
   - Á admin síðu er CKEditor notaður til að skrifa pósta með "Basic" uppsetningu
   - Póstar birtast á vefsíðu með uppsetningu notenda (tenglar, feitletrað, skáletrað ofl.) 
   <!-- Notaðu macros (hjálparfall) til að losna við endurtekningar þegar WTForm er birt í Jinja template.? -->
- 7
   - Pistlar eru skrifaðir með WTFormi í gagnagrunni og birtir á forsíðu. 
   - Innskráning með WTForm og Firebase Authentication.
   - _Flash message_ er notað til að láta vita hvort innskráning tókst eða ekki.
   - Útskrá takki til að taka út [session] notanda. 
   - CSS uppsetning og framsetning á Inn- og nýskráningu er í lagi.
   <!-- Hægt er að velja flokk í valmynd sem birtir flokkaða pistla.-->
- 6  
   - Pistlar eru birtir á forsíðu úr Firebase Realtime gagnagrunni. 
   - Nota flash message til að láta vita að aðgerðir notanda hafi tekist.   
   - Nota url_for fyrir linka.
   - Nota redirect þar sem það á við.
   <!-- Nota HTML Meta Refresh þar sem það á við.-->
   - Forsíða. Hugað er að margin, padding, letur og leturgerð með CSS.
- 5      
   - Adminsvæði aðeins fyrir innskráða notendur, upplýsingar geymdar á Firebase Authentication.
   - Póstar eru skráðir í Realtime gagnagrunn.  
        1. Hver skráning fær ID 
        1. Fyrirsögn (text)
        <!--1. Flokkur  (drop-down)-->
        <!--1. ljósmynd (url)-->
        1. póstur (textarea)
        1. Tölvupóstfang (email)
        1. Höfundur (text)
   - Valmynd/efnisyfirlit inniheldur hlekkina; forsíða | ritstjórn/admin | innskráning | nýskráning | útskráning. <br>Gögn koma úr lista / dict í .py skrá.

- 4 
   - Póstar birtast á forsíðu koma úr Firebase Realtime Database.  Allir geta lesið.  
   - Forsíða, json gögn.
   - Jinja Template; breytur, lykkjunotkun, base og extends, include (head, footer, valmynd).
   - Static og dynamic route.
   - Error route og vefsíður fyrir 404 og 500 villumeldingar
   - CSS uppsetning (eigin og PureCSS safn þar sem það á við).
   - Footer, gögn úr breytum.
   - Jinja Template; breytur og include (head og footer).
- 3 
   - Forsíða birtir gögn harðkóðuð í Jinja template.  
   - Footer inniheldur upplýsingar um höfund verkefnis, ártal og skólaupplýsingar (Tölvubraut, Tækniskólinn).
   - Vefsíður fyrir 404 og 500 villumeldingar (frjáls útfærsla).
   - static route.
- 2 
   - Stórlega ábótavant.
   - Keyrir ekki.
- 1 
   - lausn tekin af netinu eða unnin af öðrum.
- 0 
   - Vantar skil

---

### Verkefnaskil

- Skilaðu verkefni 6 í eigin verkefnageymslu (_repository_) 
- Settu vefinn þinn á [Pythonanywhere](https://www.pythonanywhere.com/) vefhýsinguna. 
  - Skilaðu tengli á pythonanywhere vefinn í Innu
<!-- Skilaðu einnig vefslóð á hýsingu, admin innskráningar upplýsingum (user:admin@admin.is, password:123456) og skjámynd að gagnagrunni á Firebase og Security Rules ef þú útfærir gagnagrunninn í Locked Mode. (engin er að ná að setja upp useradmin) -->

**Gangi þér vel!**
