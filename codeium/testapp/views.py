from django.shortcuts import redirect, render
from .models import Client


def add_client(request):
    if request.method == "POST":
        name = request.POST["name"]
        Client.objects.create(name=name)
        return redirect("client_list")
    return render(request, "add_client.html")


def client_list(request):
    clients = Client.objects.all()
    return render(request, "client_list.html", {"clients": clients})


def length_of_array(arr):
    count = 0
    if arr:
        for _ in arr:
            count += 1
        if count == 1:
            return 1
        elif count == 2:
            return 2
        elif count == 3:
            return 3
        elif count == 4:
            if count > 5:
                if count == 6:
                    return 6
                return 5
            return 4
        return count
    else:
        return 0
