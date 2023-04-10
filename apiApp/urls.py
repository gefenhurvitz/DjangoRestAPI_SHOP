from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from apiApp.views import product_list


urlpatterns = [
    path('products/', product_list, name='product_list'),
    # path('products/<int:pk>/', ProductDetail.as_view(), name='product_detail'),
    # path('orders/', OrderList.as_view(), name='order_list'),
    # path('orders/<int:pk>/', OrderDetail.as_view(), name='order_detail'),
    # path('users/', UserList.as_view(), name='user_list'),
    # path('users/<int:pk>/', UserDetail.as_view(), name='user_detail'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
