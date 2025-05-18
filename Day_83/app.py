import json
import smtplib
from datetime import datetime
from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Email, Length
from dotenv import load_dotenv, find_dotenv
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ['SECRET_KEY']

# Load environment variables
load_dotenv(find_dotenv())

# Email configuration from environment variables
FROM_EMAIL = os.environ["FROM_EMAIL"]
PASSWORD = os.environ["PASSWORD"]
TO_EMAIL = os.environ["TO_EMAIL"]


class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(max=50)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    phone = StringField("Phone Number", validators=[
                        DataRequired(), Length(max=15)])
    message = TextAreaField("Message", validators=[
                            DataRequired(), Length(max=500)])
    submit = SubmitField("Send")


def load_projects():
    data_path = os.path.join(app.root_path, 'static',
                             'data', 'projects.json')  # Adjust path as needed
    with open(data_path, 'r') as f:
        projects = json.load(f)
    return projects


def send_email(name, email, phone, message):
    """Send an email with contact form details."""
    email_message = f"Subject: New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(FROM_EMAIL, PASSWORD)
        connection.sendmail(FROM_EMAIL, TO_EMAIL, email_message)


@app.route("/", methods=["GET", "POST"])
def index():
    form = ContactForm()

    projects = load_projects()

    if form.validate_on_submit():
        flash("Message sent successfully!", "success")
        send_email(
            name=form.name.data,
            email=form.email.data,
            phone=form.phone.data,
            message=form.message.data
        )
        return redirect(url_for("index"))

    return render_template("index.html", form=form, projects=projects, current_year=datetime.now().year)


# Run the app
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
