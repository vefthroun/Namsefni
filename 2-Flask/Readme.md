### Hvað er Flask

[Flask](https://flask.palletsprojects.com/en/2.2.x/) er Python veframmi (_web framework_) sem er byggður á litlum kjarna og auðvelt er að framlengja hann með viðbótum í pakkaformi (_package manager_). Flask er talið meira _Pythonic_ en Django veframminn vegna þess að Flask vefforrit er skýrara (_explicit_). Flask er auðvelt fyrir byrjendur, það hefur lítin grunnkóða (_boilerplate_) til að koma einföldu vefforriti í gang.

---

Flask is a Python web framework built with a small core and easy-to-extend philosophy. 
Flask is considered more Pythonic than the Django web framework because in common situations the equivalent Flask web application is more explicit. Flask is also easy to get started with as a beginner because there is little boilerplate code for getting a simple app up and running. 

[Flask – Overview](https://www.tutorialspoint.com/flask/flask_quick_guide.htm)

---

### Uppsetning á Flask

#### Windows leiðbeiningar (með notkun power shell)
1. Þú þarft að hafa nýlega stöðuga (stable) útgáfu t.d. 3.8.x af [python þýðanda](https://www.python.org/downloads/release/python-387/).
    1. Til að kanna núverandi útgáfu:  `python --version` 
1. Vefþróunarsvæði (_virutal environment_)
    1. búðu til möppu t.d. _vefforitun1_ í tölvunni t.d. á C: rót: `mkdir vefforritun1`
    1. færðu þig í nýju möppuna `cd vefforritun1`
    1. settu upp vefþróunarsvæði (virtual environment): `py -3 -m venv venv`
    1. Virkjaðu svæðið (activate venv): `venv\Scripts\activate`
1. Insetning Flask (Install flask framework)
    1. Activate venv: `venv\Scripts\activate`
    1. Notaðu pip til að setja inn (install) flask: `pip install flask`
    1. Opnaðu python þýðandann: `python`            
    1. Athugaðu hvort flask sé virkt (active):  `>>> import flask`  
    1. ef það er engin villumelding þá tókst það.  `>>> quit()`
1. Halló heimur
    1. Búðu til [halloheimur.py](Routes/halloheimur.md) skránna í Visual Studio Code Editor 
    1. Ekki nefna skrá "flask.py" nema að þú viljir lenda í vandræðum  
    1. vistaðu `halloheimur.py` í vefur3 möppunni sem geymir einnig venv möppuna
1. Að keyra og sjá halloheimur.py á local server
    1. Keyrðu python skrána: `python halloheimur.py`
    1. Skoðaðu vefsíðuna í vafra

- https://flask.palletsprojects.com/en/2.1.x/installation/
- [Vandamál við uppsetningu Flask](Vandamal.md)
- [MAC leiðbeiningar, _pip virtualenv mac_](https://programwithus.com/learn/python/pip-virtualenv-mac)

---

### 🌈 Skipulag VEFÞ2VFC

Klónaðu áfangageymsluna þína í möppuna vefforritun1 - [Undirbúningur (vefgrunnur)](https://github.com/vefgrunnur/Namsefni/wiki)

```

Github.com/22VF/22h-nafn (áfangageymsla - Classroom repository)
   |___ .gitignore
   |___ LICENCE
   |___ README.md
   |___ verkefni-1 
   |___ verkefni-2 
   |___ verkefni-3 
   |___ verkefni-4 
   |___ verkefni-5 
   |___ verkefni-6
   |___ verkefni-7
       
Vefforritun1 (local environment)
   |___	venv (python flask)
   |___	áfangageymsla (Classroom repository clone)
   
```
_Athugið að "venv" mappan á **ekki** að vera ofan í áfangageymslunni_

---

#### VS Code (python og venv)

1. Náðu þér í python stuðning sem er viðbót (extension) í VS Code [Python linting](https://marketplace.visualstudio.com/items?itemName=ms-python.python)
1. Opnaðu möppuna sem geymir python skrárnar fyrir flask appið.
1. Veldu python þýðandann sem er í venv (neðra vinstra horni) prófað að keyra python skrá.
1. .vscode -> settings.json  sýnir hvaða þýðandi verið að nota fyrir project.
1. (venv) er virkt (_activate_) sjálfkrafa þegar við opnum terminal innan VS Code  
1. Til að sækja söfn t.d. flask þá notum við [pip (python package installer)](https://pypi.org/) `pip install flask` 
1. Við getum skoðað hvaða viðbætur við höfum sett í `env/Lib/site-packages/` þessar viðbætur tilheyra eingöngu vefþróunarsvæðinu
1. Búum til `.gitignore` skrá  til að hunsa `venv` möppu og `.vscode skrá, við vijum ekki hafa þetta með í git aðgerðum. Tengjum Git við Github repository.

- [Getting Started with Python in VS Code](https://code.visualstudio.com/docs/python/python-tutorial)
- [Tutorial Flask in VS Code](https://code.visualstudio.com/docs/python/tutorial-flask)
- Python tutorial. [What is Flask Python?](https://pythonbasics.org/what-is-flask-python/)
- Python tutorial. [Hello world](https://pythonbasics.org/flask-tutorial-hello-world/)
- Video: [First install and Virtual Environments - Windows 10](https://www.youtube.com/watch?v=x1cbYa2SSlE)
- Video: [Visual Studio Code (Windows) - Setting up a Python Development Environment - Corey Shafer](https://www.youtube.com/watch?v=-nh9rCzPJ20)

---

#### Virtual environment og pip (package manager)
 - Video: [Python Tutorial: VENV (Mac & Linux) - How to Use Virtual Environments](https://www.youtube.com/watch?v=Kg1Yvry_Ydk)
 
---

<!--
### Skoða betur linka (kennari)
- http://www.compjour.org/lessons/flask-single-page/hello-tiny-flask-app/
- [Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
- Flask by Example – Project Setup https://realpython.com/flask-by-example-part-1-project-setup/
-->

<!--

#### Mac leiðbeiningar
Python Environment 101 - https://towardsdatascience.com/python-environment-101-1d68bda3094d
  - pyenv vs pipenv vs virtualenv

- https://opensource.com/article/19/6/python-virtual-environments-mac
  - homebrew + pyenv ( pyenv is a Python version management.)
- https://opensource.com/article/19/5/python-3-default-mac
---

-->
