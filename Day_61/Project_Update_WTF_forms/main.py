import os
from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from flask_bootstrap import Bootstrap
import smtplib
from dotenv import load_dotenv, find_dotenv
import requests

# Load environment variables
load_dotenv(find_dotenv())

# Environment variables
FROM_EMAIL = os.environ["FROM_EMAIL"]
PASSWORD = os.environ["PASSWORD"]
TO_EMAIL = os.environ["TO_EMAIL"]

# Flask application setup
app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default-secret-key')
Bootstrap(app)

# Form class using Flask-WTF
class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(max=50)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    phone = StringField("Phone Number", validators=[DataRequired(), Length(max=15)])
    message = TextAreaField("Message", validators=[DataRequired(), Length(max=500)])
    submit = SubmitField("Send")

# Routes
@app.route('/')
def get_all_posts():
    posts = requests.get(url='https://api.npoint.io/447af222d6804d293c72').json()
    return render_template('index.html', all_posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post/<int:index>')
def show_post(index):
    posts = requests.get(url='https://api.npoint.io/447af222d6804d293c72').json()
    requested_post = next((post for post in posts if post["id"] == index), None)
    return render_template("post.html", post=requested_post)

@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        send_email(
            form.name.data,
            form.email.data,
            form.phone.data,
            form.message.data
        )
        flash("Message sent successfully!", "success")
        return redirect(url_for('contact'))
    return render_template("contact.html", form=form)

def send_email(name, email, phone, message):
    email_message = f"Subject: New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(FROM_EMAIL, PASSWORD)
        connection.sendmail(FROM_EMAIL, TO_EMAIL, email_message)

if __name__ == '__main__':
    app.run(debug=True)
