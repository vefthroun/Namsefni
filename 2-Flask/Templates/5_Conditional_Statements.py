from flask import Flask, render_template
app = Flask(__name__)

# Jinja2: Conditional Statements
# https://python-web.teclado.com/section07/lectures/06_jinja2_conditional_statements/#jinja2-conditional-statements

@app.route('/')
def index():
    # data
    #company = "Apple"   # 
    company = "Google"
    return render_template("template5.html", title="skilyrðissetningar", company=company)

if __name__ == '__main__':
  app.run(debug=True, use_reloader=True)  
    
