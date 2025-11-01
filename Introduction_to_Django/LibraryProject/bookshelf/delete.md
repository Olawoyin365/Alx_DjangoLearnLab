# Delete Operation

## Command:
>>> book = Book.objects.get(id=1)
>>> book.delete()
>>> Book.objects.all()

## Expected Output:
(1, {'app_name.Book': 1})
<QuerySet []>
# The Book instance was successfully deleted, confirmed by an empty QuerySet.
