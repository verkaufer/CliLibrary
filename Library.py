import argparse
#import library as Library
from Book import Book
from Bookshelf import Bookshelf

bookshelf = Bookshelf()

def addBook(args):
    book = Book(args.title, args.author)
    bookshelf.add(book)

def removeBook(args):
    if(args.all):
        print "all books"
    elif(args.title):
        print "remove book with title"

def readBook(args):
    bookshelf.read(args.title)

def showBooks(args):
    pass

def main():

    parser = argparse.ArgumentParser(description="Command line utility to add/remove/list/update books in a virtual library.")

    subparsers = parser.add_subparsers(help='subcommand help')

    ## Add book
    parser_add = subparsers.add_parser('add', help='Add new book to library')
    parser_add.add_argument('title', help='Title of the book')
    parser_add.add_argument('author', help='Author of the book')
    parser_add.set_defaults(func=addBook)

    ## Remove book(s)
    parser_remove = subparsers.add_parser('remove', help='Remove book(s) from library')
    r_group = parser_remove.add_mutually_exclusive_group(required=True)
    r_group.add_argument('-all', '-a', help='Remove all books', action='store_true')
    r_group.add_argument('-title', '-t', help='Remove specific book with title')
    parser_remove.set_defaults(func=removeBook) ## this will print 'hello' and the -title argument

    ## Read book
    parser_readBook = subparsers.add_parser('read', help='Read book with given title')
    parser_readBook.add_argument('title', help='Title of book to read')
    parser_readBook.set_defaults(func=readBook)

    ## Show book(s)
    parser_show = subparsers.add_parser('show', help='Show list of books in library')
    parser_show.add_argument('-author', help='Show books by author')

    show_group = parser_show.add_mutually_exclusive_group()
    show_group.add_argument('-unread', '-u', help='Show unread books', action='store_true')
    show_group.add_argument('-read', '-r', help='Show read books', action='store_true')

    # Bookmark book
    parser_bookmark = subparsers.add_parser('bookmark', help='Add bookmark to a book')
    parser_bookmark.add_argument('title', help='Title of the book')
    parser_bookmark.add_argument('page', help='Page to set bookmark', type=int)


    ## final setup
    args = parser.parse_args()
    #print args	
    args.func(args)

if __name__ == "__main__":
    main()
	
	