from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired

app = Flask(__name__)
app.secret_key = "i-am-koushik-sadhu"


class LoginForm(FlaskForm):
    email = StringField(label='email')
    password = PasswordField(label='password')
    submit = SubmitField(label='Log In')


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/login')
def login():
    login_form = LoginForm()
    login_form.validate_on_submit()
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
