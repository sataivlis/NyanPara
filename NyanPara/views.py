from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def my_login(request):
    # from login.html. The values in this request.POST dictionary are given from
    # the <input ... name="______">
    username = request.POST['username']
    password = request.POST['password']

    # check to see if the person actually typed in values for username and password
    if username and password:
        print("There's a username and password!")
        print(username, password)
        user = authenticate(username=username, password=password)
        print(user)
        if user:
            print("Redirecting to nyannyan!")
            login(request, user)
            return redirect('nyannyan')

    return render(request, 'login.html', {'fail': True})

def my_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('nyannyan')
