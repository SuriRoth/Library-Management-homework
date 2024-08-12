import json

class Book:
    def __init__(self, title, author, ISBN, copies):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.copies = copies
        
    def __str__(self):
        return f"'{self.title}' by {self.author}, ISBN is {self.ISBN}, {self.copies} copies. "
    
    def __repr__(self):
        return f'Title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}, Copies: {self.copies} '
    
class Ebook(Book):
    def __init__(self, title, author, ISBN, copies, fileFormat):
        super().__init__(title, author, ISBN, copies)
        self.fileFormat = fileFormat
    
    def __str__(self):
        return f"'{self.title}' by {self.author}, ISBN is {self.ISBN}, {self.copies} copies, {self.fileFormat} format. "
    
    def __repr__(self):
        return f'Title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}, Copies: {self.copies}, File format: {self.fileFormat}. '
    

class Member:
    def __init__(self, name, memberID, borrowedBooks):
        self.name = name 
        self.memberID = memberID
        self.borrowedBooks = []
        
    def __str__(self):
        return f'{self.name} with a member ID of {self.memberID}, borrowed {self.borrowedBooks}.'
    
    def __repr__(self):
        return f'Name: {self.name}, Member ID: {self.memberID}, Borrowed Books: {self.borrowedBooks}'
    
    def borrowBook(self, book):
        self.borrowedBooks.append(book)
        print('You have borrowed a book.')
        
    def returnBook(self, book):
        if book in self.borrowedBooks:
            self.borrowedBooks.remove(book)
        print('You have returned your book')
        

class Library:
    def __init__(self, name, books, members):
        self.name = name
        self.books = books
        self.members = members
    
    def addBook(self, book):
        self.books[book.ISBN] = book
        print('You added a book to the library. ')
        
    def removeBook(self, ISBN):
        if ISBN in self.books:
            del self.books[ISBN]
        print('You have removed a book from the library list.')
        
    def addMember(self, member):
        if member in self.members:
            self.members.append(member)
        print('you added a member.')
        
    def removeMember(self, member):
        if member in self.members:
            self.members.remove(member)
        print('You removed a member.')
        
    def lendBook(self, member, book):
        if book.copies > 0 :
            member.borrowBook(book)
            book.copies -= 1
        print('You lent the book out')
        
    def returnBook(self, member, book):
        if book in member.borrowedBooks:
            member.returnBook(book)
            book.copies += 1
        print('This book was returned')
        
    def __str__ (self):
        return f'Library name: {self.name}'
    
    def __repr__(self):
        return f'Library({self.name})'


library = Library("MyLibrary", {}, [])

while True:
    choice = input('Welcome! lets create a new libary system!'
                   'What would you like to do today?')
    title = input("Enter the title of the book: ")
    author = input("Enter the author of the book: ")
    ISBN = input("Enter the ISBN of the book: ")
    copies = int(input("Enter the number of copies: "))
    book = Book(title, author, ISBN, copies)
    library.addBook(book)
    name = input("Enter the name of the member: ")
    memberID = input("Enter the member ID: ")
    member = Member(name, memberID, [])
    library.addMember(member)


    # Add books and members to the library
    library.addBook(book)
    library.addMember(member)

    # Borrowing and returning books
    library.lendBook(member, book)
    library.returnBook(member, book)

    # Save the state of the library to a JSON file
    libraryData = {
        "name": library.name,
        "books": [book.__dict__ for book in library.books.values()],
        "members": [member.__dict__ for member in library.members]
    }

    with open("libraryData.json", "w") as libraryFile:
        json.dump(libraryData, libraryFile, indent=4)
        
    print("Library saved to libraryData.json")

