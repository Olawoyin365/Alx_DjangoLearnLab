from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework import status
from django.contrib.auth.models import User
from .models import Book, Author


class BookAPITests(APITestCase):

    def setUp(self):
        # Create test user
        self.user = User.objects.create_user(
            username="testuser",
            password="testpass123"
        )

        # Create author
        self.author = Author.objects.create(name="John Doe")

        # Authenticated client
        self.client = APIClient()
        self.client.login(username="testuser", password="testpass123")

        # Endpoints
        self.list_url = reverse("book-list")      # /books/
        self.create_url = reverse("book-list")    # same as list for POST

    def test_create_book(self):
        data = {
            "title": "New Book",
            "publication_year": 2020,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 1)
        self.assertEqual(response.data["title"], "New Book")

    def test_list_books(self):
        Book.objects.create(
            title="Sample Book",
            publication_year=2015,
            author=self.author
        )

        response = self.client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_retrieve_book(self):
        book = Book.objects.create(
            title="Detail Book",
            publication_year=2018,
            author=self.author
        )
        url = reverse("book-detail", args=[book.id])

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Detail Book")

    def test_update_book(self):
        book = Book.objects.create(
            title="Old Title",
            publication_year=2010,
            author=self.author
        )
        url = reverse("book-detail", args=[book.id])

        data = {
            "title": "Updated Title",
            "publication_year": 2011,
            "author": self.author.id
        }

        response = self.client.put(url, data, format="json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        book.refresh_from_db()
        self.assertEqual(book.title, "Updated Title")

    def test_delete_book(self):
        book = Book.objects.create(
            title="Delete Me",
            publication_year=2000,
            author=self.author
        )
        url = reverse("book-detail", args=[book.id])

        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    def test_authentication_required(self):
        unauth_client = APIClient()

        response = unauth_client.get(self.list_url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
