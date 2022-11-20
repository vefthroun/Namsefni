### Cookies

* cookie expires at the end of the browser session or as soon as the browser window is closed. 
* cookies are stored at client side and are not encrypted in any way. Never store confidential information in cookies (XSS vulnerabilities).

#### Sýnidæmi

<!--1. [Flask cookies (vefgrein)](https://pythonise.com/series/learning-flask/flask-cookies)-->
1. [Get and set cookies with Flask](https://pythonbasics.org/flask-cookies/)
1. [Cookies kóðasýnidæmi](https://github.com/vefthroun/Namsefni/tree/main/5-Cookies%26Sessions/Cookies)
1. [What is makeresponse](https://www.educative.io/answers/what-is-flaskmakeresponse)
1. [Flask make response](https://www.educba.com/flask-make_response/)

---

### Sessions
- sessions in Flask are a way to store information about a specific user from one request to the next.
- sessions work by storing a cryptographically signed cookie on the users browser and decoding it on every request.
- The session object is NOT a secure way to store data. It's a base64 encoded string and can easily be decoded.

#### Sýnidæmi

1. [An Introduction to Sessions in Flask (myndband)](https://www.youtube.com/watch?v=T1ZVyY1LWOg) _private?_
1. [Kóðasýnidæmi](https://github.com/vefthroun/Namsefni/tree/main/5-Cookies%26Sessions/Sessions) 
1. [Sessions in Flask](https://overiq.com/flask-101/sessions-in-flask/)
1. [Hvar geymir Flask session?](https://stackoverflow.com/questions/52677755/where-does-flask-store-the-sessions)

<!--1. [The Flask session object](https://pythonise.com/series/learning-flask/flask-session-object)-->

