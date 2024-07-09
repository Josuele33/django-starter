from django.shortcuts import render
from .models import Cliente, Factura

def index(request):
    print("Han solicitado invoices/")
    # clientes = [1, 2, 3]
    # facturas = ['a', 'b', 'c']

    clientes = list(Cliente.objects.all())
    facturas = list(Factura.objects.all())

    context = {
        "secret": "Supersafe123/",
        "clientes": clientes,
        "facturas": facturas,
    }
    return render(request, "a_invoices/index.html", context=context)


def detalle_cliente(request, id):
    cliente = Cliente.objects.all().filter(pk=id).first()
    context = {
        "cliente": cliente
    }
    return render(request, "a_invoices/clientes.html", context=context)