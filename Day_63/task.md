# Task: Build a "My Library" Web Application with SQLAlchemy

## Objective
Create a web application that allows users to manage their favorite books. Users can add, edit, and delete books, as well as assign ratings to them. The app uses SQLAlchemy for database interactions and Flask for the web interface.

---

## Steps

### 1. Set Up the Database
#### Tasks:
- Create an SQLite database named `books.db`.
- Define a `Book` model with the following attributes:
  - `id` (Integer, primary key)
  - `title` (String, unique, required)
  - `author` (String, required)
  - `rating` (Float, required)

#### Example Code:
```python
class Book(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    author: Mapped[str] = mapped_column(String(250), nullable=False)
    rating: Mapped[float] = mapped_column(Float, nullable=False)

with app.app_context():
    db.create_all()
```

### 2. Implement the Home Page
#### Tasks:
- Create a route for `/` to display all books in the database.
- Query the database for all books and pass them to the `index.html` template.

#### Example Code:
```python
@app.route('/')
def home():
    result = db.session.execute(db.select(Book).order_by(Book.title))
    all_books = result.scalars().all()
    return render_template("index.html", books=all_books)
```

#### Example HTML (`index.html`):
- Display books in a table with options to edit or delete each book.
```html
<table>
    <thead>
        <tr>
            <th>Title</th>
            <th>Author</th>
            <th>Rating</th>
            <th>Actions</th>
        </tr>
    </thead>
    <tbody>
        {% for book in books %}
        <tr>
            <td>{{ book.title }}</td>
            <td>{{ book.author }}</td>
            <td>{{ book.rating }}</td>
            <td>
                <a href="/edit?id={{ book.id }}">Edit</a>
                <a href="/delete?book_id={{ book.id }}">Delete</a>
            </td>
        </tr>
        {% endfor %}
    </tbody>
</table>
```

### 3. Add New Books
#### Tasks:
- Create a route for `/add` to handle adding new books.
- Use a `POST` request to submit a form with the book's title, author, and rating.

#### Example Code:
```python
@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        new_book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=request.form["rating"]
        )
        db.session.add(new_book)
        db.session.commit()
        return redirect(url_for('home'))
    return render_template('add.html')
```

#### Example HTML (`add.html`):
```html
<form method="POST">
    <label for="title">Title:</label>
    <input type="text" id="title" name="title" required>

    <label for="author">Author:</label>
    <input type="text" id="author" name="author" required>

    <label for="rating">Rating:</label>
    <input type="number" id="rating" name="rating" step="0.1" required>

    <button type="submit">Add Book</button>
</form>
```

### 4. Edit Book Ratings
#### Tasks:
- Create a route for `/edit` to handle editing book ratings.
- Use a form to update the rating of a selected book.

#### Example Code:
```python
@app.route("/edit", methods=["GET", "POST"])
def edit():
    if request.method == "POST":
        book_id = request.form["id"]
        book_to_update = db.get_or_404(Book, book_id)
        book_to_update.rating = request.form["rating"]
        db.session.commit()
        return redirect(url_for('home'))
    book_id = request.args.get('id')
    book_selected = db.get_or_404(Book, book_id)
    return render_template("edit.html", book=book_selected)
```

#### Example HTML (`edit.html`):
```html
<form method="POST">
    <input type="hidden" name="id" value="{{ book.id }}">

    <label for="rating">Rating:</label>
    <input type="number" id="rating" name="rating" value="{{ book.rating }}" step="0.1" required>

    <button type="submit">Update Rating</button>
</form>
```

### 5. Delete Books
#### Tasks:
- Create a route for `/delete` to handle deleting books by ID.
- Redirect to the home page after deletion.

#### Example Code:
```python
@app.route("/delete")
def delete():
    book_id = request.args.get('book_id')
    if not book_id:
        return "Book ID is required", 400
    book_to_delete = db.get_or_404(Book, book_id)
    db.session.delete(book_to_delete)
    db.session.commit()
    return redirect(url_for('home'))
```

---

## Deliverables
1. A fully functional web app with:
   - Home page displaying all books.
   - Add, edit, and delete functionalities.
2. HTML templates (`index.html`, `add.html`, `edit.html`).
3. SQLite database to store books.
4. SQLAlchemy models and Flask routes for all CRUD operations.

---

## Notes
- Ensure the app runs without errors (`python app.py`).
- Use Bootstrap or another CSS framework for styling if desired.
- Test all features thoroughly to ensure data integrity and proper navigation.

