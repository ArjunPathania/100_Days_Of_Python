import sqlite3

#creating a database
db = sqlite3.connect("books-collection.db")

#creating a cursor
cursor = db.cursor()

#creating a table
# cursor.execute("CREATE TABLE books (id INTEGER PRIMARY KEY, title varchar(250) NOT NULL UNIQUE, author varchar(250) NOT NULL, rating FLOAT NOT NULL)")

#adding entry to table
cursor.execute("INSERT INTO books VALUES(1, 'Harry Potter', 'J. K. Rowling', '9.3')")
db.commit()