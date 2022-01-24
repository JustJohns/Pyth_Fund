from flask import Flask, render_template
app = Flask(__name__)    # Create a new instance of the Flask class called "app"



@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template('index.html', phrase="hello", times=5)  # Return the string 'Hello World!' as a response

@app.route('/say/<name>')
def say_Hi(name):
    print(name)
    return "Hi " + name + "!"


if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.
