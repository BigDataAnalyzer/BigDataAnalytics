from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'BigDataVisualization/home.html')


def visualize(request):
    return render(request, 'BigDataVisualization/visualize.html')