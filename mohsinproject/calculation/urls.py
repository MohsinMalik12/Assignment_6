from django.urls import path
from . import views

urlpatterns = [
    path('total_sum', views.total_sum, name='sum'),
    path('total_average', views.total_average, name='average'),
    path('total_product', views.total_product, name='product'),
]