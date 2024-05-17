from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    a={
        'movies':['War','Avengers','casino']
    }
    return render(request,'movie/index.html',a)
def about(request):
    return render (request,'movie/about.html')