from django.conf.urls import url,include
from django.urls import path
from product import models, views
from product.views import ListCreateProductAPIView,RetrieveUpdateDestroyProductAPIView


urlpatterns = [
   
    
     path('', ListCreateProductAPIView.as_view(), name='filter'),
     path('<int:pk>', RetrieveUpdateDestroyProductAPIView.as_view(), name='get_delete_update_Product'),


   

]
 
 
 
 
 
 
 
 
 