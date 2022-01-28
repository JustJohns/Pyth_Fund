from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'alkfjjailfjajliejliajlij'
from user import User

@app.route('/')
def index():

    users = User.get_all()

    print(users)

    for user in users:
        print(user.first_name)

    return render_template('index.html', users =  users)

@app.route("/add_user")
def add_user():
    return render_template("add_user.html")

@app.route("/create_user", methods=["POST"])
def create_user():

    #1 collect info from Form
    # first_name = request.form['first_name']
    # last_name = request.form['last_name']
    # email = request.form['email']
    
    #2 repack info to send to query
    data = {
        "first_name" : request.form['first_name'],
        "last_name" : request.form['last_name'],
        "email" : request.form['email']
    }
    
    #3 call on query
    add_user_id = User.create_user(data)
    
    #4 if successful, redirect to render route
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)