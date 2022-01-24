from flask import Flask, render_template  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"



@app.route("/")          # The "@" decorator associates this route with the function immediately following
def eightByEight():
    return render_template('index.html', num=1)  

@app.route("/4")          # The "@" decorator associates this route with the function immediately following
def eightByFour():

    return render_template('index.html', num=2)


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.





