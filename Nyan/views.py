from django.shortcuts import render
from .models import UserCat, Cat

def nyannyan(request):
    if request.user.is_authenticated:
        # We can put this logic in the HTML
        # if they have cats, show cats
        # else show "eggs"

        # Write a query to get all of the User's cat's
        user = request.user
        users_cats = UserCat.objects.filter(owner=user)

        return render(request, 'Nyan/nyannyan.html', {"users_cats": users_cats })


        ### doesn't work bc jumps straight to adopt page...
        # if user doesn't have cat?
        # if users_cats.exists():
        #     # give option to get a cat
        #     return render(request, 'Nyan/nyannyan.html', {"users_cats": users_cats })
        # if yes then just display
        # else:
        #     return render(request, 'adopt.html', {})

    else:
        print('user needs to log in!')
        return render(request, 'login.html', {})
