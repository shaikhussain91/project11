from django.shortcuts import render

def home(request):
    return render(request,'home.html')

def courses(request):
    return render(request,'courses.html')

def bootcamp(request):
    return render(request,'bootcamp.html')

def requestcallback(request):
    return render(request,"callback.html")

def signin(request):
    return render(request,"signin.html")

def form(request):
    return render(request,"form.html")

def bootform(request):
    return render(request,"bootform.html")

def freelearning(request):
    return render(request,"freelearning.html")
