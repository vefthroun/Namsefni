---
### Verkefni 3
- Lykilmatsverkefni
- 30% af heildareinkunn
- Viðfangsefni:
  - Notkun á [JSON](https://en.wikipedia.org/wiki/JSON) og [API](https://en.wikipedia.org/wiki/API_key)
  - Jinja Template: inheritance, loops, conditionals
  - CSS Responsive Grid Layout t.d. með NEW.CSS
  - Eigið CSS 

---

### Verkefnalýsing
 
1. Útfærðu vefforrit í Flask sem nýtir API.
1. Notum [The Movie Database API](https://www.themoviedb.org/) / [Getting started](https://developer.themoviedb.org/docs/getting-started) / [API reference](https://developer.themoviedb.org/reference/intro/getting-started)  
1. Nemendur þurfa að [skrá sig inn á síðuna (register)](https://github.com/vefthroun/Namsefni/tree/main/3-Json/join_TMDB) hér að ofan og sækja um API key.  _Það kostar ekkert að skrá sig_.
1. Á forsíðu (index) skal birta grunn upplýsingar um 20 random þáttaraðir.  Birta skal amk nafn og mynd.
1. Ef valin er ein þáttaröð af forsíðu er farið á undirsíðu sem birtir nánari upplýsingar um valda þáttaröð.
1. **Engin harðkóðun** til að standast grunnkröfur.
1. Byrjið á því að útfæra grunnkröfur til að standast lykilmat, síðan skulu þið bæta við virkni / útlit til að hækka einkunn.
1. Hér fyrir neðan er nánari útlistun á þeim þáttum sem þarf að uppfylla til að fá tiltekna einkunn.


**Ath:** Ekki setja inn persónuupplýsingar, sumir API biðja um að fá kreditkorta upplýsingar (sleppa þeim).<br>

---

### Nánari verklýsing, námsmat og skil

Einkunn:
- 10 
  - Sama og einkunn 9 + 
  - Auka virkni að eigin vali í samráði við kennara
- 9
  - Sama og einkunn 8 +
  - Hægt að skoða trailer fyrir valda þáttaröð (embed af youtube)
- 8
  - Sama og einkunn 7 +
  - Upplýsingar um helstu leikara, leikstjóra, framleiðendur fyrir valda þáttaröð ( ekki lúppa í gegnum allt "crew" og birta, sigta út  )
- 7
  - Sama og einkunn einkunn 6 +
  - Ef valinn er flokkur (genre) opnast síða sem birtir random þáttaraðir úr völdum flokk (dynamic route)
- 6
  - Sama og einkunn 5 +
  - Valmöguleiki að sjá yfirlit yfir allar seríur (seasons) þáttaraðar
    - nafn (name)
    - fjöldi þátta (episode_count)
    - mynd (poster_path)
- 5
  - Sama og einkunn 4 + 
  - hvenær fyrsti þáttur þáttaraðar var sýndur (first_air_date), dagsetning á íslensku formatti    
  - hnökralaus útlitshönnun (eigið CSS og t.d. NEW.CSS virkar að fullu)
- 4
  - forsíða birtir nafn (original_title) og mynd (poster_path) þáttaraðar (static route)
  - undirsíða birtir nánari upplýsingar um valda þáttaröð (dynamic route)
    - nafn þáttaraðar (original_title)
    - Tagline (tagline)
    - mynd (poster_path)
    - textalýsing þáttaraðar (overview)
    - hvenær fyrsti þáttur þáttaraðar var sýndur (first_air_date) 
    - flokkar sem þáttaröð tilheyrir (genres)
  - viðeigandi errorhandler routes
  - Jinja: erfðir, include, lúppur og skilyrði
  - engin harðkóðun í Jinja template
  - frjáls Responsive Grid uppsetning
  - smávægilegir hnökrar í útlitshönnun sleppa
- 3
  - forsíða birtir nafn (original_title) og mynd (poster_path) þáttaraðar (static route)
  - Jinja ábótavant (ekki erfðir og  / eða  ekki include)
  - harðkóðun í Jinja template
- 2
  - Keyrir en lítil sem engin virkni
  - harðkóðun í Jinja template
- 1
  - Keyrir ekki, stórlega ábótavant
- 0
  - Engu skilað, eins / líkar lausnir hjá 2 eða fleiri nemendum


Skilaðu þjappaðri (zip/rar) möppu með öllum skrám (ekki venv) á Innu.

---

### Dæmi um gögn
Hlekkurinn / API endpoint [https://api.themoviedb.org/3/discover/tv?api_key=???](https://api.themoviedb.org/3/discover/tv?api_key=???) skilar upplýsingum um 20 þáttaraðir á fyrstu síðu ( page ) af 500.  Til að fá næstu 20 þáttaraðir af síðu 2 þaftu að bæta við skilyrðinu / flagginu &page=2 fyrir aftan api_key eða [https://api.themoviedb.org/3/discover/tv?api_key=???&page=2](https://api.themoviedb.org/3/discover/tv?api_key=???&page=2) 

Hlekkurinn / API endpoint [https://api.themoviedb.org/3/tv/1668?api_key=???](https://api.themoviedb.org/3/tv/1668?api_key=???) skilar okkur upplýsingum um þáttaröð eftir id:  Í þessu tilviki þáttaröðin Friends sem hefur id = 1668.  Í staðinn fyrir ??? setur þú þinn API key.
```python

{
    "adult": false,
    "backdrop_path": "/l0qVZIpXtIo7km9u5Yqh0nKPOr5.jpg",
    "created_by": [
        {
            "id": 163461,
            "credit_id": "525710bf19c295731c03280b",
            "name": "Marta Kauffman",
            "gender": 1,
            "profile_path": "/AsX4ZOoQP5oQVLiA51zdRiTNKTm.jpg"
        },
        {
            "id": 1216352,
            "credit_id": "525710bf19c295731c032811",
            "name": "David Crane",
            "gender": 2,
            "profile_path": "/1NYo5ZYCSqoxQ5sqXLMDm3cqvKp.jpg"
        }
    ],
    "episode_run_time": [],
    "first_air_date": "1994-09-22",
    "genres": [
        {
            "id": 35,
            "name": "Comedy"
        }
    ],
    "homepage": "",
    "id": 1668,
    "in_production": false,
    "languages": [
        "en"
    ],
    "last_air_date": "2004-05-06",
    "last_episode_to_air": {
        "id": 87632,
        "name": "The Last One",
        "overview": "Ross and Phoebe chase Rachel to the airport, but end up at the wrong one. Chandler and Monica finish packing for their move to the suburbs, and Joey loses Chick Jr. and Duck Jr. in the foosball table.\n\nThe series finale finds Rachel, Monica, Phoebe, Joey, Chandler and Ross embarking on the next chapters in their lives. The six of them have been there for one another through all the ups and downs of becoming adults. Now it's their last day together, and it's one of momentous events and last-minute surprises. Even as the friends make major decisions, they share a bond that will last forever.",
        "vote_average": 9.5,
        "vote_count": 35,
        "air_date": "2004-05-06",
        "episode_number": 17,
        "episode_type": "finale",
        "production_code": "176266 / 176267",
        "runtime": 48,
        "season_number": 10,
        "show_id": 1668,
        "still_path": "/7XmwmXkJtObpt6ABPENanrJHlg9.jpg"
    },
    "name": "Friends",
    "next_episode_to_air": null,
    "networks": [
        {
            "id": 6,
            "logo_path": "/cm111bsDVlYaC1foL0itvEI4yLG.png",
            "name": "NBC",
            "origin_country": "US"
        }
    ],
    "number_of_episodes": 228,
    "number_of_seasons": 10,
    "origin_country": [
        "US"
    ],
    "original_language": "en",
    "original_name": "Friends",
    "overview": "Six young people from New York City, on their own and struggling to survive in the real world, find the companionship, comfort and support they get from each other to be the perfect antidote to the pressures of life.",
    "popularity": 451.699,
    "poster_path": "/2koX1xLkpTQM4IZebYvKysFW1Nh.jpg",
    "production_companies": [
        {
            "id": 1957,
            "logo_path": "/pJJw98MtNFC9cHn3o15G7vaUnnX.png",
            "name": "Warner Bros. Television",
            "origin_country": "US"
        },
        {
            "id": 31810,
            "logo_path": "/3oyBCnFO3tIRmny3yzYQpF5n2cS.png",
            "name": "Bright/Kauffman/Crane Productions",
            "origin_country": "US"
        }
    ],
    "production_countries": [
        {
            "iso_3166_1": "US",
            "name": "United States of America"
        }
    ],
    "seasons": [
        {
            "air_date": "2001-02-14",
            "episode_count": 39,
            "id": 4583,
            "name": "Specials",
            "overview": "",
            "poster_path": "/xaEj0Vw0LOmp7kBeX2vmYPb5sTg.jpg",
            "season_number": 0,
            "vote_average": 0.0
        },
        {
            "air_date": "1994-09-22",
            "episode_count": 24,
            "id": 4573,
            "name": "Season 1",
            "overview": "",
            "poster_path": "/odCW88Cq5hAF0ZFVOkeJmeQv1nV.jpg",
            "season_number": 1,
            "vote_average": 8.0
        },
        {
            "air_date": "1995-09-21",
            "episode_count": 24,
            "id": 4574,
            "name": "Season 2",
            "overview": "",
            "poster_path": "/kC9VHoMh1KkoAYfsY3QlHpZRxDy.jpg",
            "season_number": 2,
            "vote_average": 8.3
        },
        {
            "air_date": "1996-09-16",
            "episode_count": 25,
            "id": 4575,
            "name": "Season 3",
            "overview": "",
            "poster_path": "/n9u4pslqb6tpiLc8soldL5IbAyG.jpg",
            "season_number": 3,
            "vote_average": 8.2
        },
        {
            "air_date": "1997-09-25",
            "episode_count": 23,
            "id": 4576,
            "name": "Season 4",
            "overview": "",
            "poster_path": "/3WdH3FNMXgp3Qlx21T7kwKS8Mtc.jpg",
            "season_number": 4,
            "vote_average": 8.3
        },
        {
            "air_date": "1998-09-24",
            "episode_count": 23,
            "id": 4577,
            "name": "Season 5",
            "overview": "",
            "poster_path": "/aEwLXWbo6gV1TNIv9veu4rRwsPZ.jpg",
            "season_number": 5,
            "vote_average": 8.4
        },
        {
            "air_date": "1999-09-23",
            "episode_count": 23,
            "id": 4578,
            "name": "Season 6",
            "overview": "",
            "poster_path": "/7EU6bV6d8j1Xbc1F8QoNkOZrpsi.jpg",
            "season_number": 6,
            "vote_average": 8.3
        },
        {
            "air_date": "2000-10-12",
            "episode_count": 23,
            "id": 4579,
            "name": "Season 7",
            "overview": "",
            "poster_path": "/yvUZVChjOnqCjB9rjdEqEmpDdnQ.jpg",
            "season_number": 7,
            "vote_average": 8.2
        },
        {
            "air_date": "2001-09-27",
            "episode_count": 23,
            "id": 4580,
            "name": "Season 8",
            "overview": "",
            "poster_path": "/eh6PPkrzkXsEksRJDcdtx9lZsqX.jpg",
            "season_number": 8,
            "vote_average": 8.5
        },
        {
            "air_date": "2002-09-26",
            "episode_count": 23,
            "id": 4581,
            "name": "Season 9",
            "overview": "",
            "poster_path": "/1IvIdN4I5jJ0bwC3BkmDCy4pQ9j.jpg",
            "season_number": 9,
            "vote_average": 8.5
        },
        {
            "air_date": "2003-09-25",
            "episode_count": 17,
            "id": 4582,
            "name": "Season 10",
            "overview": "",
            "poster_path": "/67ETB6XIqYc5vZkyAjN8XINOX5i.jpg",
            "season_number": 10,
            "vote_average": 8.7
        }
    ],
    "spoken_languages": [
        {
            "english_name": "English",
            "iso_639_1": "en",
            "name": "English"
        }
    ],
    "status": "Ended",
    "tagline": "I'll be there for you.",
    "type": "Scripted",
    "vote_average": 8.442,
    "vote_count": 7573
}

```
