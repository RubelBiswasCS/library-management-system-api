from rest_framework import serializers
from library.models import Author, Book

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = [ 'id','first_name','last_name' ]
        depth = 1

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [ 'id', 'title','author','publication_date', 'availability_status' ]

       
