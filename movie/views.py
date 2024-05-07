from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
    return render(request,'movie/index.html',{'Movie':'War'})
def about(request):
    return render (request,'movie/about.html')