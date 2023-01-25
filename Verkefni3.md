---

### Verkefni 3
- Lykilmatsverkefni
- 30% af heildareinkunn
- Viðfangsefni:
  - Notkun á [JSON](https://en.wikipedia.org/wiki/JSON) og [API](https://en.wikipedia.org/wiki/API_key)
  - Jinja Template: inheritance, skilyrði
  - CSS Responsive Grid Layout með PureCSS
  - Eigið CSS 

---

### Verkefnalýsing
 
1. Útfærðu vefforrit í Flask sem nýtir API.
1. Notum [The Movie Database API](https://developers.themoviedb.org/3/getting-started/introduction)  
1. Nemendur þurfa að skrá sig inn á síðuna (register) hér að ofan og sækja um API key.  Það kostar ekkert að skrá sig.
1. Á forsíðu (index) skal birta grunn upplýsingar um 20 random bíómyndir.  Birta skal amk nafn og mynd.
1. Ef valin er ein bíómynd af forsíðu er farið á undirsíðu sem birtir nánari upplýsingar um valda bíómynd.
1. **Engin harðkóðun** til að standast grunnkröfur.
1. Byrjið á því að útfæra grunnkröfur til að standast lykilmat, síðan skulu þið bæta við virkni / útlit til að hækka einkunn.
1. Hér fyrir neðan er nánari útlistun á þeim þáttum sem þarf að uppfylla til að fá tiltekna einkunn.


**Ath:** Ekki setja inn persónuupplýsingar, sumir API biðja um að fá kreditkorta upplýsingar (sleppa þeim).<br>

---

### Nánari verklýsing, námsmat og skil

Einkunn:
- 10
  - Allt neðangreint frá og með einkunn 6 
  - Auka virkni að eigin vali
- 9
  - Allt neðangreint frá og með einkunn 6
  - Hægt að skoða trailer fyrir valda bíómynd
- 8
  - Allt neðangreint frá og með einkunn 6
  - Upplýsingar um helstu leikara og leikstjóra fyrir valda bíómynd
- 7
  - Allt neðangreint frá og með einkunn 6
  - ef valinn er flokkur (genre) opnast síða sem birtir random bíómyndir úr þeim flokk (dynamic route)
- 6
  - forsíða birtir nafn (original_title) og mynd (poster_path) bíómyndar (static route)
  - undirsíða birtir nánari upplýsingar um valda bíómynd (dynamic route)
  - upplýsingar um flokka (genre) fyrir valda bíómynd
  - Jinja: erfðir, include, lúppur og skilyrði
  - engin harðkóðun í Jinja templae
  - viðeigandi errorhandler routes
- 5
  - forsíða birtir nafn (original_title) og mynd (poster_path) bíómyndar (static route)
  - undirsíða birtir nánari upplýsingar um valda bíómynd (dynamic route)
    - nafn bíómyndar (original_title)
    - mynd (poster_path)
    - textalýsing myndar (overview)
    - hvenær mynd kom út (release_date)
    - lengd myndar (runtime)
  - Jinja: erfðir, include, lúppur og skilyrði
  - engin harðkóðun í Jinja templae
  - viðeigandi errorhandler routes
  - frjáls PureCSS Responsive Grid uppsetning
  - hnökralaus útlitshönnun (eigið CSS og PureCSS virkar að fullu)
- 4
  - forsíða birtir nafn (original_title) og mynd (poster_path) bíómyndar (static route)
  - undirsíða birtir nánari upplýsingar um valda bíómynd (dynamic route)
  - Jinja ábótavant (ekki erfðir og  / eða  ekki include)
  - harðkóðun í Jinja template
  - hnökrar í útlitshönnun (eigið CSS og PureCSS virkar ekki að fullu)
- 3
  - forsíða birtir nafn (original_title) og mynd (poster_path) bíómyndar (static route)
  - Jinja ábótavant (ekki erfðir og  / eða  ekki include)
  - harðkóðun í Jinja template
- 2
  - Keyrir en lítil sem engin virkni
  - harðkóðun í Jinja template
- 1
  - Keyrir ekki,  stórlega ábótavant
- 0
  - Engu skilað, eins / líkar lausnir hjá 2 eða fleiri nemendum


Skilaðu þjappaðri (zip/rar) möppu með öllum skrám (ekki venv) á Innu.

---

### Dæmi um gögn
Hlekkurinn / API endpoint [https://api.themoviedb.org/3/movie/550?api_key=???](https://api.themoviedb.org/3/movie/550?api_key=???) skilar okkur upplýsingum um bíómynd eftir id:  Í þessu tilviki bíómyndin The Fight Club sem hefur id = 550.  Í staðinn fyrir ??? setur þú þinn API key.
```python

{
  "adult": false,
  "backdrop_path": "/fCayJrkfRaCRCTh8GqN30f8oyQF.jpg",
  "belongs_to_collection": null,
  "budget": 63000000,
  "genres": [
    {
      "id": 18,
      "name": "Drama"
    }
  ],
  "homepage": "",
  "id": 550,
  "imdb_id": "tt0137523",
  "original_language": "en",
  "original_title": "Fight Club",
  "overview": "A ticking-time-bomb insomniac and a slippery soap salesman channel primal male aggression into a shocking new form of therapy. Their concept catches on, with underground \"fight clubs\" forming in every town, until an eccentric gets in the way and ignites an out-of-control spiral toward oblivion.",
  "popularity": 0.5,
  "poster_path": null,
  "production_companies": [
    {
      "id": 508,
      "logo_path": "/7PzJdsLGlR7oW4J0J5Xcd0pHGRg.png",
      "name": "Regency Enterprises",
      "origin_country": "US"
    },
    {
      "id": 711,
      "logo_path": null,
      "name": "Fox 2000 Pictures",
      "origin_country": ""
    },
    {
      "id": 20555,
      "logo_path": null,
      "name": "Taurus Film",
      "origin_country": ""
    },
    {
      "id": 54050,
      "logo_path": null,
      "name": "Linson Films",
      "origin_country": ""
    },
    {
      "id": 54051,
      "logo_path": null,
      "name": "Atman Entertainment",
      "origin_country": ""
    },
    {
      "id": 54052,
      "logo_path": null,
      "name": "Knickerbocker Films",
      "origin_country": ""
    },
    {
      "id": 25,
      "logo_path": "/qZCc1lty5FzX30aOCVRBLzaVmcp.png",
      "name": "20th Century Fox",
      "origin_country": "US"
    }
  ],
  "production_countries": [
    {
      "iso_3166_1": "US",
      "name": "United States of America"
    }
  ],
  "release_date": "1999-10-12",
  "revenue": 100853753,
  "runtime": 139,
  "spoken_languages": [
    {
      "iso_639_1": "en",
      "name": "English"
    }
  ],
  "status": "Released",
  "tagline": "How much can you know about yourself if you've never been in a fight?",
  "title": "Fight Club",
  "video": false,
  "vote_average": 7.8,
  "vote_count": 3439
}
```
