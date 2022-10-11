Hypertext Transfer Protocol (HTTP) er aðferð til að senda eða taka við gögnum á veraldarvefnum. Upprunalegi tilgangurinn var að birta HTML síður, þótt núna sé HTTP notað til að hlaða niður myndum, hljóði, leikjum, textaskjölum og margmiðlun af allri gerð. Venjulega eru HTTP skilaboð alltaf í pörum (en ekki reglan frá og með HTTP/2), beiðni frá biðlara og svar frá miðlara. 

HTTP skilaboð eru byggð upp af HTTP haus og síðan gögnunum sjálfum. Til að skilja á milli gagnanna og haussins eru notuð tvö auð línubil (í útgáfum af HTTP fyrir HTTP/2). HTTP/1.1 er enn mikið notað og í nokkrum mæli næsta útgáfa HTTP, HTTP/2 sem staðlað var 2015, er studd af flestum vöfrum og t.d. netþjónum Google. Einnig er HTTP/3 ("Internet Draft") líka í notkun á vefnum nú þegar, er en sú aðferð, sem notar UDP en ekki TCP, ólíkt fyrri HTTP stöðlum, bætir hraðann enn frekar umfram HTTP/2 sem gerður var til að bæta hraðann á eldri HTTP staðli. 

Allar þessar aðferðir þurfa bæði stuðning í vöfrum sem notaðir eru, en líka á miðlara ("web server"). Hvaða aðferð er í raun notuð er ekki augljóst fyrir notanda (ólíkt dulkóðuðu HTTPS; þó nota staðlarnir HTTP/2 og nýrri í reynd HTTPS). HTTPS þýðir aðeins að notuð sé örugg útgáfa af HTTP, t.d. HTTP/1.1 (eða nýrri); S-ið í lokin stendur fyrir secure.  [Sjá nánar á wikipedia](https://is.wikipedia.org/wiki/HTTP)

---

Hypertext Transfer Protocol (HTTP) is an application-layer protocol for transmitting hypermedia documents, such as HTML. It was designed for communication between web browsers and web servers, but it can also be used for other purposes. HTTP follows a classical client-server model, with a client opening a connection to make a request, then waiting until it receives a response. HTTP is a stateless protocol, meaning that the server does not keep any data (state) between two requests. 

---

* [HTTP Basics](https://code.tutsplus.com/tutorials/http-the-protocol-every-web-developer-must-know-part-1--net-31177)
* [An overview of HTTP](https://developer.mozilla.org/en-US/docs/Web/HTTP/Overview)
* [HTTP skilaboð](https://httpstatuses.com/)
* [HTTP3 the past present and future](https://blog.cloudflare.com/http3-the-past-present-and-future/)
* [Network Monitor, Mozilla](https://developer.mozilla.org/en-US/docs/Tools/Network_Monitor)
* [Network Monitor, Google](https://developer.chrome.com/docs/devtools/network/)

---



