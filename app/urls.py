from django.urls import path, include

from app.views import add_student, list_of_students, student, add_mark

app_name = 'app'

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('add/', add_student, name='add_student'),
    path('list/', list_of_students, name='list_of_stundents'),
    path('<int:id>/', student, name='student'),
    path('<int:id>/addmark', add_mark, name='add_mark')
]
