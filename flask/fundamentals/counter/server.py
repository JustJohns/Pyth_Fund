from itertools import count
from flask import Flask, render_template, redirect, session, request
app = Flask(__name__)
app.secret_key = "aljfilejlijalijelijla"

@app.route('/')
def index():

    if "count" not in session:
        session['count'] = 0
    
    count = session['count']

    return render_template('index.html', count=count)

@app.route('/count')
def counts():
    print("1")

    # if 'count' in session:
    count = session['count']
    session['count'] = count + 1

    return render_template('index.html', count=count)

@app.route('/count+2')
def twoMore():
    count = session['count'] + 1
    session['count'] = count + 1

    return render_template('index.html', count=count)

@app.route('/destroy_session')
def destroy():



    session.clear()

    return redirect('/')

# if 'key_name' in session:
#     print('key exists!')
# else:
#     print("key 'key_name' does NOT exist")




# session.pop('key_name')





# @app.route('/reset')
# def reset():
#     session.clear()
#     return redirect('/')

if __name__=="__main__":
    app.run(debug=True)