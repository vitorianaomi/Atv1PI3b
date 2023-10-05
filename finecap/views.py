from django.shortcuts import render, get_object_or_404, redirect
from .models import Reserva
from .forms import ReservaForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required(login_url='/accounts/login')
def reserva_detalhar(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    context = {'reserva': reserva}
    return render(request, 'detalhe.html', context)


@login_required(login_url='/accounts/login')
def reserva_editar(request,id):
    reserva = get_object_or_404(Reserva,id=id)
   
    if request.method == 'POST':
        form = ReservaForm(request.POST,instance=reserva)

        if form.is_valid():
            form.save()
            return redirect('reserva_listar')
    else:
        form = ReservaForm(instance=reserva)

    return render(request,'formreserva.html',{'form':form})

@login_required(login_url='/accounts/login')
def reserva_remover(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect('reserva_listar')


@login_required(login_url='/accounts/login')
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


@login_required(login_url='/accounts/login')
def reserva_listar(request):
    reservas = Reserva.objects.all().order_by('data')
    paginator = Paginator(reservas, 5)
    pagina = request.GET.get('pag')
    pag_obj = paginator.get_page(pagina)
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
        'pag_obj': pag_obj
    }
    return render(request, "reservas.html", context)


@login_required(login_url='/accounts/login')
def index(request):
    objetos = Reserva.objects.count()
    context = {'objetos': objetos}
    return render(request, 'index.html', context)