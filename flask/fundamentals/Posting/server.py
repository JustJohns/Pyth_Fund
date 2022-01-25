from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "alkjeflijflikajlk;j"

@app.route('/')
def index():

    if "name" not in session:
        name = "Nanashi"
    else:
        name = session["name"]


        # if "count" not in session:
        #     session['count'] = 0

    # name = session["name"]
    # name = session["name"]
    # name = session["name"]

    return render_template('index.html', name=name)

# @app.route('/count')

@app.route('/users', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(request.form)
    print(request.form['name'])
    print(request.form['email'])
    # Never render a template on a POST request.
    # Instead we will redirect to our index route.

    # email = request.form['email']
    # age = request.form['age']
    # dojo = request.form['dojo']

    session["name"] = request.form['name']
    session["email"] = request.form['email']
    session["age"] = request.form['age']
    session["dojo"] = request.form['dojo']

    return redirect('/')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)