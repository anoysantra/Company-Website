from django.http import HttpResponse
from django.shortcuts import render
from . models import JobPost,Consultant
from .forms import JobPostForm,ConsultationForm

# Create your views here.


def post_job(request):

    if request.method=='POST':
        form=JobPostForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Job Added</h1>')
        
    else:
        form=JobPostForm()

    jobs = JobPost.objects.all()

    return render(request, 'jobs_page.html', {'form':form, 'jobs':jobs})


def consult(request):

    if request.method=='POST':
        form=ConsultationForm(request.POST)

        if form.is_valid():
            form.save()
            print("validated")
            return HttpResponse('<h1>Booking Added</h1>')
        
        else:
            print("Errors:", form.errors)
        
    else:
        form=ConsultationForm()


    return render(request, 'consultancy.html', {'form':form})
