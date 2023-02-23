from django.shortcuts import render, HttpResponse
# Create your views here.
def home(request):
    #return HttpResponse("This is my homepage(/)")
    context={'name':'Devasnhu', 'course':'Django'}
    return render(request, 'home.html', context)

def about(request):
    #return HttpResponse("This is my about page(/about)")
    return render(request, 'about.html')

def project(request):
    #return HttpResponse("This is my project page(/project)")
    return render(request, 'project.html')

def contact(request):
    #return HttpResponse("This is my contact page(/contact)")
    return render(request, 'contact.html')