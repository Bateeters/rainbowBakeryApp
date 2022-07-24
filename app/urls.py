from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.item_list, name='item_list'),
    path('item/new/', views.item_new, name='item_new'),
    path('item/<int:pk>/edit/', views.item_edit, name="item_edit"),
    path('item/<int:pk>/', views.item_detail, name='item_detail'),
    path('item/<pk>/remove/', views.item_remove, name='item_remove'),
    url(r'/', views.item_remove, name='item_remove'),
]
