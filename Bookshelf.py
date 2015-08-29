import Book
import json
import sqlite3

class Bookshelf(object):
  
  def _connectDB(self):
    """
    Setup a DB connection 
    """
    connection = sqlite3.connect('mybooks.db')

    #Set the row_factory to let us call row values by column name
    connection.row_factory = sqlite3.Row
    
    return connection

  def add(self, book):
    """
    Add a new book to our library database. 
    Book object should contain title and author
    """
    db = self._connectDB()

    db.execute('INSERT INTO books (title, author) VALUES(?, ?)', (book.title, book.author))
    db.commit()
    db.close()

    print "{} by {} added to bookshelf.".format(book.title, book.author)

  def read(self, title):
    """
    Set status of book with given title to 'read' 
    In SQLite database, this is a 0 or 1 value 
    """
    db = self._connectDB()

    # Check if book exists and return its PK `id`
    cur = db.cursor()
    cur.execute('SELECT id FROM books WHERE title = ?', [title])
    if cur.fetchone() is None:
        print "Could not find book with title: {}".format(title)
        return

    # Book exists, save reference to book id
    bookID = cur.fetchone[0]

    # Set isRead to 1 because we are marking book as read
    try:
        with db:
            db.execute('UPDATE books SET isRead = 1 WHERE id = ?', [bookID])
    except Exception as e:
        db.rollback()
        raise e

    # Everything went well, commit to DB and close connection. Return success string.    
    db.commit()
    db.close()
    print "You just read {}".format(title)

    