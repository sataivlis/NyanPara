from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# View which handles the logic to log in. If there is an error, we redirect to
# the login page, with a failure message. If we are successful, we return to the
def my_login(request):
    # from login.html. The values in this request.POST dictionary are given from
    # homepage, but with a logged-in template.
    # the <input ... name="______">
    try:
        username = request.POST['username']
        password = request.POST['password']
    except:
        return render(request, 'login.html')

    # check to see if the person actually typed in values for username and password
    print("There's a username and password!")
    print(username, password)
    user = authenticate(username=username, password=password)
    print(user)
    if user:
        print("Redirecting to nyannyan!")
        login(request, user)
        return redirect('nyannyan')

    return render(request, 'login.html', {'fail': True})

# Log the user out.
def my_logout(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('nyannyan')

# Render a page with a form to allow users to register a username and password.
def register(request):
    return render(request, 'register.html', {})

# After hitting the "Register" Button, create a User instance into the DB,
# 1. Get the values from the request dictionary (from HTML)
# authenticate the new user, and return to the homepage.
def register_user(request):
    try:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        password = request.POST['password']
        username = request.POST['username']
    except:
        return render(request, 'register.html', {'fail': True})

    # 2. Create a user with that information like we did in the shell
    user = User(username=username, first_name=first_name, last_name=last_name)
    user.set_password(password)

    try:
        user.save()
    except:
        # What should we do in the case where there was an error with registration?
        return render(request, 'register.html', {'fail': True})

    # 3. authenticate the user, then redirect to the homepage.
    login(request, user)
    return redirect('nyannyan')
