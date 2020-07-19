from rest_framework import serializers

from .models import Book


class BookListSerializer(serializers.ModelSerializer):
    """Books list serializer"""

    class Meta:
        model = Book
        fields = ('id', 'title', 'author')


class BookDetailSerializer(serializers.ModelSerializer):
    """Books detail and create serializer"""

    class Meta:
        model = Book
        fields = ('id', 'title', 'author', 'description')
        read_only_fields = ('id',)
