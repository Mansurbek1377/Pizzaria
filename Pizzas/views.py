from django.shortcuts import render
from .models import Pizzas, Topping


def index(request):
    return render(request, 'Pizzas/index.html')


def home(request):
    return render(request, 'Pizzas/home.html')


def pizzas(request):
    all_pizzas = Pizzas.objects.all()
    return render(request, 'Pizzas/pizzas.html', {'all_pizzas': all_pizzas})


#
# def toppings(request):
#     return (request)
#

def concrete_pizza(request, pizza_id):
    pizza = Pizzas.objects.get(id=pizza_id)
    concrete_pizza = pizza.topping_set.all()

    return render(request, 'Pizzas/concrete_pizza.html', {'pizza': pizza,
                                                  'concrete_pizza': concrete_pizza})
