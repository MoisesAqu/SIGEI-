from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def login_view(request):

    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            if user.groups.filter(name='Administradores').exists():
                return redirect('dashboard_admin')

            elif user.groups.filter(name='Compradores').exists():
                return redirect('dashboard_compras')

            elif user.groups.filter(name='Vendedores').exists():
                return redirect('dashboard_ventas')

            elif user.groups.filter(name='Almacenistas').exists():
                return redirect('dashboard_inventario')

    return render(request, 'usuarios/login.html')


def logout_view(request):
    logout(request)
    return redirect('login')
    