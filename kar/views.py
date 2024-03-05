from django.shortcuts import render
def home(request):
    return render(request,"index.html")
def cone(request):
    return render(request,"obito.html")
def pain(request):
    return render(request,"yhiko.html")
def login(request):
    return render(request,"naruto.html")
def sign(request):
    return render(request,"minato.html")

# Create your views here.
