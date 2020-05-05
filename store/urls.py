from django.urls import path
from .import views


urlpatterns = [
    #leave as empty string for base url
    path('',views.store,name='store'),
    path('cart/',views.cart,name='cart'),
    path('checkout/',views.checkout,name='checkout'),
    
    path('updateitem/',views.updateItem,name='updateitem'),
    path('processOrder/',views.processOrder,name='processOrder'),




]
