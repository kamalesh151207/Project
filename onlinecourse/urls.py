from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('exam/', views.exam, name='exam'),
    path('submit/', views.submit, name='submit'),
    path('show_exam_result/', views.show_exam_result, name='show_exam_result'),
]