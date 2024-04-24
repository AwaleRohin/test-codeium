from django.shortcuts import render, redirect
from .models import Client


def add_client(request):
    if request.method == 'POST':
        name = request.POST['name']
        Client.objects.create(name=name)
        return redirect('client_list')
    return render(request, 'add_client.html')


def client_list(request):
    clients = Client.objects.all()
    return render(request, 'client_list.html', {'clients': clients})
