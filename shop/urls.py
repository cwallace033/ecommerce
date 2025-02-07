from django.urls import path
from .views import home, cart, checkout , add_to_cart, remove_from_cart

urlpatterns = [
    path('', home, name='home'),
    path('cart/', cart, name='cart'),
    path('checkout/', checkout, name='checkout'),
    path('add_to_cart/<int:product_id>/', add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:product_id>/', remove_from_cart, name='remove_from_cart'),
]
