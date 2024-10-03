from django.urls import path

from products.views import GetProductsView

urlpatterns = [
    path('get-products/', GetProductsView.as_view(), name='get-products'),
]