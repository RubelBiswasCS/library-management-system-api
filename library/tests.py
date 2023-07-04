from django.test import TestCase
from .models import Author, Book, Borrower, BorrowingTransaction

class TestAuthorModel(TestCase):
    def setUp(self):
        self.author1 = Author.objects.create(name="Test 1")
        self.author2 = Author.objects.create(name="Test 2")

    def test_authot_model_entry(self):
        author1 = self.author1
        author2 = self.author2

        self.assertTrue(isinstance(author1,Author))
        self.assertTrue(isinstance(author2,Author))
        self.assertEqual(str(author1),'Test 1')
        self.assertNotEqual(str(author2),'Test 1')

    def test_authot_model_retrieve(self):
        authors = Author.objects.all()
        self.assertEqual(authors.count(),2)

class TestBookModel(TestCase):
    def setUp(self):
        self.author = Author.objects.create(name='Test Author')
        Book.objects.create(
            title='Test Book',
            author=self.author,
            publication_date='2022-01-01',
            availability_status=True
        )

    def test_book_model_retrieve(self):
        books = Book.objects.all()
        self.assertEqual(books.count(),1)
        self.assertNotEqual(books.count(),2)

    def test_book_title(self):
        book = Book.objects.get(id=1)
        expected_title = 'Test Book'
        self.assertEqual(book.title, expected_title)

    def test_book_author(self):
        book = Book.objects.get(id=1)
        expected_author = Author.objects.get(id=1)
        self.assertEqual(book.author, expected_author)

    def test_book_publication_date(self):
        book = Book.objects.get(id=1)
        expected_publication_date = '2022-01-01'
        self.assertEqual(str(book.publication_date), expected_publication_date)

    def test_book_availability_status(self):
        book = Book.objects.get(id=1)
        expected_availability_status = True
        self.assertEqual(book.availability_status, expected_availability_status)