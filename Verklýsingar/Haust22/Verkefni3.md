## Verkefni 3 
- 14% af heildareinkunn
- Viðfangsefni: 
   1. Data structure: Listi með dictionary
   1. Dynamic routing 
   1. Jinja Template: inheritance, include, skilyrði
   1. CSS safn 

### Verkefnalýsing
Útfærðu vörusíðuvef með Flask. Notaðu [gagnagrindina](#data) sem fylgir verkefninu sem viðmið (þú þarft að breyta innihaldi). Notaðu [purecss](https://purecss.io/) safnið fyrir uppsetningu og framsetningu á vef. Engin harðkóðun.

1. Forsíða inniheldur yfirlit yfir allar vörur. heiti, verð, vöruflokk, mynd (static) og hlekk til að sjá nánar um vöru (undirsíðu).
1. Undirsíða (vara) inniheldur nánari upplýsingar um vöruna; heiti, verð, mynd, vöruflokk, textalýsing og listi.
1. Í hausi (header) vefsíðu skal vera valmynd. Valmynd þessi skal innihalda hlekki fyrir hvern vöruflokk (úr gagnagrindinni). Dæmi: Ef notandi velur hlekkinn **Tölvur** þá birtist vefsíða (undirsíða) einungis með vörum úr þeim flokki (síun).
1. Fótur (footer) skal innihalda upplýsingar um höfund verkefnis.


---

### Námsmat og skil 

   1. Uppsetning gagna í gagnagrindum (ekki bull) og static myndir (5%)
   1. forsíða birtir allar vörur (static routing) (10%)
   1. undirsíða sem birtir valda vöru af forsíðu (dynamic routing) (15%)
   1. undirsíða sem birtir allar vörur úr ákveðnum flokki (dynamic routing) (15%)  
   1. Notkun á base og extends í Jinja (10%)
   1. Notkun á include (header og footer) á öllum vefsíðum með Jinja (10%)
   1. dálka uppsetning á forsíðu og síðu eftir flokkum með CSS layout (15%) 
   1. frjáls CSS uppsetning á undirsíðu (vara) (5%)
   1. Útlit og framsetning með CSS (5%)
   1. Vefur er responsive (mobile og desktop) (10%)
  


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
