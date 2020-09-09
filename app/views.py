from django.shortcuts import render


def index(request):
    context = {
        "title": "Learning Materialize"
    }
    return render(request, "app/index.html", context)
