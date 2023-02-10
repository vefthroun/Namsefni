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
- Forsíða inniheldur Html töflu sem birtir upplýsingar úr Firebase Realtime Database.  Gögnin sem unnið er með eru valfrjáls.  Sýnidæmi varðandi dýnamískar töflur:
    - [sýnidæmi 1](https://www.youtube.com/watch?v=mCy52I4exTU&ab_channel=teclado) (með tuples), [sýnidæmi 2](https://www.folkstalk.com/2022/09/jinja-table-template-with-code-examples.html) (með dictionary) og _[sýnidæmi 3](https://flask-table.readthedocs.io/en/stable/) (með class)_
- Notaðu custom filter í Jinja til að birta dagsetningu með íslensku sniði.
- Admin vefsíða er með form (label, input, textarea ) þar sem notandi slær inn gögnin sem fara í fb gagnagrunn. 
- Adminsíða með form til að búa til tilvitnanir sem eru svo vistuð í fb gagnagrunni. 
- Notaðu Template og PureCSS fyrir uppsetningu og framsetningu (Views). 
- Engin harðkóðun og önnur CSS söfn eru ekki leyfð.

---

### Námsmat og skil

1. Admin fb write aðgerðir og route útfærsla. (20%)
1. Admin (view) sem birtir WTForm með WYSIWYG innsláttarsvæði. (20%)  
1. Forsíða fb read aðgerðir, og route útfærsla. (20%)
1. Forsíða (view) birtir gögn frá database í töfluformi. (20%) 

Skilaðu þjappaðri (zip/rar) möppu með öllum skrám (ekki venv) ásamt skjámynd af fb gagnagrunni á Innu.