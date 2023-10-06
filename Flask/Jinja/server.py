from flask import Flask, render_template
# import random
# import datetime
import requests

app = Flask(__name__)

# @app.route('/')
# def root():
#     r =random.randint(1, 10)
#     year = datetime.datetime.now().year
#     return render_template('index.html', number=r, year=year)

@app.route('/guess/<name>')
def guess(name):
    agify = requests.get(f'https://api.agify.io?name={name}')
    age = agify.json()["age"]
    genderize = requests.get(f'https://api.genderize.io/?name={name}')
    gender = genderize.json()["gender"]
    return render_template('index.html', name=name, age=age, gender=gender)



if __name__ == '__main__':
    app.run(debug=True)