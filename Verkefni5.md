## Verkefni 5  
- 10% af heildareinkunn
- Viðfangsefni: 
  - [Firebase Realtime Database](https://github.com/vefthroun/Namsefni/tree/main/6-Gagnagrunnur#firebase)
      1. Uppsetning á gagnagrunni fyrir vefapp.
      1. Gagnagrunnsaðgerðir (CRUD) með Pyrebase4.
 - [WYSIWYG HTML editor](https://github.com/vefthroun/Namsefni/blob/main/WTForms/Readme.md#wysiwyg-html-editor) notum CKEditor
 - Dýnamísk HTML Tafla.
 - Jinja Filters.

---

### Verkefnalýsing

- Settu upp Firebase Realtime Database í test mode.
- Forsíða birtir upplýsingar úr Firebase Realtime Database.  Gögnin sem unnið er með eru valfrjáls. Dæmi: 
    - Fréttatengt efni ( fyrirsögn, dagsetning, megintexti, höfundur )
    - Lagalisti ( titill lags, höfundur lags og útgáfuár )
    - Tilvitnanir úr kvikmyndum ( nafn kvikmyndir, tilvitnunin sjálf, útgáfurár kvikmyndar )
    - Annað sem ykkur dettur í hug ( í samráði við kennara )
- Allir notendur vefs geta skoðað færslur úr gagnagrunni.
- Aðeins innskráður admin notandi getur:
    - Bætt við nýrri færslu
    - Eytt valinni færslu
- Þegar admin notandi skráir sig inn í kerfið fer hann inn á "Dashboard" síðu.
    - Á Dashboard síðu eru allar grunnupplýsingar úr gagnagrunni birtar í HTML töflu
    - Í hverri röð töflu skal vera möguleiki á að eyða viðkomandi færslu ( hnappur / hlekkur )
    - Á Dashboard síðu skal vera möguleiki á að bæta við nýrri færslu í gagnagrunn ( hnappur / hlekkur )
    - Admin notandi þarf að geta skráð sig út
- Sýnidæmi varðandi dýnamískar töflur:
    - [sýnidæmi 1](https://www.youtube.com/watch?v=mCy52I4exTU&ab_channel=teclado) (með tuples), [sýnidæmi 2](https://www.folkstalk.com/2022/09/jinja-table-template-with-code-examples.html) (með dictionary) og _[sýnidæmi 3](https://flask-table.readthedocs.io/en/stable/) (með class)_
- Öll HTML formin skulu vera útfærð með WTForm klasanum ( Eiga að vera 2 form, 1 fyrir login á admin og 1 til að skrá nýjar upplýsingar í gagnagrunn ).
- Form til að skrá inn nýjar upplýsingar verður að innihalda WYSIWYG HTML editor ( CKEditor ).
- Notaðu alla Jinja Template virkni ( include / erfðir / filter ).
- PureCSS fyrir uppsetningu og framsetningu ( Responsive Grid / Form / Table / Menu  ) og eigið CSS. 
- Notaðu viðeigandi Jinja filter.
- Engin harðkóðun og önnur CSS söfn eru ekki leyfð.

---

### Námsmat og skil

1. Uppsetning á Firebase Realtime gagnagrunn í test mode og samskipti við Python Flask app (5%) 
1. Forsíða birtir gögn úr gagnagrunni frjáls framsetning (15%)
1. Admin notandi skráir sig inn í kerfi og fer á Dashboard síðu, Dashboard hluti aðeins opin innskráðum notanda (25%)
    - WTForm
    - HTML tafla
    - Jinja filter
1. Admin notandi eyðir færslu úr töflu (20%)
1. Admin notandi bætir við nýrri færslu í gagnagrunn (20%)
    - WTForm
    - CKEditor
1. Admin notandi skráir sig út (5%)
1. Uppsetning / framsetning með PureCSS og eigin CSS (10%)

Skilaðu þjappaðri (zip/rar) möppu með öllum skrám (ekki venv) ásamt skjámynd af fb gagnagrunni á Innu.  **Hafðu admin notanda með email: admin@admin.is pass: 123456 í Auth hluta Firebase**
