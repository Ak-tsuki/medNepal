import django_filters
from django.contrib.auth.models import User


class UserFilter(django_filters.FilterSet):
    email_contains = django_filters.CharFilter(field_name='email', label='Email', lookup_expr='icontains')

    class Meta:
        model = User
        fields = []