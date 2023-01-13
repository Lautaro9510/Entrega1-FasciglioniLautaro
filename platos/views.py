from django.shortcuts import render
from platos.models import Platos
from platos.forms import PlatosForm

# Create your views here.

def lista_platos(request):
    if 'search' in request.GET:
        search = request.GET['search']
        plato = Platos.objects.filter(nombre__icontains=search)
    else:
        plato = Platos.objects.all()
    context = {
        'platos':plato,
    }
    return render(request, 'platos/lista_platos.html', context=context)


def crear_plato(request):
    if request.method == 'GET':
        context = {
            'form': PlatosForm()
        }

        return render(request, 'platos/crear_plato.html', context=context)

    elif request.method == 'POST':
        form = PlatosForm(request.POST)
        if form.is_valid():
            Platos.objects.create(
                nombre=form.cleaned_data['nombre'],
                especialidad=form.cleaned_data['especialidad'],
                precio=form.cleaned_data['precio'],
                stock=form.cleaned_data['stock'],
                apto_vegano=form.cleaned_data['apto_vegano'],
                apto_vegetariano=form.cleaned_data['apto_vegetariano'],
                apto_celiaco=form.cleaned_data['apto_celiaco'],

            )
            context = {
                'message': 'Plato creado exitosamente'
            }

        else:
            context = {
                'form_errors': form.errors,
                'form': PlatosForm()
            }
        return render(request, 'platos/crear_plato.html', context=context)
