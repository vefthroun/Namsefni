# skipulag CRUD

```
- index
    |_ texti úr rdb (R) tenging við Realtime database 
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
    |_ tenging við Realtime database 
        |_ Skrifa (C)
        |_ Uppfæra (U)
        |_ Eyða (D)

```