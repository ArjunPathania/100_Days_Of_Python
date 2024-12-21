import os

from flask import Flask,render_template,request
import requests,smtplib
from dotenv import load_dotenv,find_dotenv

load_dotenv(find_dotenv())

FROM_EMAIL = os.environ["FROM_EMAIL"]
PASSWORD = os.environ["PASSWORD"]
TO_EMAIL = os.environ["TO_EMAIL"]
app = Flask(__name__)

posts  = requests.get(url='https://api.npoint.io/447af222d6804d293c72').json()
print(posts)

@app.route('/')
def get_all_posts():
    return render_template('index.html',all_posts = posts)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in posts:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["phone"], data["message"])
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html")

def send_email(name, email, phone, message):
    email_message = f"Subject:New Message\n\nName: {name}\nEmail: {email}\nPhone: {phone}\nMessage:{message}"
    with smtplib.SMTP("smtp.gmail.com",587) as connection:
        connection.starttls()
        connection.login(FROM_EMAIL, PASSWORD)
        connection.sendmail(FROM_EMAIL,TO_EMAIL, email_message)

if __name__ =='__main__':
    app.run(debug=True)