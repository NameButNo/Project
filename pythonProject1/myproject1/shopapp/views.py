from django.http import HttpResponse
from django.shortcuts import render
from timeit import default_timer

products = [
    ("Phone", 999),
    ("Laptop", 1999),
    ("Macbook", 2999)]

names = [
    "Aram", "Ara", "Bella", "Hugo", "Eva"
]
def shop_index(request):
    con = {
        "time_running": default_timer,
        "products":     products,
        "name": names,
    }
    return render(request, 'shopapp/index.html', context=con)
