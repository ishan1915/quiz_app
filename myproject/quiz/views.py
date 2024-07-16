from django.shortcuts import render, get_object_or_404
from .models import Quiz1
from django.shortcuts import render, redirect
from .forms import QuizForm,SignUpForm
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth.decorators import login_required



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username,password=raw_password)
            login(request,user)
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request,'signup.html',{'form':form})    

def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user)
                return redirect('create_quiz')  # Redirect to create quiz page after login
    else:
        form = AuthenticationForm()
    
    return render(request, 'login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')
  
def quiz_list(request):
    quizzes = Quiz1.objects.all()
    return render(request, 'quiz_list.html', {'quizzes': quizzes})

def quiz_list1(request):
    query = request.GET.get('q','')  # Get the search query from the GET parameters

    if query:
        quizzes = Quiz1.objects.filter(title__icontains=query)  # Case-insensitive search by title
    else:
        quizzes = Quiz1.objects.all()  # If no query, display all quizzes

    return render(request, 'quiz_list1.html' ,{'quizzes':quizzes, 'query':query})

def quiz_view(request, quiz_id):
    quiz = get_object_or_404(Quiz1, pk=quiz_id)
    context = {
        'quiz': quiz,
    }
    return render(request, 'quiz.html', context)

def quiz_result(request, quiz_id):
    quiz = get_object_or_404(Quiz1, pk=quiz_id)
    selected_option = request.POST.get('option')
    correct_option = quiz.correct_option

    # Check if selected option is correct
    if selected_option == correct_option:
        is_correct = True
    else:
        is_correct = False

    context = {
        'quiz': quiz,
        'selected_option': selected_option,
        'is_correct': is_correct,
        'correct_option': correct_option,
    }
    return render(request, 'result.html', context)


 
def create_quiz(request):
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.user=request.user
            quiz.save()  
            return redirect('create_quiz')  
    else:
        form = QuizForm()
    
    return render(request, 'quiz_form.html', {'form': form})
      