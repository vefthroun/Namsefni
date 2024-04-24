# Realtime database (RtDb), skipulag CRUD

```
- index
    |_ texti úr rdb (R) tenging við RtDb
    |_ innskráning /login 
        |_ tenging við Authentication db
            |_ OK > /editor*
            |_ error > /index
    |_ nyskraning /register
        |_ tenging við Authentication db
            |_ OK > index/login
            |_ error > index
- editor
    |_ lokað með session id
    |_ tenging við RtDb
        |_ Skrifa (C) /create > /editor
        |_ Uppfæra (U) /update > /editor
        |_ Eyða (D) /delete > /editor

```

## Vinnsla

### Read

- Titill (sótt í RtDb)
- Innihald (sótt í RtDb)
- Höfundur (sótt í RtDb)
- Email (birt úr session)
- Tími (birt úr session)

> postar=db.child('postholf').child('postur').get().val()

### Create

- Titill (skráð í RtDb)
- Innihald (skráð í RtDb)
- Höfundur (skráð í RtDb)
- Email (birt úr session)
- Tími (birt úr session - skráð í RtDb)

> posts = db.child("postholf").get()
> db.child("postholf").push(.......)

### Update

- Titill (náð í og yfirritað)
- Innihald (náð í og yfirritað)
- Tími (náð í og yfirritað)

> update = db.child("postholf").get(.....)
> db.child("postholf").child(........).update(.......)

### delete

> posts = db.child("postholf").get()
> db.child("postholf").child(p.key(...)).remove() 