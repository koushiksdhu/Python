from flask import Flask, render_template, request
from mail import Email

app = Flask(__name__)
email_service = Email()


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        text = f'''Name: {request.form['name']}\nEmail address: {request.form['email']}\nPhone Number: {request.form['phn']}
        \nMessage: {request.form['msg']}\n\nThank you for submitting the contact form!\nWe'll revert you back soon.'''
        email_service.send_mail(request.form['email'], text)
        return render_template('submit.html', form_data=request.form)


if __name__ == '__main__':
    app.run(debug=True)
