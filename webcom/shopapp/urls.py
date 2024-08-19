from django.contrib import admin
from django.urls import path
from shopapp import views
urlpatterns = [
    path('', views.home,name='Homie'),
    path('register',views.register,name='register'),
    path('collections',views.collections,name='collections'),
    path('collections/<str:name>',views.collection_view,name='collections_view'),
    path('collections/<str:cname>/<str:pname>',views.product_detail,name='product_view')
]
