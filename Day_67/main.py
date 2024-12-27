from bleach import clean
from flask import Flask, render_template, redirect, url_for, flash, jsonify, request
from flask_bootstrap import Bootstrap5
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Text
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField ,TextAreaField
from wtforms.validators import DataRequired, URL ,Email,Length
from markupsafe import Markup #
import smtplib , os
from dotenv import load_dotenv,find_dotenv
from flask_ckeditor import CKEditor,CKEditorField
from datetime import date

load_dotenv(find_dotenv())

# Environment variables
FROM_EMAIL = os.environ["FROM_EMAIL"]
PASSWORD = os.environ["PASSWORD"]
TO_EMAIL = os.environ["TO_EMAIL"]

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)
ckeditor = CKEditor(app)
app.config['CKEDITOR_SERVE_LOCAL'] = True
app.config['CKEDITOR_PKG_TYPE'] = 'standard'
app.config['CKEDITOR_CONFIG'] = {'versionCheck': False}

# CREATE DATABASE
class Base(DeclarativeBase):
    pass
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///posts.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# CONFIGURE TABLE
class BlogPost(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    subtitle: Mapped[str] = mapped_column(String(250), nullable=False)
    date: Mapped[str] = mapped_column(String(250), nullable=False)
    body: Mapped[str] = mapped_column(Text, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    img_url: Mapped[str] = mapped_column(String(250), nullable=False)



with app.app_context():
    db.create_all()

# Form class using Flask-WTF
class ContactForm(FlaskForm):
    name = StringField("Name", validators=[DataRequired(), Length(max=50)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    phone = StringField("Phone Number", validators=[DataRequired(), Length(max=15)])
    message = TextAreaField("Message", validators=[DataRequired(), Length(max=500)])
    submit = SubmitField("Send")

class BlogForm(FlaskForm):
    title = StringField(Markup('<b>Blog Post Title</b>'), validators=[DataRequired(), Length(max=50)])
    subtitle = StringField(Markup('<b>Subtitle</b>'), validators=[DataRequired(),Length(max=50)])
    author = StringField(Markup('<b>Your Name</b>'), validators=[DataRequired(), Length(max=50)])
    img_url = StringField(Markup('<b>Blog Image URL</b>'), validators=[DataRequired(), URL()])
    body = CKEditorField(Markup('<b>Blog Content</b>'), validators=[DataRequired(), Length(max=2500)])
    submit = SubmitField('Submit Post')


@app.route('/')
def get_all_posts():
    # Query the database for all the posts. Convert the data to a python list.
    result = db.session.execute(db.select(BlogPost))
    posts = result.scalars().all()
    return render_template("index.html", all_posts=posts)

# Add a route so that you can click on individual posts.
@app.route('/<int:post_id>')
def show_post(post_id):
    #Retrieve a BlogPost from the database based on the post_id
    requested_post = db.get_or_404(BlogPost,post_id)
    return render_template("post.html", post=requested_post)

# add_new_post() to create a new blog post
@app.route('/new-post', methods=["GET", "POST"])
def add_new_post():
    form = BlogForm()
    if form.validate_on_submit():
        try:
            sanitized_body = clean(
                form.body.data,
                tags=['p', 'b', 'i', 'strong', 'ul', 'li', 'ol', 'a'],
                attributes={'a': ['href']}
            )
            new_post = BlogPost(
                title=form.title.data,
                subtitle=form.subtitle.data,
                body=sanitized_body,
                img_url=form.img_url.data,
                author=form.author.data,
                date=date.today().strftime("%B %d, %Y")
            )
            db.session.add(new_post)
            db.session.commit()
            flash("New post added successfully!", "success")
            return redirect(url_for("get_all_posts"))
        except Exception as e:
            db.session.rollback()
            flash("An error occurred while adding the post. Please try again.", "danger")
            return jsonify(error={e})
    return render_template('make-post.html', form=form)


# edit_post() to change an existing blog post
@app.route("/edit-post/<int:post_id>", methods=["GET", "POST"])
def edit_post(post_id):
    post = db.get_or_404(BlogPost, post_id)
    # Auto-populate the form fields for an existing post (by passing a BlogForm() object with prefilled data as form)
    edit_form = BlogForm(
        title=post.title,
        subtitle=post.subtitle,
        img_url=post.img_url,
        author=post.author,
        body=post.body
    )
    if edit_form.validate_on_submit():
        try:
            sanitized_body = clean(
                edit_form.body.data,
                tags=['p', 'b', 'i', 'strong', 'ul', 'li', 'ol', 'a'],
                attributes={'a': ['href']}
            )
            post.title=edit_form.title.data
            post.subtitle=edit_form.subtitle.data
            post.body=sanitized_body
            post.img_url=edit_form.img_url.data
            post.author=edit_form.author.data
            post.date=post.date
            db.session.commit()
            flash("New post added successfully!", "success")
            return redirect(url_for("show_post", post_id=post.id))
        except Exception as e:
            db.session.rollback()
            flash("An error occurred while adding the post. Please try again.", "danger")
            return {"error":f"{e}"}
    return render_template("make-post.html", form=edit_form, is_edit=True)


# delete_post() to remove a blog post from the database
@app.route("/delete/<int:post_id>")
def delete_post(post_id):
    post_to_delete = db.get_or_404(BlogPost, post_id)
    db.session.delete(post_to_delete)
    db.session.commit()
    return redirect(url_for('get_all_posts'))



# Below is the code from previous lessons. No changes needed.
@app.route("/about")
def about():
    return render_template("about.html")

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


if __name__ == "__main__":
    app.run(debug=True, port=5003)
