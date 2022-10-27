## Verkefni 2 
- 14% af heildareinkunn
- Viðfangsefni: 
   - Static routing
   - Jinja template: include, lykkjunotkun
   - Datastructure; breytur, tuples, listi og dictionary
   - CSS/HTML: tafla, listi og efnisyfirlit (láréttur listi).
   
---

### Verkefnalýsing 

Flask app (vefur) þarf að uppfylla eftirfarandi:

1. Forsíða inniheldur fyrirsögn, ljósmynd (static) og málsgrein [sýnidæmi](https://css-tricks.com/how-do-you-make-a-layout-with-pictures-down-one-side-of-a-page-matched-up-with-paragraphs-on-the-other-side/). 
1. Undirsíða 1 inniheldur töflu (5x5) sem geymir upplýsingar (frjálst) <br>[sýnidæmi 1](https://www.youtube.com/watch?v=mCy52I4exTU&ab_channel=teclado) (með tuples), [sýnidæmi 2](https://www.folkstalk.com/2022/09/jinja-table-template-with-code-examples.html) (með dictionary), [sýnidæmi 3](https://flask-table.readthedocs.io/en/stable/) (með class)
1. Undirsíða 2 inniheldur lista (5 items) sem geymir upplýsingar (frjálst).
1. Síður innihalda lárettan menu, sjá [sýnidæmi](https://hackersandslackers.com/flask-jinja-templates/).
1. Allur texti og hlekkir í html eru geymd í gagnagrindum (data structure); breytur, tuple, listi og dictionary.
1. Static routing útfærsla fyrir forsíðu, undirsíður og 404.
1. Vefinn er hlutaður niður með include í Jinja2: head, header, menu og footer og lykkjunotkun.
1. Búðu til html síðu fyrir 404 villumeldingu.
1. Notað er for_url fyrir static linka á CSS og ljósmyndir.
1. CSS fyrir útlit.

---

### Námsmat og skil 

1. Static routing útfærsla (15%) 
   1. forsíða, undirsíður, Status Codes (404 og 500)
2. Template og gögn.
   1. head, header, footer með include og breytur (10%)
   1. undirsíða með lista og lykkju notkun (10%)
   1. forsíða með dictonary og lykkju notkun (15%)
   1. undirsíða með töflu með tuple með tuples items, listi með dictionary items eða class og lykkjunotkun (20%) 
   1. láréttur menu (include) með lista sem geymir dictonary items fyrir hlekki og lykkju notkun (20%)
3. CSS útlit og framsetning (10%)

Skilaðu þjappaðri (zip/rar) möppu með öllum skrám (ekki venv) á Innu.

