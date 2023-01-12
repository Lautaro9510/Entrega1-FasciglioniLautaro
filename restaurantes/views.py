from django.shortcuts import render
from restaurantes.models import Restaurantes
from restaurantes.forms import RestaurantesForm

# Create your views here.

def lista_restaurantes(request):
    if 'search' in request.GET:
        search = request.GET['search']
        restaurante = Restaurantes.objects.filter(name__icontains=search)
    else:
        restaurante = Restaurantes.objects.all()
    context = {
        'restaurantes':restaurante,
    }
    return render(request, 'restaurantes/lista_restaurantes.html', context=context)


def crear_restaurante(request):
    if request.method == 'GET':
        context = {
            'form': RestaurantesForm()
        }

        return render(request, 'restaurantes/crear_restaurante.html', context=context)

    elif request.method == 'POST':
        form = RestaurantesForm(request.POST)
        if form.is_valid():
            Restaurantes.objects.create(
                nombre=form.cleaned_data['nombre'],
                especialidad=form.cleaned_data['especialidad'],
                direccion=form.cleaned_data['direccion'],
                abierto=form.cleaned_data['abierto'],

            )
            context = {
                'message': 'Restaurante creado exitosamente'
            }

        else:
            context = {
                'form_errors': form.errors,
                'form': RestaurantesForm()
            }
        return render(request, 'restaurantes/crear_restaurante.html', context=context)
