from django.shortcuts import render

def show_main(request):
    context = {
        'name': 'Eudora Vanya Lindsay',
        'class': 'PBP D'
    }

    return render(request, "main.html", context)