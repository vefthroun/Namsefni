# Skipulag

Mikilvægt áður en forritun hefst er að hafa yfirsýn á verkefnið.

> Hér er dæmi um skipulag, það má útfæra verkefnið með öðrum hætti

## Skipurit - Sitemap

```

           forsíða
        ______|______
        |           |
       users      admin

```
## Efnisyfirlit

1. Haus (header)
    - innskráning
    - nýskráning
    - forsíða
    - annað td félagsmiðlatákn
1. Fótur (footer)
    - upplýsngar um eiganda og hönnuð (þig)
    - hafðu samband (spjallbox)
        
# innihaldslýsing

1. Á forsíðu (/): 
    - birtast allar færslur notenda (users) sem allir geta lesið 
    - er tenging við Json database
1. Á "users": 
    - einungis skráðir notendur geta komist á /users
    - hver notandi getur aðeins séð eigin pósta
        - notandi getur skrifað nýja pósta (C)
        - notandi getur lesið eigin pósta (R)
        - notandi getur uppfært eigin pósta (U)
        - notandi getur eytt eigin pósta (D)
1. Á "admin"
    - einungis einn notandi getur komist á /admin (Addi)
    - Addi getur séð alla pósta notenda og gert allar CRUD aðgerðir
    - Addi hefur yfirlit yfir alla notendur í "users"
    - Addi getur eytt notendum
    - Addi getur lokað á notanda (email) til að nýskrá sig aftur (extra)

---

### Flæðirit - Wireframe

- [drawio.com](https://www.drawio.com/)

Appið er hægt að beintengja við Github :smile;

---

### [Python pyrebase](../6-Gagnagrunnur/Pyrebase/README.md)

#### Read

> postar=db.child('postholf').child('postur').get().val()

#### Create

> posts = db.child("postholf").get()
> db.child("postholf").push(.......)

#### Update

> update = db.child("postholf").get(.....)
> db.child("postholf").child(........).update(.......)

#### delete

> posts = db.child("postholf").get()
> db.child("postholf").child(p.key(...)).remove() 

#### RtDb tafla (_dæmi_)

- postholf 
    - RtDb ID  
    - Name 
    - Content 
    - Timestamp
    - email
