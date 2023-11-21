from django.urls import path

from Shop.views import show_index_page, DetailViewPage

urlpatterns = [
    path('', show_index_page, name='index'),
    path('detail/<int:product_id>/', DetailViewPage.as_view(), name='detail'),
]
