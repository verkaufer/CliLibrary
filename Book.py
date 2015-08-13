class Book:
	""" Model for Book object """
	
	def __init__(self, title, author):
		self.title = title
		self.author = author
		self.bookmark = None
		self.read = False
		
	def setBookmark(self, page):
		""" Sets bookmark attribute of a book to given page """
		self.bookmark = page
		
	def read(self):
		""" Changes read status of a book """
		self.read = True
		