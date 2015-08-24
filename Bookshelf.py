import Book
import json, sqlite3

class Bookshelf(object):
  
  def add(self, book):
    print "{} by {} added to bookshelf.".format(book.title, book.author)