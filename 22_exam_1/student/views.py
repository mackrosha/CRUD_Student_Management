from django.shortcuts import render,redirect
from .models import Student
from . import models
from . import forms
from django.contrib import messages
# Create your views here.


# html From
# def home(request):
#     print(request.POST)
#     if request.method == 'POST':
#         fullname = request.POST.get('fullname')
#         email = request.POST.get('email')
#         course = request.POST.get('course')
#         number = request.POST.get('number')
#         photo = request.FILES.get('photo')
        


#         student = Student(fullname=fullname, email=email, course=course, number=number, photo=photo)
#         student.save()
#         return render(request, 'student/index.html')
    
#     return render(request, 'student/index.html')


# Model From
def create_student(request):
    if request.method == 'POST':
        form = forms.StudentFrom(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Student Create successfully.')
            return redirect('home')
    else:
        form = forms.StudentFrom()
    return render(request, 'student/create_edit_student.html', {'form': form})




def home(request):
    students = models.Student.objects.all()
    return render(request, 'student/index.html', {'students': students})



def update_student(request, id):
    student = Student.objects.get(id=id)
    form = forms.StudentFrom(instance=student)
    if request.method == 'POST':
        form = forms.StudentFrom(request.POST, request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Student Data Update successfully.')
            return redirect('home')
    # form = forms.StudentFrom(request.POST or None, request.FILES or None, instance=student)
    return render(request, 'student/create_edit_student.html', {'form': form, 'edit' : True})


def delete_student(request, id):
    student = Student.objects.get(id=id)
    student.delete()
    messages.add_message(request, messages.SUCCESS, 'Student Delete successfully.')
    return redirect('home')