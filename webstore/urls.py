from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('login/',views.user_login, name='login'),
    path('logout/',views.user_logout, name='logout'),
    path('register/',views.register, name='register'),
    path('guest/',views.guest, name='guest'),
    path('apanel/',views.apanel, name='apanel'),
    path('product/<str:pk>/',views.product_page, name='product_page'),
    path('addproduct/',views.add_product, name='addproduct'),
    path('delp/<str:pk>',views.del_product, name='del_product'),
    path('search/',views.search, name='search'),
    path('checkout/<str:pk>',views.checkout, name='checkout'),
    path('cart/<str:pk>/',views.cart, name='cart'),
    path('payment/',views.payment, name='payment'),
    path('thanks/',views.thanks, name='thanks'),
    path('myorders/<str:pk>',views.my_orders, name='my_orders'),
    path('status/',views.status, name='status'),
    path('ustatus/',views.update_status, name='update_status'),
    path('stats/',views.stats, name='stats'),
]
