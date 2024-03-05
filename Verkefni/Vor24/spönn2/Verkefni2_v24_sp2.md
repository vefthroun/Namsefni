## Verkefni 2 
- 10% af heildareinkunn
- Viðfangsefni: 
   1. Data structure: Listar / Dictionary
   1. Dynamic routing 
   1. Jinja Template: include
   1. Eigið CSS eða safn eins og New CSS

### Verkefnalýsing 
Útfærðu vörusíðuvef með Flask. Notaðu [gagnagrindina](#data) og [myndir](https://github.com/vefthroun/Namsefni/tree/main/Verkefni/Vor24/sp%C3%B6nn2/static) sem fylgja verkefninu. Notaðu  [New CSS](https://newcss.net/) safnið fyrir uppsetningu og framsetningu á vef eða eigið CSS. Engin harðkóðun.

Flask app (vefur) þarf að uppfylla eftirfarandi:

1. Vefurinn er hlutaður niður með include í Jinja2: header, menu og footer. Lykkjunotkun.
1. Forsíða inniheldur yfirlit yfir allar vörur: mynd, address og verð.  Einnig þarf hlekk / hnapp til að smella á til að sjá nánar um vöru (undirsíðu).
1. Undirsíða (valin vara) inniheldur nánari upplýsingar um vöruna; address, verð, mynd og textalýsing (pnr og lysing).
1. Í haus (header) vefsíðu skal vera valmynd. Valmynd þessi skal innihalda hlekki fyrir hvern vöruflokk (úr gagnagrindinni). Dæmi: Ef notandi velur hlekkinn **Einbýlishús** birtist vefsíða (undirsíða) einungis með vörum úr þeim flokki (síun).
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
   1. Vefur er responsive með frjálsri dálkauppsetning á forsíðu.  Nota eigið CSS / [New CSS](https://newcss.net/) eða svipað  (15%)
   1. Errorhandler routes (10%)
  

Skilaðu þjappaðri (zip/rar) möppu með öllum skrám (ekki venv) á Innu.

---

#### Data
```python

hus =  [
        {
            "id": 0,
            "address": "Aðalstræði 1",
            "mynd": "hus0.PNG",
            "verd":160000000,
            "nanar":{"pnr":101, "lysing":"Falleg eign í hjarta Reykjavíkur"},
            "flokkur":"einbyli"
        },
        {
            "id": 1,
            "address": "Túngata 2",
            "mynd": "hus1.PNG",
            "verd":140000000,
            "nanar":{"pnr":450, "lysing":"Rólegur og fallegur staður við sjávarsíðuna"},
            "flokkur":"einbyli"
        },
        {
            "id": 2,
            "address": "Sigtún 3",
            "mynd": "hus2.PNG",
            "verd":145000000,
            "nanar":{"pnr":102, "lysing":"Fjölskylduvæn eign á góðum stað, nálægt allri þjónustu"},
            "flokkur":"einbyli"
        },
        {
            "id": 3,
            "address": "Skagabraut 3",
            "mynd": "hus3.PNG",
            "verd":65000000,
            "nanar":{"pnr":110, "lysing":"Fallegt og nýlega endurnýjað raðhús fyrir fólk á uppleið í lífinu"},
            "flokkur":"radhus"
        },
                {
            "id": 4,
            "address": "Háteigsgata 4",
            "mynd": "hus4.PNG",
            "verd":75000000,
            "nanar":{"pnr":200, "lysing":"Þeir segja að það sé gott að búa í Kópavogi..."},
            "flokkur":"radhus"
        },
        {
            "id": 5,
            "address": "Skagahlíð 55",
            "mynd": "hus5.PNG",
            "verd":30000000,
            "nanar":{"pnr":250, "lysing":"Lítil og falleg íbúð í glænýju fjölbýli á rótgrónum stað í sveitinni"},
            "flokkur":"fjolbyli"
        }
    ]

```