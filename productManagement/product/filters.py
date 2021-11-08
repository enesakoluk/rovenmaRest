from django_filters import rest_framework as filters
from product.models import Products


# We create filters for each field we want to be able to filter on
class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    id = filters.CharFilter(lookup_expr='icontains')
    barcodeNumber = filters.CharFilter(lookup_expr='icontains')
    stockInformation = filters.NumberFilter()
    created_at_gt = filters.NumberFilter(field_name='year', lookup_expr='gt')
    created_at_lt = filters.NumberFilter(field_name='year', lookup_expr='lt')
    
    class Meta:
        model = Products
        fields=["id","name","created_at","updated_at","categoryId","stockInformation","barcodeNumber"]






