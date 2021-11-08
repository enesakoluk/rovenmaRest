
from rest_framework import serializers
from product.models import Products


class ProductSerializer(serializers.ModelSerializer):
  
    user=serializers.ReadOnlyField(source='user.username')
   
    
    class Meta:
        model=Products
        fields=("id","name","created_at","updated_at","categoryId","stockInformation","barcodeNumber","user")


    