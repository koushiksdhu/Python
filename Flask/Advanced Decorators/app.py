from flask import Flask

app = Flask(__name__)

# Different routes using the app.route() decorators.


@app.route('/')
def root():
    return '<h1 style="text-align: center; color: red;">This is the root path.</h1>' \
        '<p>This is a paragraph.</p>' \
        '<img src="https://media.giphy.com/media/njtPBlbYnHAHK/giphy.gif" alt="Giphy Animation">'

# Flask framework determines which of the methods to call.


@app.route('/home')
def bye():
    return '<h2>This is the home path.</h2>'

# Variable name passing through route

# Creating variable paths and converting the path to a specified data type.


@app.route('/<fname>/<lname>')
def greet(fname, lname):
    return '<h3>f"Good Morning, {fname} {lname}"</h3>'


@app.route('/<name>/<int:age>')
def name(name, age):
    return f"Hello, I am {name}. My age is {age} years old!"


# This also works in same way as flask run works in terminal.
if __name__ == "__main__":
    # app.run()

    # Run the app in debug mode to auto-reload the server.
    app.run(debug=True)
