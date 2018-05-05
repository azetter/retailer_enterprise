from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .import views
from homepage.models import *
from homepage.views import StoreList, ProductList, SalesList

urlpatterns = [
    # Index page
    path('', views.index, name ='index'),

    # Stores/
    path('stores/', StoreList.as_view()),

    # Products/
    path('products/', ProductList.as_view()),

    # Sales/
    # path('sales/', views.queryTest, name='sales'),
    path('sales/', SalesList.as_view()),

     # Sales/
    # path('storesales/', views.queryTest1, name='store'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
