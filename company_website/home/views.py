from django.http import HttpResponse
from django.shortcuts import render
from . forms import ContactForm
from . models import ContactMessage
# Create your views here.

def homeview(request):
    return render(request, 'home.html')


def review(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
           
            return HttpResponse('<h1>Successfully Submitted</h1>')  
    else:
        form = ContactForm()

    return render(request, 'contact_template.html', {'form': form})



def engineering_course(request):
    return render(request, 'engineering_course.html')



def software_course(request):
    return render(request,'software.html')

def contact_us(request):
    return render(request,'contact_us.html')

def placement(request):
    return render(request,'placement.html')

def products(request):
    return render(request, 'products.html')

def construction(request):
    return render(request, 'construction.html')

def construction_services(request):
    return render(request, 'construction_detail.html')


