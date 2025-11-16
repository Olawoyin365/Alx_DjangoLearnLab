from relationship_app.models import Author, Book, Library, Librarian

#Query all books by a specific author
author_name = "Ibrahim Olawoyin"
author = Author.objects.get(name=author_name)
books_by_author = Book.objects.filter(author=author)
print(f"Books by {author.name}:")
for book in books_by_author:
    print("-", book.title)


#List all books in a specific library
library_name = "Haven Library"
library = Library.objects.get(name=library_name)
books_in_library = library.books.all()
print(f"\nBooks in {library.name}:")
for book in books_in_library:
    print("-", book.title)


#Retrieve the librarian for a specific library
library_name = "Haven Library"
library = Library.objects.get(name=library_name)
librarian = Librarian.objects.get(library=library)
print(f"\nLibrarian for {library.name}: {librarian.name}")
