from django.shortcuts import render

def nyannyan(request):
    return render(request, 'Nyan/nyannyan.html', {})
