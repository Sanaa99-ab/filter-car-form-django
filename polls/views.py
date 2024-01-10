# polls/views.py

from django.shortcuts import render
from .forms import CarSearchForm
from .models import Car 


def car_search_view(request):
    if request.method == 'POST':
        form = CarSearchForm(request.POST)
        if form.is_valid():
            marque = form.cleaned_data.get('marque')
            modele = form.cleaned_data.get('modele')
            annee = form.cleaned_data.get('annee')
           
            price = form.cleaned_data.get('price')

            cars = Car.objects.all()

            if marque:
                cars = cars.filter(marque__icontains=marque)
            if modele:
                cars = cars.filter(modele__icontains=modele)
            if annee:
                cars = cars.filter(annee=annee)
            if price:
                cars = cars.filter(price__lte=price)

            if not cars.exists():
                message = None

            print(f"Marque: {marque}, Modele: {modele}, Annee: {annee}, Price: {price}")  # Add a debug print
            print(f"Number of cars found: {cars.count()}")  

            return render(request, 'car_search.html', {'form': form, 'cars': cars})
    else:
        form = CarSearchForm()

    return render(request, 'car_search.html', {'form': form})


def car_list_view(request):
    cars = Car.objects.all()
    return render(request, 'car_list.html', {'cars': cars})