from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/httpresponse')
def http():
    return "This is a Http Response"



if __name__=="__main__":
    app.run(debug=True)