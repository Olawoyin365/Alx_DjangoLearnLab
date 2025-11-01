# Update Operation

## Command:
>>> book = Book.objects.get(id=1)
>>> book.title = "Nineteen Eighty-Four"
>>> book.save()
>>> book.title

## Expected Output:
'Nineteen Eighty-Four'
# The Book title was successfully updated from "1984" to "Nineteen Eighty-Four".
