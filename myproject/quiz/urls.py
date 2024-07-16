from django.urls import path
from . import views
from .views import quiz_list1


urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout/',views.logout_view,name='logout'),
    
    path('list/', views.quiz_list, name='quiz_list'),
    path('list1/', quiz_list1, name='quiz_list1'),

    path('create/', views.create_quiz, name='create_quiz'),
    path('<int:quiz_id>/quiz', views.quiz_view, name='quiz'),
    path('<int:quiz_id>/result/', views.quiz_result, name='result'),
    # other URL patterns
]