from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from .forms import LoginForm

from .models import Client
from .forms import ClientForm


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('create_client')

        else:
            # print("from else conditon")
            error_message = 'Invalid username or password.'
            context = {'error_message': error_message}
            return render(request, 'login.html', context)
    else:
        return render(request, 'login.html')


def create_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()

    context = {'form': form}
    return render(request, 'create_client.html', context)


def client_list(request):
    query = request.GET.get('query')
    clients = Client.objects.all()

    if query:
        clients = clients.filter(name__icontains=query)

    context = {'clients': clients}
    return render(request, 'client_list.html', context)
