class Book:
    def __init__(self,title,author,available=True):
        self.title = title
        self.author = author
        self.available = available

    def borrow(self):
        if self.available:
            self.available = False
            return f"{self.title} can be borrowed."
        else:
            return f"Someone already borrowed."

    def return_book(self):
        if not self.available:
            self.available = True
            return f"You have returned {self.title}, author{self.author}."
        else:
            return f"The book was not borrowed."
        
    def view(self):
        status = "available" if self.available else "borrowed"
        return f"{self.title} by {self.author} is {status}."

class User:
    def __init__(self,name,role):
        self.name = name
        self.role = role

class Member(User):
    def __init__(self,name):
        super().__init__(name,"Member")

    def borrow(self,book):
        result = book.borrow()
        if "can be borrowed" in result:
            return f"{result} The book is borrowed by {self.name}."
        else:
            return result 

    def return_book(self,book):
        return book.return_book()

class Librarian(User):
    def __init__(self,name):
        super().__init__(name,"Librarian")
        self.library = []

    def add_books(self,book):
        self.library.append(book) 
        print(f"{self.name} added {book.title}.") 

    def view_books(self):
        print(f"{self.name} is viewing all books in the library.")
        for book in self.library:
            print(book.view())


        
book = Book("King", "Rosie")
book1 = Book("Queen", "Honey")
member = Member("Balmond")
librarian = Librarian("Saraha")

# Librarian adds books
librarian.add_books(book)
librarian.add_books(book1)

# View all books in the library
librarian.view_books()

# Member borrows a book
print(member.borrow(book1))

# View the status of the borrowed book
print(book1.view())

# Member returns the book
print(member.return_book(book1))

# View the status of the returned book
print(book1.view())