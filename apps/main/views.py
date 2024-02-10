from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    return render(request, 'main/index.html')


def lolasdasdasd(request):
    return render(request, 'main/lol.html')