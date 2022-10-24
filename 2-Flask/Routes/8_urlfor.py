
from flask import Flask, url_for
app = Flask(__name__)


# Í stað þess að harðkóða tengla í html t.d. <a href="/sida1"> Tengill á síðu 1</a>
# Þá getum við notað url_for fall fyrir url bindingu (auðveldara að uppfæra tengla)
# https://youtu.be/Ofy_jRHE3no?list=PLXmMXHVSvS-CoYS177-UvMAQYRfL3fBtX


@app.route('/')
def index():
    return "The index"       # The index

@app.route('/sida1')
def sida1():
    # vísar í routið sem geymir index fallið og skilar því urli
    return url_for("index")  # /

@app.route('/sida2')
def sida2():
    # vísar í routið sem geymir sida3 fallið og skilar því urli
    return url_for("sida3", name="Gunnar")  # /sida3/Gunnar

@app.route('/sida3/<string:name>')
def sida3(name):
    return "The name is " + name  # The name is Gunnar


# Vísun í static möppu sem inniheldur CSS skrá (auðveldara að nota með template):  
# url_for('static', filename='style.css') 

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  
