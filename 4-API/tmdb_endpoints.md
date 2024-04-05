## Genre
https://api.themoviedb.org/3/genre/tv/list?language=en&api_key=(þinn lykill)

## Discover
https://api.themoviedb.org/3/discover/tv?api_key=(þinn lykill)&page=2

## Ákveðinn þáttur eftir ID, fáum grunnupplýsingar um "seasons"
https://api.themoviedb.org/3/tv/59941?api_key=(þinn lykill)


## Sama og hér að ofan nema tungumál
https://api.themoviedb.org/3/tv/1396?api_key=(þinn lykill)&language=is-IS


## Ákveðið season þáttaraðar, upplýsingar um alla þættina í völdu s
https://api.themoviedb.org/3/tv/59941/season/1?api_key=(þinn lykill)

## Mynd
https://image.tmdb.org/t/p/w500/g4amxJvtpnY79J77xeamnAEUO8r.jpg

## Video, virðist ekki mikið um að video séu til staðar fyrir ákveðinn þátt
https://api.themoviedb.org/3/tv/82873/videos?api_key=(þinn lykill)
https://www.youtube.com/watch?v=e890gJkoVfg  

## Leikarar þáttaraðar
https://api.themoviedb.org/3/tv/1396/credits?api_key=(þinn lykill)

## Ákveðin leikari
https://api.themoviedb.org/3/person/84497?api_key=(þinn lykill) 


## fá alla flokka (genres)
https://api.themoviedb.org/3/genre/tv/list?language=en&api_key=(þinn lykill)

## fá random myndir í völdum flokk
https://api.themoviedb.org/3/discover/movie?api_key=(þinn lykill)&with_genres=" + str(id) + "&page=" + str(random.randint(1, 500))