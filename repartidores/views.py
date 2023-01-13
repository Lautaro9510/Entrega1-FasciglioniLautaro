from django.shortcuts import render
from repartidores.models import Repartidores
from repartidores.forms import RepartidoresForm

# Create your views here.

def lista_repartidores(request):
    if 'search' in request.GET:
        search = request.GET['search']
        repartidor = Repartidores.objects.filter(name__icontains=search)
    else:
        repartidor = Repartidores.objects.all()
    context = {
        'repartidores':repartidor,
    }
    return render(request, 'repartidores/lista_repartidores.html', context=context)


def crear_repartidor(request):
    if request.method == 'GET':
        context = {
            'form': RepartidoresForm()
        }

        return render(request, 'repartidores/crear_repartidor.html', context=context)

    elif request.method == 'POST':
        form = RepartidoresForm(request.POST)
        if form.is_valid():
            Repartidores.objects.create(
                nombre=form.cleaned_data['nombre'],
                vehiculo=form.cleaned_data['vehiculo'],
                direccion=form.cleaned_data['direccion'],
                email=form.cleaned_data['email'],
                telefono=form.cleaned_data['telefono'],
                esta_trabajando=form.cleaned_data['esta_trabajando']

            )
            context = {
                'message': 'Repartidores creado exitosamente'
            }

        else:
            context = {
                'form_errors': form.errors,
                'form': RepartidoresForm()
            }
        return render(request, 'repartidores/crear_repartidor.html', context=context)
