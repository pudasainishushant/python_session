from flask import Flask,request,render_template, redirect, url_for
from werkzeug.utils import redirect
from weki import WekiModule
app = Flask(__name__)
wiki_obj = WekiModule()

data = []

@app.route("/",methods = ['GET','POST'])
def index():
    if request.method == 'POST':
        search = request.form["search"]
        print("",search)
        return redirect(url_for("search",search_query=search))
    else:
        return render_template('index.html')

@app.route("/query/<search_query>",methods = ['GET','POST'])
def search(search_query):
    print(search_query)
    returneddta = wiki_obj.generatesumary(search_query)
    print("Aba yo data render garna sika results.html ma hai suan bhai")
    print(returneddta)
    return render_template('results.html')


app.run(debug=True)

