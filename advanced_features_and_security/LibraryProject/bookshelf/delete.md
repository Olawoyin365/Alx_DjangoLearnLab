# Delete Operation

## Command:

from bookshelf.models import Book
>>> book = Book.objects.get(id=1)
>>> book.delete()
>>> Book.objects.all()

## Expected Output:
(1, {'bookshelf.Book': 1})
<QuerySet []>
# The Book instance was successfully deleted, confirmed by an empty QuerySet.
