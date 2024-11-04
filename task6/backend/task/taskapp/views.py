from django.shortcuts import render,get_object_or_404,redirect
from .models import Students
from django.http import Http404,HttpResponse
from .forms import StudentForm,UserRegistrationForm
from rest_framework import viewsets
from . import serializers


# Create your views here.
def index(request):
    students = Students.objects.all()
    context = {
        "students":students
    }
    return render(request, 'taskapp/index.html',context)


def edit(request , pk=None):
    if pk:
        student = get_object_or_404(Students, pk=pk)
    else:
        Http404('Error 404')
        return None

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            redirect('index')
        
    else :
        form = StudentForm(instance=student)

    return render(request ,'taskapp/edit.html',{"form":form})



def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new user
            return redirect('login')  # Redirect to login page after successful registration
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form': form})

class StudentViewset(viewsets.ModelViewSet):
    queryset = Students.objects.all()
    serializer_class = serializers.StudentSerializer








