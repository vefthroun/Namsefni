## Verkefni 3 
- 10% af heildareinkunn
- Viðfangsefni: 
   1. Data structure: Listi með dictionary
   1. Dynamic routing 
   1. Jinja Template: include
   1. PureCss, eigið Css 

### Verkefnalýsing 
Útfærðu vörusíðuvef með Flask. Notaðu [gagnagrindina](#data) og myndir sem fylgja verkefninu. Notaðu [purecss](https://purecss.io/) safnið fyrir uppsetningu og framsetningu á vef. Engin harðkóðun.

Flask app (vefur) þarf að uppfylla eftirfarandi:

1. Vefurinn er hlutaður niður með include í Jinja2: header, menu og footer. Lykkjunotkun.
1. Forsíða inniheldur yfirlit yfir allar vörur: mynd, heiti, verð og hlekk til að sjá nánar um vöru (undirsíðu).
1. Undirsíða (valin vara) inniheldur nánari upplýsingar um vöruna; heiti, verð, mynd, textalýsing og listi.
1. Í haus (header) vefsíðu skal vera valmynd. Valmynd þessi skal innihalda hlekki fyrir hvern vöruflokk (úr gagnagrindinni). Dæmi: Ef notandi velur hlekkinn **Sófar** birtist vefsíða (undirsíða) einungis með vörum úr þeim flokki (síun).
1. Gögn hlekkja / texti hlekkja skal koma úr gagnagrind, ekki harðkóða í template.
1. Fótur (footer) skal innihalda upplýsingar um höfund verkefnis.
1. Engin harðkóðun.


---

### Námsmat og skil 

   1. Uppsetning gagna í gagnagrindum og static myndir (5%)
   1. Valmynd birt með texta úr gagnagrind og gögn í footer koma einnig úr gagnagrind (10%)
   1. Forsíða birtir allar vörur úr gagnagrind(static routing) (10%)
   1. Undirsíða sem birtir valda vöru af forsíðu (dynamic routing) (20%)
   1. Undirsíða sem birtir allar vörur úr ákveðnum flokki (dynamic routing) (20%)  
   1. Notkun á Jinja: include (header, menu og footer) á öllum vefsíðum með Jinja (10%)
   1. Vefur er responsive með frjálsri dálkauppsetning á forsíðu með [Pure Responsive Grid](https://purecss.io/grids/#pure-responsive-grids).  Nota einnig eigið Css  (15%)
   1. Errorhandler routes (10%)
  


Skilaðu þjappaðri (zip/rar) möppu með öllum skrám (ekki venv) á Innu.

---

#### Data
```python

vorulisti =  [
        {
            "id": 0,
            "nafn": "Leðursófi",
            "lysing": "Fallegur og þægilegur leðursófi sem hentar fyrir alla fjölskylduna.",
            "mynd": "mynd0.jpg",
            "verd":160000,
            "nanar":["Svartur","60 X 120 CM"],
            "flokkur":"sofi"
        },
        {
            "id": 1,
            "nafn": "Svefnsófi",
            "lysing": "Svefnsófi sem hentar fyrir lítil og nett rými.  Rosa gott að sofa í honum.",
            "mynd": "mynd1.jpg",
            "verd":140000,
            "nanar":["Grár","70 X 120 CM"],
            "flokkur":"sofi"
        },
        {
            "id": 2,
            "nafn": "Fataskápur",
            "lysing": "Ef þú átt mikið af fötum er þessi skápur akkúrat fyrir þig, einn tveir og bing bæng.",
            "mynd": "mynd2.jpg",
            "verd":75000,
            "nanar":["Hvítlakkað","80 X 60 X 180 CM"],
            "flokkur":"skapur"
        },
        {
            "id": 3,
            "nafn": "Þvottaskápur",
            "lysing": "Ef þú vilt hafa allt á hreinu og vel skipulagt þá er þetta skápurinn fyrir þig.",
            "mynd": "mynd3.jpg",
            "verd":50000,
            "nanar":["Hvítt","100 X 70 X 200 CM"],
            "flokkur":"skapur"
        },
                {
            "id": 4,
            "nafn": "Borðstofuborð",
            "lysing": "Stílhreint og fallegt borð inn á hvert heimili.",
            "mynd": "mynd4.jpg",
            "verd":50000,
            "nanar":["Hvíttlakkaður Askur","100 X 70 X 200 CM"],
            "flokkur":"bord"
        },
        {
            "id": 5,
            "nafn": "Barnaborð",
            "lysing": "Fyrir smáfólkið, nú geta allir föndrað og leikið sér við þetta fallega borð.",
            "mynd": "mynd5.jpg",
            "verd":30000,
            "nanar":["Hvítt","50 X 50 X 60 CM"],
            "flokkur":"bord"
        }
    ]

```

<!-- 
1. Notaðu mismunandi litaþema fyrir hvern fréttaflokk fyrir sig. Dæmi: ef birtar eru fréttir úr flokknum **sport** verða haus og fótur með ákveðnum lit. Ef birtar eru fréttir úr flokknum **veidi** verður litur á haus og fæti öðruvísi o.s.frv.
-->
