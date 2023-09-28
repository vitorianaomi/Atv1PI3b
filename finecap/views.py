from django.shortcuts import render, get_object_or_404, redirect
from .models import Reserva
from .forms import ReservaForm

# Create your views here.


def index(request):
    objetos = Reserva.objects.all()
    context = {'objetos': objetos}
    return render(request, 'index.html', context)


def reserva_remover(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect('reserva_listar')


def reserva_criar(request):
    if request.method == 'POST':
        form = ReservaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('reserva_listar')
        else:
            print(form.errors)
    else:
        form = ReservaForm()
    return render(request, 'formreserva.html', {'form': form})


def reserva_listar(request):
    reservas = Reserva.objects.all().order_by('data')
    if (request.GET.get('nome_empresa')):
        reservas = reservas.filter(
            nome_empresa__contains=request.GET.get('nome_empresa'))
    if request.GET.get('quitado') and request.GET.get('naoquitado'):
        pass
    else:
        if (request.GET.get('quitado')):
            reservas = reservas.filter(quitado=True)
        if (request.GET.get('naoquitado')):
            reservas = reservas.filter(quitado=False)
    if (request.GET.get('valor')):
        reservas = reservas.filter(stand__valor=request.GET.get('valor'))
    if (request.GET.get('data')):
        reservas = reservas.filter(data__date=request.GET.get('data'))
    context = {
        'reservas': reservas
    }
    return render(request, "reservas.html", context)


def reserva_detalhar(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    context = {'reserva': reserva}
    return render(request, 'detalhe.html', context)
