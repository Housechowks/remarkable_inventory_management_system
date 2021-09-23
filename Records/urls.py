from django.urls import path
from .views import (
    home_view,
    SaleListView,
    sale_list_view,
    sale_detail_view,
    SaleDetailView,
    )


app_name = 'Records'

urlpatterns = [
    path('', home_view, name = 'home'),
    path('Records/', sale_list_view, name = 'list'),
    path('Records/<pk>/', sale_detail_view, name = 'detail'),
]