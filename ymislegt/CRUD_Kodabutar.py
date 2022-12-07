# Að lesa úr gagnagrunni 

blog = list(db.child("blogs").get().val().values())[::-1]


    {% for i in blog %}
            <div class="blog">
                <h2>{{ i["title"] }}</h2>
                {{ i["content"]|safe }}
  
            </div>
        {% endfor %}



---


mottekid = db.child("greinar").get()
    global greinar # greinar = {}
    for grein in mottekid.each():
        # print(grein.val()) # {'texti': 'qwerqwerqwerqwer\r\n', 'titill': 'werwerwer'}
        greinar[(grein.val()["titill"])] = grein.val()["texti"]

{% for titill,grein in greinar.items() %}
    <div class="center">
        <h1>{{ titill|safe }}</h1>
        {{ grein|safe }}
    </div>
{% endfor %}




----



 quoteList = []
  quote = db.child("quotes").get()
  for i in quote.each():
    quoteDict = {"content": i.val()["content"], "author": i.val()["author"]}
    quoteList.append(quoteDict)

{% block content %}
<div class="center">
    <div class="pure-g">
        {% for x in quoteList %}
            <div class="pure-u-sm-4 quotes">
                <h3>,,{{x["content"]}}''</h3>
                <small>-{{x["author"]}}</small>
            </div>
        {% endfor %}
    </div>
</div>
{% endblock %}




----



  article_data = []
  
    articles =  db.child('Article data').get()
    try:
      for article in articles.each():
          data = article.val()
          article_data.append(data)
      article_data.reverse()
    except:
      pass



---



posts=db.child("Posts").get()

{% for article in posts.each() %}
            <div class="pure-u-1 pure-u-md-1-3 l-box">
                <h3> {{ article.val()['Title'] }}</h3>
                <h4> {{ article.val()['Username'] }}</h4>
                <h5> {{ article.val()['Text'] }}</h5>
            </div>
        {% endfor %}
        


--------







# Að skrifa í gagnagrunn

if form.is_submitted():
        gogn["titill"] = remove_html_tags(form.title.data)
        gogn["texti"] = remove_html_tags(form.body.data)
        db.child("greinar").push(gogn)



---



if not session.get("user") is None:
        if form.is_submitted():
            json_data = {
                'title': form.title.data,
                'content': form.content.data
                }
            new_path = db.child("blogs/").push(json_data)
            return redirect("/")



---



data = {
        'title': article.title.data,
        'content': request.form.get('ckeditor')
      }
      db.child('Article data').push(data)



---



   form.Title.data))
        dicta={}
        dicta["Title"]=form.Title.data
        dicta["Username"]=session['email']
        dicta["Text"]=form.Text.data
        
        db.child("Posts").push(dicta)

-----------

@app.route("/skra_ut/")
def skra_ut():
    session.pop("email",None)
    nav.pop("Skrá út")
    return redirect(url_for("login"))
