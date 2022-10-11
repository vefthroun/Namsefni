## Verkefni 6 

### _Google Firebase gagnagrunnur og Session._

Í 6. verkefni vinnum við með Firebase gagnagrunninn frá Google ( firebase.google.com ) í Flask. Til þess þurfum við að nota viðbætur í Python sem heita _pycryptodome og pyrebase4_ sem þarf að setja upp með _pip install_.

**Fireabase gagnagrunnur**

- Ef þú ert ekki með Google reikning þarftu að búa hann til ( kostar ekkert )
- Skráðu þig inn á **firebase.google.com**
- Búðu til nýtt **project** ( myndband í Innu )
- Við ætlum að nota **Authentication** til að halda utan um netfang og lykilorð til innskráningar

**Vefsíðan / virkni**

- Á forsíðu ( index route ) þurfa einungis að vera tveir hlekkir ( takkar ) annar sem vísar á innskráningar síðu ( login ) og hinn sem vísar á nýskráningar síðu ( register )
   - Á innskráningar síðu skal vera HTML form sem leyfir notanda að slá inn notendanafn ( sem í þessu kerfi þarf að vera email ) og lykilorð. Ef notandi skráir sig rétt inn skal kerfið vísa notanda á læsta síðu. Innihald síðunnar er frjálst og skiptir ekki öllu máli. Í þessu vefkerfi á alls ekki að vera hægt að skoða þessa læstu síðu nema að hafa aðgang með réttu notendanafn og lykilorði.
   - Á nýskráningar síðu skal vera HTML form sem leyfir notanda að nýskrá sig inn á síðuna með því að velja notendanafn ( email ) og lykilorð. Athugaðu að í kerfinu má aðeins nota hvert email aðeins einu sinni. Kerfið gengur úr skugga um að svo sé.
   - Á læstu síðunni sem aðeins er hægt að skoða ef notandi er rétt innskráður þarf að vera útskráningar takki sem gerir notanda kleift að skrá sig út ( eyða session ).

**Flask útfærsla**

1. Notaðu _dynamic routing_.
2. Notaðu _templates_.
3. Notið **flask session** til aðgangsstýringar.
4. Notið **firebase Authentication** til að halda utan um email og password.

### Námsmat 14% af heildareinkunn

1. Dynamic routing, template inheritance, include, error route ( 2% )
2. Ekki hægt að skoða læsta síðu nema að vera innskráður notandi ( 2% )
3. Innskráning ( 4% )
4. Nýskráning ( 4% )
5. Útskráning ( 2% )

### Skil

*  https://github.com/22vf/ 22h-geymslan þín/verkefni-6

_Gangi þér vel_
