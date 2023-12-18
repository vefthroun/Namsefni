## Verkefni 2 
- 10% af heildareinkunn
- Viðfangsefni: 
   1. Data structure: Listar / Dictionary
   1. Dynamic routing 
   1. Jinja Template: include
   1. Eigið CSS eða safn eins og Barebones 

### Verkefnalýsing 
Útfærðu vörusíðuvef með Flask. Notaðu [gagnagrindina](#data) og [myndir](https://github.com/vefthroun/Namsefni/tree/main/static) sem fylgja verkefninu. Notaðu [Barebones]([https://purecss.io/](https://acahir.github.io/Barebones/)) safnið fyrir uppsetningu og framsetningu á vef eða eigið CSS. Engin harðkóðun.

Flask app (vefur) þarf að uppfylla eftirfarandi:

1. Vefurinn er hlutaður niður með include í Jinja2: header, menu og footer. Lykkjunotkun.
1. Forsíða inniheldur yfirlit yfir allar vörur: mynd, heiti og verð.  Einnig þarf hlekk / hnapp til að smella á til að sjá nánar um vöru (undirsíðu).
1. Undirsíða (valin vara) inniheldur nánari upplýsingar um vöruna; heiti, verð, mynd og textalýsing.
1. Í haus (header) vefsíðu skal vera valmynd. Valmynd þessi skal innihalda hlekki fyrir hvern vöruflokk (úr gagnagrindinni). Dæmi: Ef notandi velur hlekkinn **Vegan** birtist vefsíða (undirsíða) einungis með vörum úr þeim flokki (síun).
1. Gögn hlekkja / texti hlekkja skal koma úr gagnagrind, ekki harðkóða í template.
1. Fótur (footer) skal innihalda upplýsingar um höfund verkefnis.
1. Engin harðkóðun.


---

### Námsmat og skil 

   1. Uppsetning gagna í gagnagrindum og static myndir (5%)
   1. Valmynd birt með texta úr gagnagrind og gögn í footer koma einnig úr gagnagrind (10%)
   1. Forsíða birtir allar vörur úr gagnagrind (static routing) (10%)
   1. Undirsíða sem birtir valda vöru af forsíðu (dynamic routing) (20%)
   1. Undirsíða sem birtir allar vörur úr ákveðnum flokki (dynamic routing) (20%)  
   1. Notkun á Jinja: include (header, menu og footer) á öllum vefsíðum með Jinja (10%)
   1. Vefur er responsive með frjálsri dálkauppsetning á forsíðu.  Nota einnig eigið CSS eða [Barebones](https://acahir.github.io/Barebones/) eða svipað  (15%)
   1. Errorhandler routes (10%)
  


Skilaðu þjappaðri (zip/rar) möppu með öllum skrám (ekki venv) á Innu.

---

#### Data
```python

menu =  [
        {
            "id": 0,
            "nafn": "El Peppó Xtra",
            "mynd": "pizza0.JPG",
            "verd":1600,
            "álegg":["Xtra pepperóni", "Xtra ostur", "Xtra Sósa"],
            "flokkur":"kjöt"
        },
        {
            "id": 1,
            "nafn": "El Vegó",
            "mynd": "pizza1.JPG",
            "verd":1400,
            "álegg":["Paprika", "Laukur", "Ananas"],
            "flokkur":"vegan"
        },
        {
            "id": 2,
            "nafn": "Pizza MOI",
            "mynd": "pizza2.JPG",
            "verd":2000,
            "álegg":["Banani", "Ananas", "Lárviðarlauf"],
            "flokkur":"vegan"
        },
        {
            "id": 3,
            "nafn": "El Logos",
            "mynd": "pizza3.JPG",
            "verd":1500,
            "álegg":["Spicy Pepperoni", "Chilli Pepper", "Hot Sauce", "Laukur"],
            "flokkur":"sterk"
        },
                {
            "id": 4,
            "nafn": "Pizza Domo",
            "mynd": "pizza4.JPG",
            "verd":2500,
            "álegg":["Nautahakk", "Paprika", "Laukur"],
            "flokkur":"kjöt"
        },
        {
            "id": 5,
            "nafn": "El Grande",
            "mynd": "pizza5.JPG",
            "verd":3000,
            "álegg":["Pepperoni", "Skinka", "Nautahakk", "Paprika", "Laukur"],
            "flokkur":"kjöt"
        }
    ]

```

<!-- 
1. Notaðu mismunandi litaþema fyrir hvern fréttaflokk fyrir sig. Dæmi: ef birtar eru fréttir úr flokknum **sport** verða haus og fótur með ákveðnum lit. Ef birtar eru fréttir úr flokknum **veidi** verður litur á haus og fæti öðruvísi o.s.frv.
-->
