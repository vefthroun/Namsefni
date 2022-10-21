from flask import Flask
app = Flask(__name__)

"""
Dynamic Routes & Variable Rules
You can use filters to be more specific.
https://flask.palletsprojects.com/en/2.1.x/quickstart/#variable-rules

    string: (default) accepts any text without a slash
    int:    accepts positive integers
    float:  accepts positive floating point values
    path:   like string but also accepts slashes
    uuid:   accepts UUID strings
"""

# matches only integers
@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post: %d' % post_id

# heiltala með sjálfgefið gildið 
@app.route('/sale/<transaction_id>')
def get_sale(transaction_id=0):
  return "The transaction is "+str(transaction_id)

# flask route with multiple parameters 
@app.route('/create/<first_name>/<last_name>')
def create(first_name=None, last_name=None):
  return 'Hello ' + first_name + ',' + last_name

# Dynamically generate article URLs based on the publication date.
# ex. http://127.0.0.1:5000/2020/3/Covid
@app.route('/<int:year>/<int:month>/<title>')
def article(year, month, title):
    #... Logic goes here
    return "%d, %d, %s" % (year, month, title) # tuple

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  # This will allow the app to display a proper Python error message, so you can fix the typo/syntax error.
  
