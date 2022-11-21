## Verkefni 6  
- 14% af heildareinkunn
- Viðfangsefni: 
  1. [Firebase rauntíma NoSQL gagnagrunnur](https://github.com/vefthroun/Namsefni/tree/main/6-Gagnagrunnur#firebase)
     1. Uppsetning á gagnagrunni fyrir vefapp.
     1. Gagnagrunnsaðgerðir (CRUD) með Pyrebase4.
     1. [Firebase Authentication](https://firebase.google.com/products/auth?gclid=Cj0KCQiAveebBhD_ARIsAFaAvrEtvE57H2m6H_lRneDW80cc-iUJLxlzvZRbKca57QR-9vnX0QwBLVwaAug8EALw_wcB&gclsrc=aw.ds).
  1. [Sessions](https://github.com/vefthroun/Namsefni/tree/main/5-Cookies%26Sessions) 

---

### Verkefnalýsing
Búðu til vef með gagnagrunni sem vinnur með tilvitnanir t.d. twitter eða e. funny quotes.

- Settu upp Firebase Realtime Database í test mode.
- Forsíða birtir tilvitnanir úr fb gagnagrunni.
- Innskráningarsíða (login) er með email/password [FB authentication](https://github.com/nhorvath/Pyrebase4#authentication). Notaðu netfangið `dummy@mail.com` og lykilorðið `12345678`.
- Skráningarsíða (signup). Bættu í firebase admin profile (nafn og netfang). 
- Adminsíða með form til að búa til tilvitnanir sem eru svo vistuð í fb gagnagrunni. Adminsíða sýnir einnig nafn á admin úr fb gagnagrunni. 
- Það á ekki ekki að vera hægt að fara beint inná Adminsíðu nema að hafa aðgang. Takki gerir notanda kleift að skrá sig út (eyða session).
- Jinja Template og CSS fyrir uppsetningu og framsetningu (Views).
- Engin harðkóðun.

---

### Námsmat og skil

1. Signup. View, fb (create), admin notandi. (20%) 
1. Innskráning með Firebase Authentication, view og route útfærsla. (20%)
1. Adminsíða. View, fb (write) aðgerðir og route útfærsla. (20%)
1. Sessions. Ekki hægt að skoða Admin síðu nema að vera innskráður notandi og útskráning. (20%)
1. Forsíða. View, fb (read) aðgerðir og route útfærsla. (20%)

Skilaðu þjappaðri (zip/rar) möppu með öllum skrám (ekki venv) á Innu.

