from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)

from user import User


@app.route('/')
def index():

    users = User.all_users()

    print(users)
    for user in users:
        print(user.first_name)
    return render_template('index.html', users = users)

@app.route("/<int:user_id>")
def user_info(user_id):
    # call get one user query
    data = {
        "user_id" : user_id
    }

    user = User.one_user(data)
    print(user)
    return render_template("show_user.html", user = user)



if __name__=="__main__":
    app.run(debug=True)