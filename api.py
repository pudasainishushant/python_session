import flask
from flask import render_template
from flask.globals import request
from flask.json import jsonify


app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route("/",methods=["POST","GET"])
def home():
    query = requests.form["query"]
    summary = generate_summary(query)
    return render_template("index.html",{"summary":summary})

@app.route("/get_profile",methods = ["GET","POST"])
def get_profile():
    """
- Connect to that database
- Perform query to get data from the database
SELECT USER_PROFILE FROM USERTABLE.TABLE
- userprofilecollection.get("Umesh KC")
"""
    print("hahhahahahahaha")
    umesh_profile_data = {
        "name":"Umesh KC",
        "profile_pic":"dsjagh",
        "Works at":"Facebook",
        "Lives in":"Sydney"
    }
    return jsonify(umesh_profile_data)

login_users = {"umesh@gmail.com":"umes123","sujan@gmail.com":"sujan123","shushant@gmail.com":"shushant123"}

@app.route("/login",methods = ["GET","POST"])
def login():
    # 
    user_email = request.form["email"]
    password = request.form["password"]
    if user_email in login_users.keys():
        if password == login_users[user_email]:
            return jsonify("Login succefull")
        else:
            return jsonify("Password Milena")
    else:
        return jsonify("Yo user nai xaina")

app.run()