from .models import Reserva
from django.forms import TextInput
import django_filters


class ReservaFilter(django_filters.FilterSet):

    cnpj = django_filters.CharFilter(
        widget=TextInput(
            attrs={'class': 'form-control', 'style':'width: 300px; heigth: 50px; margin-left: 10px; margin-right: 10px;'}),
            lookup_expr='icontains')

    class Meta:
        model = Reserva
        fields = ['cnpj', 'nome_empresa', 'categoria_empresa', 'stand', 'data']
