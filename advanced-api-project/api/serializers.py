from rest_framework import serializers
from .models import Book, Author

# A BookSerializer that serializes all fields of the Book model.

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"

# Custom validation to ensure the publication_year is not in the future.

    def validate_publication_year(self, value):
        current_year = datetime.now().year
        if value > current_year:
            raise serializers.ValidError("Publication year cannot be in the future")

# An AuthorSerializer that inludes the name field and a bested BookSerializer to serialize the related books dynamically.

class AuthorSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True, read_only=True)

    class Meta:
       model = Author
       fields = ['id', 'name', 'books']
