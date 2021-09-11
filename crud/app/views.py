
from django.shortcuts import render, HttpResponse
from .forms import StudentRegistration
from .models  import Student

def index(request):
    if request.method == 'POST':
        fm = StudentRegistration(request.POST or None, request.FILES or None)
        if fm.is_valid():
            fm.save()
    else:
        fm = StudentRegistration()
    stud = Student.objects.all()
    return render(request, 'app/index.html', {'form':fm, 'stud':stud})


def delete(request, id):
    if request.method =='POST':
        pi = Student.objects.get(pk=id)
        pi.delete()
        return HttpResponse('')


def update(request, id):
    if request.method == 'POST':
        pi = Student.objects.get(pk=id)
        fm = StudentRegistration(request.POST, instance=pi)
        if fm.is_valid():
         fm.save()
    else:
        pi = Student.objects.get(pk=id)
        fm = StudentRegistration(instance=pi)
    return render(request, 'app/updatestudent.html', {'form':fm})
      
