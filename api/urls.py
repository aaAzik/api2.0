from django.urls import path, include
from .views import *

urlpatterns = [
    path('user/', user),
    path('user/<int:pk>/', user_detail),
    path('product/', product),
    path('product/<int:pk>/', product_detail),
    path('category/', category),
    path('category/<int:pk>/', category_detail),
    path('auth/', include('dj_rest_auth.urls')),
]
