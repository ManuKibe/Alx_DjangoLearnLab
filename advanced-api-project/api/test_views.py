class BookAPITestCase(APITestCase):
    """
    Test suite for Book API endpoints:
    - CRUD operations
    - Filtering, searching, ordering
    """

    def setUp(self):
        self.client = APIClient()

        # Create an Author
        self.author = Author.objects.create(name="George Orwell")

        # Create Books
        self.book1 = Book.objects.create(
            title="1984", publication_year=1949, author=self.author
        )
        self.book2 = Book.objects.create(
            title="Animal Farm", publication_year=1945, author=self.author
        )

        # Base URLs
        self.list_url = reverse("book-list")  # ListAPIView
        self.crud_url = "/api/books_all/"     # Router ViewSet

    # --- CRUD Tests ---
    def test_create_book(self):
        data = {
            "title": "Homage to Catalonia",
            "publication_year": 1938,
            "author": self.author.id
        }
        response = self.client.post(self.crud_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    def test_get_books(self):
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_update_book(self):
        url = f"{self.crud_url}{self.book1.id}/"
        data = {"title": "Nineteen Eighty-Four", "publication_year": 1949, "author": self.author.id}
        response = self.client.put(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, "Nineteen Eighty-Four")

    def test_delete_book(self):
        url = f"{self.crud_url}{self.book2.id}/"
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 1)

    # --- Filtering, Searching, Ordering ---
    def test_filter_books_by_title(self):
        response = self.client.get(self.list_url, {"title": "1984"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "1984")

    def test_search_books(self):
        response = self.client.get(self.list_url, {"search": "Animal"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Animal Farm")

    def test_order_books_by_publication_year(self):
        response = self.client.get(self.list_url, {"ordering": "publication_year"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]["title"], "Animal Farm")  # 1945 < 1949
