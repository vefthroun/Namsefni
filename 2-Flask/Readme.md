### Hvað er Flask

[Flask](https://flask.palletsprojects.com/en/2.2.x/) er Python veframmi (_web framework_) sem er byggður á litlum kjarna og auðvelt er að framlengja hann með viðbótum í pakkaformi (_package manager_). Flask er talið meira _Pythonic_ en Django veframminn vegna þess að Flask vefforrit er skýrara (_explicit_). Flask er auðvelt fyrir byrjendur, það hefur lítin grunnkóða (_boilerplate_) til að koma einföldu vefforriti í gang, [Flask API](https://tedboy.github.io/flask/interface_api.html).

#### Skráarskipulag
- Templateskrár sem í grunninn byggir á HTML geymast í möppu sem nefnist `templates`.
- Stílsíður (CSS), myndir, JavaScript og önnur `binary` skjöl fara í möppu sem nefnist `static`.
- Gögn eru ýmist vistuð í lista, dictionary, skrám eða gagnagrunna.

---

### Uppsetning á Flask
-  Mac/Windows [Flask installation](https://flask.palletsprojects.com/en/2.2.x/installation/) leiðbeiningar.

#### Windows leiðbeiningar (t.d. með Power Shell)
1. Þú þarft að hafa nýlega stöðuga (stable) útgáfu af python þýðanda.
    1. Til að kanna núverandi útgáfu:  `python --version` 
1. Vefþróunarsvæði (_virutal environment_)
    1. búðu til möppu t.d. _vefforitun_ í tölvunni t.d. á C: rót: `mkdir vefforritun`
    1. færðu þig í nýju möppuna `cd vefforritun`
    1. settu upp vefþróunarsvæði (virtual environment): `py -3 -m venv venv`
    1. Virkjaðu svæðið (activate venv): `venv\Scripts\activate`
1. Insetning Flask (Install flask framework)
    1. Activate venv: `venv\Scripts\activate`
    1. Notaðu pip til að setja inn (install) flask: `pip install flask`
    1. Opnaðu python þýðandann: `python`            
    1. Athugaðu hvort flask sé virkt (active):  `>>> import flask`  
    1. ef það er engin villumelding þá tókst það.  `>>> quit()`
1. Halló heimur
    1. Búðu til [app.py](Routes/halloheimur.md) skránna í Visual Studio Code Editor 
    1. Ekki nefna skrá "flask.py" nema að þú viljir lenda í vandræðum  
    1. vistaðu `app.py` í _vefforitun_ möppunni sem geymir einnig venv möppuna
1. Að keyra og sjá app.py á innbyggðum local server
    1. Keyrðu python skránna: `flask run` eða `python app.py`
    1. Skoðaðu vefsíðuna í vafra

- [Hugsanleg vandamál við uppsetningu Flask](Vandamal.md)

---

### VS Code ritill
- [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
- [Flask tutorial in VS Code](https://code.visualstudio.com/docs/python/tutorial-flask)

#### VSCode og VENV
1. Náðu þér í python stuðning sem er viðbót (extension) í VS Code [Python linting](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
1. Opnaðu möppuna sem geymir python skrárnar fyrir flask appið.
1. Veldu python þýðandann sem er í venv (neðst í VSCode) prófað að keyra (Play takkinn) python skrá með `Code runner` extension í VSCode.
1. (venv) er virkt (_activate_) sjálfkrafa þegar við opnum terminal innan VS Code  

#### Aðrar gagnlegar stillingar í VSCode
1. Debugger. Hægt er að búa til og stilla `launch.json` config (taka t.d. út no-reload í "args") 
1. Git og Github. Það er nauðsynlegt er að búa til `.gitignore` skrá  til að hunsa `venv` möppu og `.vscode skrá, við vijum ekki hafa þetta með í git aðgerðum. Hægt er að tengja Git við Github repository í VSCode.


<!--
1. .vscode -> settings.json  sýnir hvaða þýðandi verið að nota fyrir project.
1. Til að sækja söfn t.d. flask þá notum við [pip (python package installer)](https://pypi.org/) `pip install flask` 
1. Við getum skoðað hvaða viðbætur við höfum sett í `env/Lib/site-packages/` þessar viðbætur tilheyra eingöngu vefþróunarsvæðinu

- Video: [First install and Virtual Environments - Windows 10](https://www.youtube.com/watch?v=x1cbYa2SSlE)
- Video: [Visual Studio Code (Windows) - Setting up a Python Development Environment - Corey Shafer](https://www.youtube.com/watch?v=-nh9rCzPJ20)
- Video: [Python Tutorial: VENV (Mac & Linux) - How to Use Virtual Environments](https://www.youtube.com/watch?v=Kg1Yvry_Ydk)
-->
 



