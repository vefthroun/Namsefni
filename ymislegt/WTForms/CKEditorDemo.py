from flask import Flask, render_template, url_for
# Fields
from wtforms import StringField, TextAreaField
#from wtforms.widgets import TextArea
from wtforms.validators import InputRequired, Length
from flask_wtf import FlaskForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "Lykill"

class ArticleForm(FlaskForm):
    titill = StringField("titill", validators=[InputRequired()])
    texti = TextAreaField("texti", validators=[Length(min=20)])
#    texti = StringField('texti', widget=TextArea())

@app.route('/add', methods=["GET","POST"])
def addArticle():
    article = ArticleForm()
    if article.validate_on_submit():
        return "Það tókst"
    return render_template("form.html", article=article)  

if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)   
           
"""
form.html

<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <script src="https://cdn.ckeditor.com/ckeditor5/35.3.0/classic/ckeditor.js"></script>
    <title>CKEditor demo</title>
</head>
<body>
    <form method="POST", action="{{ url_for('addArticle') }}">
        <!-- Cross Site Request Forgery protection --> 
        {{ article.csrf_token }}
        {{ article.titill.label }}
        {{ article.titill }}
        {{ article.texti(id="editor") }} 
        <input type="submit" value="Submit">
    </form>
    <script>
        ClassicEditor
            .create( document.querySelector( '#editor' ) )
            .catch( error => {
                console.error( error );
            } );
    </script>
</body>
</html>

"""

"""
forsíða.html
{{ article.texti | safe}}

"""
