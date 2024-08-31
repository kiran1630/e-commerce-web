from django.contrib import admin
from django.urls import path
from shopapp import views
urlpatterns = [
    path('', views.home,name='Homie'),
    path('register',views.register,name='register'),
    path('login',views.login_page,name='login'),
    path('logout',views.logout_page,name='logout'),
    path('collections',views.collections,name='collections'),
    path('collections/<str:name>',views.collection_view,name='collections_view'),
    path('collections/<str:cname>/<str:pname>',views.product_detail,name='product_view')
]
