
from django.contrib import admin
from django.urls import path,include

# from product.views import HelloView

urlpatterns = [
    path('accounts/', include('accounts.urls')),
    # path('admin/', admin.site.urls),
    path('product/', include('product.urls')),
]
