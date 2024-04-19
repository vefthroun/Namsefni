# tímasetning úr firebase auth

Þegar þú hefur náð sambandi við firebase authentication í gegnum fyrirspurnina

> login = auth.sign_in_with_email_and_password(email, password)

Þá er hægt að ná í upplýsingar um reikninginn            

> info = auth.get_account_info(login['idToken'])

`pprint(info)`

```

{'kind': 'identitytoolkit#GetAccountInfoResponse',
 'users': [{'createdAt': '1713347947517',
            'disabled': False,
            'email': 'test@test.is',
            'emailVerified': False,
            'lastLoginAt': '1713457239154',
            'lastRefreshAt': '2024-04-18T16:20:39.154Z',
            'localId': '3Cj6hRRHkohNazmPIcmdIh650wy2',
            'passwordHash': 'UkVEQUNURUQ=',
            'passwordUpdatedAt': 1713347947517,
            'providerUserInfo': [{'email': 'test@test.is',
                                  'federatedId': 'test@test.is',
                                  'providerId': 'password',
                                  'rawId': 'test@test.is'}],
            'validSince': '1713347947'}]}
```
Þessar upplýsingar getum við flutt inn í _session_

> session['Innskráður'] = info

og sendum _session_ á route sem tjékkar á hvort _session_ sé með eða ekki. 

Ef _session_ er til þá náum við í upplýsingarnar úr idToken  

```python
    if 'Innskráður' in session:
        user = session['Innskráður']['users'] #idToken
        timest=user[0]["createdAt"] # ná í timestamp
        timinn=int(timest)          # breyta í numbers
        timidate=datetime.fromtimestamp(timinn/1000) # /1000 losna við millisek
        time=(timidate.strftime("%#d/%#m, %Y. Kl. %H:%M")) # breyta í isl tímaröð

        login=user[0]['lastLoginAt']
        timinlog=int(login)
        timidate=datetime.fromtimestamp(timinlog/1000)
        timelog=(timidate.strftime("%#d/%#m, %Y. Kl. %H:%M"))
        
        return render_template("editor.html", firsttime=time, timelog=timelog, t=title)
    else:
        flash("Þú þarft að vera innskráður til að komast í ritstjórn") # Ef _session_ fylgir ekki með
        return render_template("404.html")
```