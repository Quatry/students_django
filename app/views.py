from django.shortcuts import render, redirect

from app.services import _add_student, _get_students, _get_student, _add_mark
from app.forms import AddForm, AddMarkForm


def add_student(request):
    if request.method == 'POST':
        _add_student(request)
        return redirect('/student/list/')
    form = AddForm()
    return render(request,'add_student.html',{'form':form})

def list_of_students(request):
    info = _get_students(request)
    return render(request,'list_of_students.html',info)

def student(request,id):
    info = _get_student(request,id)
    return render(request,'student.html',info)

def add_mark(request,id):
    if request.method == 'POST':
        _add_mark(request,id)
        return redirect(f'/student/{id}')
    form = AddMarkForm()
    return render(request,'add_mark.html',{'form':form})
