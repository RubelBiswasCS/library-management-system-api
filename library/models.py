from django.db import models
import uuid

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=50)

    @property
    def get_books(self):
        books = self.books.all()
        return books

    def __str__(self):
        return f"{self.name}"

class Book(models.Model):
    # title, author, publication date, and availability status.
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name='books', on_delete=models.CASCADE)
    publication_date = models.DateField()
    availability_status = models.BooleanField()

    def __str__(self):
        return f"{self.title}"

class Borrower(models.Model):
    name = models.CharField(max_length=50)
    phone = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.name}"

class BorrowingTransaction(models.Model):
    transaction_id = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    book = models.ManyToManyField(Book)
    borrower = models.ForeignKey(Borrower, on_delete=models.CASCADE)
    due_date = models.DateField()

    def __str__(self):
        return f"{self.borrower.name}-{self.transaction_id}"
