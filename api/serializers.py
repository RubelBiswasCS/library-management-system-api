from rest_framework import serializers
from library.models import Author, Book, Borrower, BorrowingTransaction

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [ 'id', 'title','author','publication_date', 'availability_status' ]

class AuthorSerializer(serializers.ModelSerializer):
    books = serializers.SerializerMethodField(method_name='get_books')

    class Meta:
        model = Author
        fields = [ 'id','name', 'books' ]

    def get_books(self,obj):
        return BookSerializer(obj.get_books,many=True).data
    
class BorrowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Borrower
        fields = [ 'id', 'name','phone' ]

class BorrowingTransactionSerializer(serializers.ModelSerializer):

    class Meta:
        model = BorrowingTransaction
        fields = [ 'id','transaction_id', 'book', 'borrower', 'due_date' ]