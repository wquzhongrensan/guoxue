from django_filters import rest_framework as filters
from .models import BookDetail


class BookFilter(filters.FilterSet):
    """
    书籍过滤字段定义
    """
    name_con = filters.CharFilter(field_name="name", lookup_expr='contains')

    class Meta:
        model = BookDetail
        fields = ['name_con', 'author']


class BookDetailATFilter(filters.FilterSet):
    """
    书籍详情过滤字段定义
    """
    book_type_id = filters.CharFilter(field_name="book_type_id", lookup_expr='exact')

    class Meta:
        model = BookDetail
        fields = ['book_type_id']
