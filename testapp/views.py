from django.shortcuts import render

# Create your views here.


def helloDjango(request):

    return render(request, 'hello.html')


def example(request):

    return render(request, 'example.html')