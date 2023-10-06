from flask import Flask, render_template
import requests

app = Flask(__name__)

req = requests.get('https://api.npoint.io/c7d6121a0a75fe372932')
blogs = req.json()

@app.route('/blog')
def blog():
    return render_template('index.html', blogs=blogs)

@app.route('/post/<id>')
def post(id):
    return render_template('post.html', blogs=blogs, id=int(id))

if __name__ == '__main__':
    app.run(debug=True)
