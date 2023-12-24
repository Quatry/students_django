from django import forms

from app.models import Student, Marks


class AddForm(forms.ModelForm):
    class Meta():
        model = Student
        fields = ['first_name','second_name']


class AddMarkForm(forms.ModelForm):
    class Meta():
        model = Marks
        fields = ['value']