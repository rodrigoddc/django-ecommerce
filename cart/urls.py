from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'cart'

urlpatterns = [
    #url(r'^$', views.cart_detail, name='cart_detail'),
    path('', views.cart_detail, name='cart_detail'),
    #url(r'^add/(?P<product_id>\d+)/$', views.cart_add, name='cart_add'),
    path('add/<product_id>)', views.cart_add, name='cart_add'),
    #url(r'^remove/(?P<product_id>\d+)/$', views.cart_remove, name='cart_remove'),
    path('remove/<product_id>', views.cart_remove, name='cart_remove'),
]
