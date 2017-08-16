from django.shortcuts import render


def frontpage(request):
    """ Index page. """
    return render(request, 'index.html')
