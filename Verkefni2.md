## Verkefni 2

### Templates - Dynamic routing – static files

Útfærðu vefforrit í _Flask_ sem heldur utan um fréttir og birtir. Á "_index_" síðu vefs skal birtast yfirlit allra frétta í lista. Þegar ein ákveðin frétt er valin (hlekkur fyrir frétt valin) birtist sú frétt með sinni fyrirsögn, megin texta fréttar og fréttamanni ásamt mynd sem tengist frétt. Athugaðu eftirfarandi:

**Gögnin / fréttalistinn / myndir**

1. Notaðu gagnagrind (_data structure_) sem fylgir verkefninu, þú mátt breyta innihaldi gagnagrindarinnar.
2. Gagnagrindin er listi sem inniheldur json hluti (dict í python). Gagnagrindina er að finna í [Námsefni/2-Flask](https://github.com/vefthroun/Namsefni/blob/main/2-Flask/Static/frettir.py).
3. Notaðu myndir að eigin vali (innan skynsamlegra marka þó). Í [Námsefni/2-Flask](https://github.com/vefthroun/Namsefni/blob/main/2-Flask/Static/) eru myndir sem þú getur notað. Þegar einstaka frétt er valin þarf að birtast mynd sem tengist frétt.

**Flask útfærsla**

1. Notaðu _dynamic routing_ þegar vefsíða þarf að birta eina ákveðna frétt sem valin er af _index_ síðu.
2. Notaðu _template_ til að útfæra verkefnið.
3. Notaðu _include_ og _template inheritance_til að hanna útlit síðunnar (_header, footer_).
   1. Í hausi ( header ) vefsíðu skal vera valmynd. Valmynd skal innihalda hlekki fyrir hvern flokk frétta úr gagnagrindinni. Dæmi: ef notandi vefsíðu velur hlekkinn **Íþróttir** úr valmynd birtist síða einungis með fréttum úr flokknum **sport** úr gagnagrindinni.
   2. Fótur ( footer ) skal innihalda upplýsingar um höfund verkefnis.
4. Notaðu myndir og css stílsíður á viðeigandi hátt.
   1. Notaðu mismunandi litaþema fyrir hvern fréttaflokk fyrir sig. Dæmi: ef birtar eru fréttir úr flokknum **sport** verða haus og fótur með ákveðnum lit. Ef birtar eru fréttir úr flokknum **veidi** verður litur á haus og fæti öðruvísi o.s.frv.
5. Útfærðu HTTP _error_ síðu ef smellt er á tengil sem vísar á síðu sem er ekki til.

### Námsmat 14% af heildareinkunn

1. Routing útfærsla ( 4% )
2. Template útfærsla ( 4% )
3. CSS ( 2% )
4. Myndanotkun ( 2% )
5. HTTP error 404 ( 2% )

### Skil

[Github.com/22VF](https://github.com/22vf) – Öll gögn sem notuð eru í verkefni 2.


_Gangi þér vel_
