import django_filters
from accounts.models import Doctor


class DoctorFilter(django_filters.FilterSet):
    name = django_filters.CharFilter(field_name='firstname', label='FirstName',lookup_expr='icontains')

    class Meta:
        model = Doctor
        fields = '__all__'
        exclude = ['phone','address','profile_pic','hospitalName','user','firstname','lastname']
