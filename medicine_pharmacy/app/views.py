from django.http import HttpResponse
from django.shortcuts import render
from app.models import Pharmacy, Medicine
from django.contrib import messages


def user_input(request):
    context = {'pharmacies': Pharmacy.objects.all(),
               'medicines': Medicine.objects.all()}

    return render(request, 'index.html', context=context)


def price_output(request):
    name = request.POST['name']
    location = request.POST['location']
    medicines = Medicine.objects.get(name=name)

    def calculate_price():
        price = Medicine.price
        if location == Pharmacy.location:
            price = Medicine.price
        elif 1 < location < 10:
            price *= Pharmacy.margin
        return price

    profitable_price = calculate_price()

    message = messages.info(request,
                            "Вы находитесь на {} км шоссе. Самая выгодная цена для доставки лекарства {} составляет {:.2f}".format(
                                location, name, profitable_price))

    return render(request, 'index.html', context=message)
