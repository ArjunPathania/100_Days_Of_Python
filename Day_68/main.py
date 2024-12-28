from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

# Initialize Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = b'_5#y2L"F4Q8z\n\xec]/'


# Set up SQLAlchemy database
class Base(DeclarativeBase):
    pass


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Define User model
class User(Base, UserMixin):
    """
    User model for storing user details in the database.
    Inherits from Base (DeclarativeBase) and UserMixin (Flask-Login).
    """
    __tablename__ = 'user'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))


# Create the database tables
with app.app_context():
    db.create_all()

# Configure Flask-Login
login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    """
    Callback to reload the user object from the user ID stored in the session.
    """
    return db.get_or_404(User, user_id)


# Define routes
@app.route('/')
def home():
    """
    Render the home page.
    """
    # Passing True or False if the user is authenticated.
    return render_template("index.html", logged_in=current_user.is_authenticated)


@app.route('/register', methods=["GET", "POST"])
def register():
    """
    Handle user registration. Hashes and stores the password securely.
    """
    if request.method == "POST":
        # Hash the user's password
        email = request.form.get('email')
        result = db.session.execute(db.select(User).where(User.email == email))
        # Note, email in db is unique so will only have one result.
        user = result.scalar()
        if user:
            # User already exists
            flash("You've already signed up with that email, log in instead!")
            return redirect(url_for('login'))

        hashed_password = generate_password_hash(
            request.form['password'], method="pbkdf2:sha256", salt_length=8
        )

        # Create a new user instance
        new_user = User(
            email=request.form['email'],
            name=request.form['name'],
            password=hashed_password
        )

        # Add the user to the database
        db.session.add(new_user)
        db.session.commit()

        # Flash success message and log in the user
        flash("Registration successful! You are now logged in.", "success")
        login_user(new_user)
        return redirect(url_for("secrets"))
    # Passing True or False if the user is authenticated.
    return render_template("register.html", logged_in=current_user.is_authenticated)


@app.route('/login', methods=["GET", "POST"])
def login():
    """
    Handle user login by verifying email and password.
    """
    if request.method == "POST":
        email = request.form.get('email')
        password = request.form.get('password')

        # Query the user from the database
        result = db.session.execute(db.select(User).where(User.email == email))
        user = result.scalar()

        # Check if user exists and password matches
        if not user:
            flash("That email does not exist, please try again.")
            return redirect(url_for('login'))
        elif not check_password_hash(user.password, password):
            flash('Password incorrect, please try again.')
            return redirect(url_for('login'))
        else:
            login_user(user)
            return redirect(url_for('secrets'))
    # Passing True or False if the user is authenticated.
    return render_template("login.html", logged_in=current_user.is_authenticated)


@app.route('/secrets')
@login_required
def secrets():
    """
    Render the secrets page, accessible only to logged-in users.
    """
    return render_template("secrets.html", name=current_user.name, logged_in=True)


@app.route('/logout')
def logout():
    """
    Log the user out and redirect to the home page.
    """
    logout_user()
    return redirect(url_for("home"))


@app.route('/download', methods=["POST"])
@login_required
def download():
    """
    Allow logged-in users to download a file.
    """
    return send_from_directory(
        "static", "files/cheat_sheet.pdf", as_attachment=True
    )


# Run the app
if __name__ == "__main__":
    app.run(debug=True)
