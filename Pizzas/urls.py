from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('home/', views.home, name='home'),
    path('pizzas/', views.pizzas, name='pizzas'),
    path('concrete_pizza/<int:pizza_id>', views.concrete_pizza, name='concrete_pizza'
                                                                     ''
                                                                     ''
                                                                     '')

]