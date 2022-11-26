### Form 
1. [Web forms — Working with user data (HTML)](https://developer.mozilla.org/en-US/docs/Learn/Forms)
1. [Kóðasýnidæmi með Flask](https://github.com/vefthroun/Namsefni/tree/main/5-FORM/FORM)
<!-- 1. [flask.Request](https://tedboy.github.io/flask/generated/generated/flask.Request.html) -->

---

### WTForms
[WTForms](https://wtforms.readthedocs.io/en/3.0.x/) is a flexible forms validation and rendering library for Python web development. It can work with whatever web framework and template engine you choose. It supports data validation, CSRF protection, internationalization (I18N), and more. There are various community libraries that provide closer integration with popular frameworks.  

The [Flask-WTF](https://flask-wtf.readthedocs.io/en/1.0.x/) extension uses Python classes to represent web forms. `(venv) $ pip3 install flask-wtf`.

1. [Handling Forms in Flask with Flask-WTF](https://hackersandslackers.com/flask-wtforms-forms/) _(vefgrein)_
1. Login [The Flask Mega-Tutorial:  Web Forms](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-iii-web-forms) _(vefgrein), notar flash message_
1. Login sýnidæmi _(youtube)_
   1. [Introduction to WTForms in Flask (login)](https://www.youtube.com/watch?v=vzaXBm-ZVOQ) og _[kóðinn](https://github.com/vefthroun/Namsefni/blob/main/WTForms/1_login.py)_
   1. [Using Validators in Flask-WTF](https://youtu.be/jR2aFKuaOBs) og _[kóðinn](https://github.com/PrettyPrinted/youtube_video_code/tree/master/2017/04/24/Using%20Validators%20in%20Flask-WTF%20(Part%202%20of%205)/wtf_validators)_
   1. [Creating a Macro to Reduce Code Duplication](https://youtu.be/J9O0v-iM0TE) og _[kóðinn](https://github.com/PrettyPrinted/youtube_video_code/tree/master/2017/04/28/Flask-WTF%20-%20Creating%20a%20Macro%20to%20Reduce%20Code%20Duplication%20(4%20of%205))_
1. [Forms and User Input (48 mín)](https://www.youtube.com/watch?v=UIJKdCIEXUQ) _(youtube)_ og [kóðaskrár](https://github.com/CoreyMSchafer/code_snippets/tree/master/Python/Flask_Blog/03-Forms-and-Validation) _býr til form.py fyrir klasana, notar flash message_
1. Signup sýnidæmi: [WTForms validation and rendering in Flask (27 mín)](https://www.youtube.com/watch?v=j5IQI4aW9ZU) _(youtube)_ 

<!--
1. [How to validate and use WTForms í Flask](https://www.digitalocean.com/community/tutorials/how-to-use-and-validate-web-forms-with-flask-wtf)
1. [FLASK CRUD From scratch, wtform + editor (gamall)](https://www.youtube.com/watch?v=zRwy8gtgJ1A&t=54s&ab_channel=TraversyMedia) _youtube_ og [kóði](https://github.com/bradtraversy/myflaskapp) 
-->

#### Punktar:

- When the `action` is set to an empty string the form is submitted to the URL that is currently in the address bar, which is the URL that rendered the form on the page. 
- From WTForms 2.3.0 version, the email validation is handled by an external library called email-validator `pip install email-validator`


---

### WYSIWYG HTML editor

WYSIWYG HTML editor is designed to simplify website content creation. WYSIWYG is a type of editing software that allows users to see and edit content in a form that appears as it would when displayed on an interface like a webpage. It has the ability to convert HTML text area fields or other HTML elements to editor instances. WYSIWYG is an acronym for "what you see is what you get."

#### CKEditor 
1. [CKEditor](https://ckeditor.com/)
   - [Online Demo](https://ckeditor.com/ckeditor-5/demo/), [kóðasýnidæmi](https://ckeditor.com/docs/ckeditor5/latest/installation/getting-started/quick-start.html) og [Docs](https://ckeditor.com/docs/)
1. [Flask CKEditor](https://flask-ckeditor.readthedocs.io/en/latest/)
   1. [How To Add A Rich Text Editor and Basic usage](https://www.youtube.com/watch?v=5jnAnnxZGQQ&ab_channel=Codemy.com) _myndband_
   1. [Edit Blog Posts With Rich Text Editor](https://www.youtube.com/watch?v=3QkEjJdWoGA&ab_channel=Codemy.com) _myndband_

#### TinyMCE
1. [What is TinyMCE?](https://www.tiny.cloud/docs/tinymce/6/introduction-to-tinymce/)
1. [WtForms + TinyMCE](https://pypi.org/project/wtf-tinymce/)
1. [WTForms + Tiny kóðalausn](https://github.com/azsoftware/wtf-tinymce/tree/develop/examples/flask_app_example) 

<!--
1. [TinyMCE and Flask with WTForm](https://www.kevin7.net/post_detail/tinymce-and-flask)
1. [Flask-TinyMCE 1.0.0](https://pypi.org/project/Flask-TinyMCE/#description)
-->
