from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = 'aijefiljaljailjeiljfal;jl'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    # Never render a template on a POST request.
    # Instead we will redirect to our index route
    session["name"] = request.form['name']
    session["dojo"] = request.form['dojo']
    session["language"] = request.form['language']
    session["comment"] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def result():
    return render_template('result.html')

@app.route('/reset')
def reset():
    session.clear()
    return redirect('/')


if __name__=="__main__":
    app.run(debug=True)