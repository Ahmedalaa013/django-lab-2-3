from contextlib import redirect_stderr
from django.shortcuts import render,redirect

from .models import Student

from .forms import StudentForm

# Create your views here.

def student_select(request):
    context = {'student_select': Student.objects.all()}
    return render(request, "student_register/student_select.html",context)

def student_form(request,id=0):
 if request.method == "GET":
      if id==0: 
          form = StudentForm()
      else:
          student = Student.objects.get(pk=id)
          form = StudentForm(instance=student)
      return render(request, "student_register/student_form.html",{'form':form})
 else:
    if id==0:  
          form = StudentForm(request.POST)
    else:
         student = Student.objects.get(pk=id)
         form = StudentForm(instance=student)
    if form.is_valid():
          form.save()
    return redirect('/student/select')     

def student_delete(request,id):
     student = Student.objects.get(pk=id)
     student.delete()
     return redirect('/student/select')
