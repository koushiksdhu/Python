from flask import Flask

app = Flask(__name__)

def bold(function):
    def wrapper():
        function()
    return f"<b>{wrapper}</b>"

def emphasis(function):
    def wrapper():
        function()
    return f"<em>{wrapper}</em>"

def underline(function):
    def wrapper():
        function()
    return f"<u>{wrapper}</u>"



@app.route('/')
@underline
@
def root():
    return '<h1 style="text-align: center; color: red;">This is the root path.</h1>' \
        '<p>This is a paragraph.</p>' \
        '<img src="https://media.giphy.com/media/njtPBlbYnHAHK/giphy.gif" alt="Giphy Animation">'