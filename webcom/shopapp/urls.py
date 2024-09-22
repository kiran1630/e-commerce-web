from django.contrib import admin
from django.urls import path
from shopapp import views
urlpatterns = [
    path('', views.home,name='Homie'),
    path('register',views.register,name='register'),
    path('login',views.login_page,name='login'),
    path('logout',views.logout_page,name='logout'),
    path('remove_cart/<str:cid>',views.remove_cart,name='remove_cart'),
    path('fav',views.fav,name='fav'),
    path('fav_page',views.fav_page,name='fav_page'),
    path('remove_fav/<str:rid>',views.remove_fav,name='remove_fav'),


    path('cart',views.cart_page,name='cart'),
    path('addtocart',views.add_to_cart,name='addtocart'),
    path('collections',views.collections,name='collections'),
    path('collections/<str:name>',views.collection_view,name='collections_view'),
    path('collections/<str:cname>/<str:pname>',views.product_detail,name='product_view')
]
