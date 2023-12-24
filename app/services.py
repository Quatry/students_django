from app.forms import AddForm
from .models import Student, Marks
from django.db.models import Avg

def _add_student(request):
    add = AddForm(request.POST)
    if add.is_valid():
        form = add.save()


def _get_students(request):
    students = Student.objects.annotate(avg_mark=Avg('marks__value'))
    return {'students':students}

def _get_student(request,id):
    student = Student.objects.get(id=id)
    student_marks = student.marks.all()
    return {'student':student,
            'student_marks':student_marks}
def _add_mark(request,id):
    value = request.POST['value']
    student = Student.objects.get(id=id)
    mark = Marks(student=student,value=value)
    mark.save()

def _delete_student(request,id):
    student = Student.objects.get(id=id)
    student.delete()
    return '/student/list'