from django.urls import path, include
from.views import detalle_cliente, index

urlpatterns = [
    path('invoices/', index, name="invoices"),
    path('clientes/<int:id>', detalle_cliente, name= "cliente"),
]
