from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.quiz_list, name='quiz_list'),
    path('create/', views.create_quiz, name='create_quiz'),
    path('<int:quiz_id>/quiz', views.quiz_view, name='quiz'),
    path('<int:quiz_id>/result/', views.quiz_result, name='result'),
    # other URL patterns
]