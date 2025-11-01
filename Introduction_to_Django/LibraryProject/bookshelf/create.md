# Create Operation

## Command:
>>> from bookshelf.models import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> book

## Expected Output:
<Book: Book object (1)>
# The Book instance "1984" by George Orwell (1949) was successfully created.
