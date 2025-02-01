from django.urls import path
from . import views
urlpatterns = [
    path('home/',views.home, name='home'),
    path('create/',views.create_student, name='create_student'),
    path('edit/<int:id>/',views.update_student, name='update_student'),
    path('delete/<int:id>/',views.delete_student, name='delete_student'),
]
