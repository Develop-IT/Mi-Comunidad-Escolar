from django.shortcuts import render

def login(request):
    log_nav = True
    ctx = {
        'log_nav':log_nav,
    }
    return render(request, "login.html", ctx)
