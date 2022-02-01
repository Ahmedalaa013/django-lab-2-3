from django.urls import path, include
from . import views
urlpatterns = [
    
    path('',views.student_form,name="student_insert"),
    path('<int:id>',views.student_form,name="student_update"),
    path('delete/<int:id>',views.student_delete,name="student_delete"),
    path('form/',views.student_form,name="student_insert"),
    path('select/', views.student_select,name="student_select"),
]
