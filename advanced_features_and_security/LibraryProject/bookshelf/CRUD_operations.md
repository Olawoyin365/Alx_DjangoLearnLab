# CRUD Operations in Django Shell

This document captures all CRUD (Create, Retrieve, Update, Delete) operations performed using the Django shell.

---

## CREATE
>>> from bookshelf.models import Book
>>> book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
>>> book

<Book: Book object (1)>
# The Book instance "1984" by George Orwell (1949) was successfully created.

---

## RETRIEVE
>>> from bookshelf.models import Book
>>> book = Book.objects.get(id=1)
>>> book.title
>>> book.author
>>> book.publication_year

'1984'
'George Orwell'
1949
# Successfully retrieved the Book instance with all its details.

---

## UPDATE
>>> book = Book.objects.get(id=1)
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> book.title

'Nineteen Eighty-Four'
# The Book title was successfully updated from "1984" to "Nineteen Eighty-Four".

---

## DELETE
from bookshelf.models import Book
>>> book = Book.objects.get(id=1)
>>> book.delete()
>>> Book.objects.all()

(1, {'bookshelf.Book': 1})
<QuerySet []>
# The Book instance was successfully deleted, confirmed by an empty QuerySet.
