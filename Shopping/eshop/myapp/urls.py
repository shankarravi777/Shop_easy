from django.urls import path

from . import views 

urlpatterns = [
    path('', views.store, name='store'),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.login, name='logout'),
    path('cart',views.cart,name='cart'),
    path('checkout',views.checkout,name='checkout'),
    path('update_item/',views.updateItem,name='update_Item'),
    path('process_order/',views.processOrder,name='process_order')
  

]