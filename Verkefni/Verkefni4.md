## Verkefni 4
- 14% af heildareinkunn
- Viðfangsefni: JSON og API

---

### Verkefnalýsing

1. Útfærðu vefforrit í Flask sem nýtir API að eigin vali með samþykki kennara. Hér er hægt að skoða nokkra [Public APIs](https://github.com/public-apis/public-apis)  . 
1. Notaðu [API key](https://en.wikipedia.org/wiki/API_key) fyrir auðkenningu ef þess er þörf.
1. Gerðu API fyrirspurn (API request) á API endpoint. Birtu valin gögn úr response (20 JSON objectar að lágmarki) með random á forsíðu.
1. Á forsíðu skal birta gögn frá 20 random JSON objectum.
1. Gerðu aðra API fyrirspurn sem nýtir upplýsingarnar úr fyrri fyrirspurn (forsíða) og birtu valin gögn úr response, 1 JSON object á undirsíðu.
1. Notaðu Template og CSS fyrir uppsetningu og framsetningu.
1. Engin harðkóðun.

Hér er dæmi um Flask útfærslu [tv-maze-app.herokuapp.com](https://tv-maze-app.herokuapp.com/) sem notar [TV Maze](https://www.tvmaze.com/api) API.

**Ath:** Ekki setja inn persónuupplýsingar, sumir API biðja um að fá kreditkorta upplýsingar (sleppa þeim).<br>
API sem eru **ekki** í boði að nota; TV Maze, APIS.is, restcountries.com

---

### Námsmat og skil

1. Gögn eru sótt af API endpoint fyrir forsíðu, random notkun og static route útfærsla. (25%) 
1. Gagnavinnsla og template fyrir forsíðu (20%)
1. Gögn eru sótt af API endpoint fyrir undirsíðu og dynamic route útfærsla. (25%) 
1. Gagnavinnsla og template fyrir undirsíðu. (20%)
1. Viðmót og layout með CSS. (10%)

Skilaðu þjappaðri (zip/rar) möppu með öllum skrám (ekki venv) á Innu.

---

### Dæmi um gögn
Hlekkurinn / API endpoint [https://api.tvmaze.com/shows] skilar okkur fyrstu 240 þáttunum í lista með 240 JSON objects. Hér fyrir neðan er JSON object sem lýsir fyrsta þættinum í kerfinu:  
```python

{
    "id":1,
    "url":"https://www.tvmaze.com/shows/1/under-the-dome",
    "name":"Under the Dome",
    "type":"Scripted",
    "language":"English",
    "genres":["Drama","Science-Fiction","Thriller"],
    "status":"Ended",
    "runtime":60,
    "averageRuntime":60,
    "premiered":"2013-06-24",
    "ended":"2015-09-10",
    "officialSite":"http://www.cbs.com/shows/under-the-dome/",
    "schedule":{"time":"22:00","days":["Thursday"]},
    "rating":{"average":6.5},
    "weight":98,
    "network":{"id":2,"name":"CBS",
    "country":{"name":"United States","code":"US","timezone":"America/New_York"},
    "officialSite":"https://www.cbs.com/"},
    "webChannel":null,
    "dvdCountry":null,
    "externals":{"tvrage":25988,"thetvdb":264492,"imdb":"tt1553656"},
    "image":{"medium":"https://static.tvmaze.com/uploads/images/medium_portrait/81/202627.jpg","original":"https://static.tvmaze.com/uploads/images/original_untouched/81/202627.jpg"},
    "summary":"<p><b>Under the Dome</b> is the story of a small town that is suddenly and inexplicably sealed off from the rest of the world by an enormous transparent dome. The town's inhabitants must deal with surviving the post-apocalyptic conditions while searching for answers about the dome, where it came from and if and when it will go away.</p>",
    "updated":1631010933,
    "_links":{"self":{"href":"https://api.tvmaze.com/shows/1"},"previousepisode":{"href":"https://api.tvmaze.com/episodes/185054"}}
}
```
