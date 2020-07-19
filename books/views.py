from django.shortcuts import get_object_or_404
from django_filters import rest_framework as filters
from rest_framework import viewsets

from .models import Book
from .serializers import BookListSerializer, BookDetailSerializer


class BookFilter(filters.FilterSet):
    class Meta:
        model = Book
        fields = ['title', ]


class BooksView(viewsets.mixins.ListModelMixin, viewsets.mixins.RetrieveModelMixin,
                viewsets.mixins.CreateModelMixin, viewsets.GenericViewSet):
    """Class with all methods"""
    queryset = Book.objects.all()
    lookup_field = 'id'
    # Filtration
    filter_backends = [filters.DjangoFilterBackend]
    filter_class = BookFilter
    filter_fields = ('title',)
    # Serializer
    default_serializer_class = BookListSerializer
    serializer_classes = {
        'list': BookListSerializer,
        'retrieve': BookDetailSerializer,
        'create': BookDetailSerializer,
    }

    def get_serializer_class(self):
        """Choosing a serializer, and return"""
        return self.serializer_classes.get(self.action,
                                           self.default_serializer_class)

    def get(self, request, *args, **kwargs):
        """Return list of objects"""
        return self.list(request, *args, **kwargs)

    def get_object(self):
        """Additional method for retrieve, return object by id or code 404"""
        pk = self.kwargs.get('id')
        return get_object_or_404(Book, pk=pk)
