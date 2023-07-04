from rest_framework import generics

from library.models import Author, Book, Borrower, BorrowingTransaction
from .serializers import BookSerializer, AuthorSerializer, BorrowerSerializer, BorrowingTransactionSerializer

class BookList(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class AuthorList(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class AuthorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    lookup_field = 'pk'

class BorrowerList(generics.ListCreateAPIView):
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer

class BorrowerDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Borrower.objects.all()
    serializer_class = BorrowerSerializer
    lookup_field = 'pk'

class BorrowingTransactionList(generics.ListCreateAPIView):
    queryset = BorrowingTransaction.objects.all()
    serializer_class = BorrowingTransactionSerializer

class BorrowingTransactionDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BorrowingTransaction.objects.all()
    serializer_class = BorrowingTransactionSerializer
    lookup_field = 'pk'


