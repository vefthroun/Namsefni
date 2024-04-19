```python
    if 'Innskráður' in session:
        user = session['Innskráður']['users']
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
        flash("Þú þarft að vera innskráður til að komast í ritstjórn")
        return render_template("404.html")
```