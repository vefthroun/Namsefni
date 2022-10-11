
## Verkefni 4  

### _TVMAZE API – HTML Form_

Útfærðu vefforrit í _Flask_ sem sækir gögn ( API ) á vefsíðuna [https://www.tvmaze.com/api](https://www.tvmaze.com/api) og birtir á vefsíðu. Hér er svo dæmi um vefsíðu með svipaða virkni og lýst er hér að neðan [https://tv-maze-app2.herokuapp.com/](https://tv-maze-app2.herokuapp.com/)

Á forsíðu skal birta nafn og mynd 20 random þátta úr gagnagrunni TV Maze. Þegar 1 þáttur er valinn skal birta upplýsingar um þann þátt:

- Nafn ( name )
- Mynd ( image/medium )
- Hvenær þáttur var fyrst sýndur ( premiered )
- Hvenær þáttur var síðast sýndur ( ended )
- Stutt lýsing á þætti ( summary )

Í haus vefsíðu skulu vera hlekkir, einn sem vísar á forsíðu, annar sem vísar á síðu sem býður upp á þáttaleit. Á síðunni sem býður upp á þáttaleit skal vera form með innsláttarsvæði þar sem hægt er að leita að ákveðnum þætti. Eftir leit skulu birtast þeir þættir sem falla undir leitina í lista svipuðum og á forsíðu ( nafn og mynd). Þegar 1 þáttur er valinn í þessum lista birtast sömu upplýsingar og listaðar eru upp hér að ofan.

Í haus vefsíðu skulu einnig vera hlekkir sem vísa á flokka ( genre ) sem þættir tilheyra. Ef smellt er á einn af hlekkjunum t.d. **Action** birtast allir þeir þættir sem eru í flokknum **Action** o.s.frv. Þegar 1 þáttur er valinn í þessum lista birtast sömu upplýsingar og listaðar eru upp hér að ofan.

**Flask útfærsla**

1. Notaðu _dynamic routing_.
2. Notaðu _templates_.
3. Útfærðu HTTP _error_ síðu ef smellt er á tengil sem vísar á síðu sem er ekki til.
4. Notið myndir og css með viðeigandi hætti.

### Námsmat 14% af heildareinkunn

1. Dynamic routing ( 2% )
2. Template inheritance og include ( 2% )
3. CSS / myndir ( 2% )
4. Forsíða með 20 random þáttum ( 1% )
5. Leitarsíða sem leitar eftir þáttum ( 3% )
6. Síða sem birtir alla þætti sem tilheyra ákveðnum flokki ( genre ) ( 3% )
7. Síður sem birta nánari upplýsingar um þátt ( 1% )

### Skil

*  https://github.com/22vf/ 22h-geymslan þín/verkefni-4

Gangi þér vel!
