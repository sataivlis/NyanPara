from django.shortcuts import render

def nyannyan(request):
    if request.user.is_authenticated:
        return render(request, 'Nyan/nyannyan.html')
    else:
        print('user needs to log in!')
        return render(request, 'login.html', {})
