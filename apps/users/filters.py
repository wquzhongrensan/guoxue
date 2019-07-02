from rest_framework import generics
from django_filters import rest_framework as filters
from .models import UserProfile


class UserFilter(filters.FilterSet):
    username = filters.CharFilter(field_name="username", lookup_expr='exact')

    class Meta:
        model = UserProfile
        fields = ['username', ]

#
# class BookDetailATFilter(filters.FilterSet):
#     book_type_id = filters.CharFilter(field_name="book_type_id", lookup_expr='exact')
#
#     class Meta:
#         model = BookDetail
#         fields = ['book_type_id']