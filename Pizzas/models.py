from django.db import models


class Pizzas(models.Model):
    name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.name}"


class Topping(models.Model):
    name = models.CharField(max_length=30)
    pizza = models.ForeignKey('Pizzas', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"

