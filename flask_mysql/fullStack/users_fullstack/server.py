from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'alkfjjailfjajliejliajlij'
from user import User

#============================================
# 1. Get all users from database
#============================================

@app.route('/')
def index():

    users = User.get_all()

    print(users)

    for user in users:
        print(user.first_name)

    return render_template('index.html', users =  users)

#============================================
# 2. Get add one user from database
#============================================

@app.route("/user/add_user")
def add_user():
    return render_template("add_user.html")

@app.route("/user/create_user", methods=["POST"])
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
    User.create_user(data)
        
    #4 if successful, redirect to render route
    return redirect("/")

# #============================================
# # 3. Get one user from database
# #============================================

@app.route("/user/show/<int:user_id>")
def user_info(user_id):
    # Call on one_user query
    data = {
        "user_id" : user_id
    }
    user = User.one_user(data)

    return render_template("user_info.html", user = user)

# #============================================
# # 4. Edit one user from database
# #============================================
@app.route("/user/edit/<int:user_id>")
def edit_user(user_id):
    #1 collect info from Form
    #2 repack info to send to query
    data = {
        "user_id" : user_id
    }
    print(User.one_user(data))
    #3 call on query
    return render_template("edit_user.html", user = User.one_user(data))

@app.route("/user/update", methods=['POST'])
def update():
    
    User.update(request.form)
    # print(user)
    return redirect("/")

# #============================================
# # 5. Delete one user from database
# #============================================

@app.route("/user/delete/<int:user_id>")
def delete(user_id):
    data = {
        "user_id" : user_id
    }

    return render_template("user_info.html", user = User.delete(data))

if __name__=="__main__":
    app.run(debug=True)