from django.urls import path
from .views import ProductList, ProductCreate, ProductDetail, ProductUpdate, ProductDelete

urlpatterns = [
    path('tasks/', ProductList.as_view(), name='task-list'),
    path('tasks/create/', ProductCreate.as_view(), name='task-create'),
    path('tasks/<int:pk>/', ProductDetail.as_view(), name='task-detail'),
    path('tasks/update/<int:pk>/', ProductUpdate.as_view(), name='task-update'),
    path('tasks/delete/<int:pk>/', ProductDelete.as_view(), name='task-delete'),
]