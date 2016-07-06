from django.shortcuts import render

def index(request):
    home_nav = True
    ctx = {
        'home_nav':home_nav,
    }
    return render(request, "index.html", ctx)
